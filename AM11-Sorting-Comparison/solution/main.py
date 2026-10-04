"""Bounded, checked sorting experiment. No experiment runs during import."""

import random
from statistics import median
from time import perf_counter


def selection_sort(lst):
    """Sort in place, choosing the minimum of the remaining suffix."""
    for i in range(len(lst)):
        min_item_i = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_item_i]:
                min_item_i = j
        lst[i], lst[min_item_i] = lst[min_item_i], lst[i]
    return lst


def insertion_sort(lst):
    """Sort stably in place by growing the sorted prefix."""
    for i in range(len(lst)):
        j = i
        while j != 0 and lst[j] < lst[j - 1]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    return lst


def bubble_sort(lst):
    """Basic in-place bubble sort, intentionally without early exit."""
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def merge_sort(lst):
    """Stable sorted copy using indexed linear merging, not pop(0)."""
    if len(lst) <= 1:
        return lst.copy()
    midpoint = len(lst) // 2
    left = merge_sort(lst[:midpoint])
    right = merge_sort(lst[midpoint:])
    result = []
    a = b = 0
    while a < len(left) and b < len(right):
        if left[a] <= right[b]:
            result.append(left[a])
            a += 1
        else:
            result.append(right[b])
            b += 1
    result.extend(left[a:])
    result.extend(right[b:])
    return result


def partition(lst, pivot):
    """Partition around a pivot value, preserving order within each group."""
    less, equal, greater = [], [], []
    for value in lst:
        if value < pivot:
            less.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            greater.append(value)
    return less, equal, greater


def quicksort(lst, rng=None):
    """Return a new sorted list with repeatable optional random pivots."""
    if len(lst) <= 1:
        return lst.copy()
    generator = random if rng is None else rng
    pivot = lst[generator.randint(0, len(lst) - 1)]
    less, equal, greater = partition(lst, pivot)
    return quicksort(less, generator) + equal + quicksort(greater, generator)


def make_workloads(size, rng):
    """Derive random, sorted, reversed and duplicate-heavy shared inputs."""
    if type(size) is not int or not 0 <= size <= 2000:
        raise ValueError("size must be an integer from 0 to 2000")
    values = [rng.randint(-10000, 10000) for _ in range(size)]
    ordered = sorted(values)
    return {
        "random": values,
        "sorted": ordered,
        "reversed": ordered[::-1],
        "duplicates": [rng.randint(-2, 2) for _ in range(size)],
    }


def time_sort(sorter, values):
    """Time only sorting a fresh copy; reject wrong results after timing."""
    expected = sorted(values)
    working = values.copy()
    start = perf_counter()
    result = sorter(working)
    elapsed = perf_counter() - start
    if result != expected:
        raise AssertionError("Sorting result is incorrect; do not report its speed.")
    return elapsed


def benchmark(sizes=(100, 300), repeats=3, seed=0, algorithms=None):
    """Return measured median seconds with bounded sizes and repeat counts."""
    if type(repeats) is not int or not 1 <= repeats <= 10:
        raise ValueError("repeats must be an integer from 1 to 10")
    sizes = tuple(sizes)
    if not 1 <= len(sizes) <= 5:
        raise ValueError("provide between one and five sizes")
    for size in sizes:
        if type(size) is not int or not 0 <= size <= 2000:
            raise ValueError("sizes must be integers from 0 to 2000")
    workloads_rng = random.Random(seed)
    pivot_rng = random.Random(seed)
    if algorithms is None:
        algorithms = {
            "Selection Sort": selection_sort,
            "Insertion Sort": insertion_sort,
            "Bubble Sort (basic)": bubble_sort,
            "Merge Sort": merge_sort,
            "Quicksort": lambda values: quicksort(values, pivot_rng),
        }
    rows = []
    for size in sizes:
        for shape, values in make_workloads(size, workloads_rng).items():
            for name, sorter in algorithms.items():
                samples = [time_sort(sorter, values) for _ in range(repeats)]
                rows.append({
                    "size": size,
                    "shape": shape,
                    "algorithm": name,
                    "repeats": repeats,
                    "median_seconds": median(samples),
                })
    return rows


if __name__ == "__main__":
    print("Measured medians: 3 runs, shared input copies, seed 0.")
    print("Sorting only; generation, copying, validation and printing excluded.")
    print("These small local measurements illustrate behavior, not Big-O proof.")
    for row in benchmark():
        print(
            f"{row['size']:4} {row['shape']:10} "
            f"{row['algorithm']:20} {row['median_seconds']:.6f} seconds"
        )
