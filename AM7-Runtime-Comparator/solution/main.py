"""Comparable, bounded search batches; no experiment runs during import."""

import math
import platform
import random
import statistics
import time


def linear_search(list1, item):
    """Return Boolean membership without changing the input sequence."""
    for value in list1:
        if value == item:
            return True
    return False


def bin_search_iter(lst, item):
    """Search sorted values by inclusive index bounds, without copying slices."""
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == item:
            return True
        if lst[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return False


def bin_search_recur(lst, item):
    """Optional original slice-based search: logarithmic comparisons, linear copying."""
    if not lst:
        return False
    mid = (len(lst) - 1) // 2
    if lst[mid] == item:
        return True
    if lst[mid] < item:
        return bin_search_recur(lst[mid + 1:], item)
    return bin_search_recur(lst[:mid], item)


def _count(value, minimum, maximum, label):
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{label} must be an integer from {minimum} through {maximum}.")


def make_workload(size=2000, queries=50, seed=0):
    """Return fresh seeded integer data and targets without changing global RNG state."""
    _count(size, 0, 5000, "size")
    _count(queries, 0, 100, "queries")
    if type(seed) is not int:
        raise ValueError("seed must be an integer.")
    rng = random.Random(seed)
    return (
        [rng.randint(0, 100000) for _ in range(size)],
        [rng.randint(0, 100000) for _ in range(queries)],
    )


def _integers(values, maximum, label):
    if not isinstance(values, list) or len(values) > maximum:
        raise ValueError(f"{label} must be a list with at most {maximum} items.")
    if any(type(value) is not int for value in values):
        raise ValueError(f"Every {label} item must be an integer, not Boolean.")


def _checked_batch(search, values, targets, expected, original):
    actual = [search(values, target) for target in targets]
    _check_results(values, original, actual, expected)
    return actual


def _check_results(values, original, actual, expected):
    if values != original:
        raise AssertionError("A search changed its working input.")
    if any(type(value) is not bool for value in actual) or actual != expected:
        raise AssertionError("Search results differ from the independent membership oracle.")


def _elapsed(start, end):
    for value in (start, end):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("Clock readings must be finite numbers.")
        try:
            finite = math.isfinite(value)
        except OverflowError as error:
            raise ValueError("Clock readings must be finite numbers.") from error
        if not finite:
            raise ValueError("Clock readings must be finite numbers.")
    elapsed = end - start
    try:
        finite_elapsed = math.isfinite(elapsed)
    except OverflowError as error:
        raise ValueError("Elapsed time must be finite.") from error
    if elapsed < 0 or not finite_elapsed:
        raise ValueError("The clock must yield finite, nondecreasing readings.")
    return elapsed


def compare_searches(nums, targets, repeats=3, clock=None):
    """Return two measured median rows; preparation and verification are not timed."""
    _integers(nums, 5000, "nums")
    _integers(targets, 100, "targets")
    _count(repeats, 1, 10, "repeats")
    clock = time.perf_counter if clock is None else clock
    if not callable(clock):
        raise ValueError("clock must be callable.")

    query_batch = tuple(targets)
    membership = set(nums)
    expected = [target in membership for target in query_batch]
    original = nums[:]
    sorted_values = sorted(nums)
    experiments = (
        ("linear", linear_search, original, "original"),
        ("binary", bin_search_iter, sorted_values, "sorted"),
    )

    # Both algorithms pass a warm-up oracle check before either is timed.
    for _, search, values, _ in experiments:
        _checked_batch(search, values[:], query_batch, expected, values)

    rows = []
    for name, search, values, order in experiments:
        samples = []
        for _ in range(repeats):
            working = values[:]
            start = clock()
            actual = [search(working, target) for target in query_batch]
            end = clock()
            _check_results(working, values, actual, expected)
            samples.append(_elapsed(start, end))
        rows.append({
            "algorithm": name,
            "size": len(nums),
            "queries": len(query_batch),
            "hits": sum(expected),
            "repeats": repeats,
            "input_order": order,
            "median_seconds": statistics.median(samples),
        })
    return rows


def main(size=2000, queries=50, repeats=3, seed=0):
    """Print the measured batch medians and environment; return the same report rows."""
    nums, targets = make_workload(size, queries, seed)
    rows = compare_searches(nums, targets, repeats)
    print(f"Python {platform.python_version()} ({platform.python_implementation()}), seed={seed}")
    print("Shared targets/multiset; generation, sorting, copies and checks are not timed.")
    print("Linear input is original-order; binary input is sorted. Hit position can differ.")
    for row in rows:
        print(
            f"{row['algorithm']}: median_seconds={row['median_seconds']:.9g}, "
            f"size={row['size']}, queries={row['queries']}, "
            f"hits={row['hits']}, repeats={row['repeats']}, order={row['input_order']}"
        )
    print("These are measured local batches, not a proof of Big-O or an end-to-end sort cost.")
    return rows


if __name__ == "__main__":
    main()
