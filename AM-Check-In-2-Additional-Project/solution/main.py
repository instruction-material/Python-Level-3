"""Import-safe two-sort experiment; measured medians are not Big-O proofs."""

import math
import random
from statistics import median
from time import perf_counter


def selection_sort2(lst):
    for i in range(len(lst)):
        minimum = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minimum]:
                minimum = j
        lst[i], lst[minimum] = lst[minimum], lst[i]
    return lst


def insertion_sort2(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    return lst


def _integer(value, name, minimum, maximum=None):
    if (isinstance(value, bool) or not isinstance(value, int)
            or value < minimum or (maximum is not None and value > maximum)):
        raise ValueError(name + " is outside the documented integer bounds")


def make_workloads(n, seed=0):
    _integer(n, "n", 0, 2000)
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer, not bool")
    rng = random.Random(seed)
    values = [rng.randint(1, max(1, n * 10)) for _ in range(n)]
    ordered = sorted(values)
    return {"random": values, "sorted": ordered, "reversed": ordered[::-1]}


def time_sort(sorter, values):
    expected = sorted(values)
    working = values.copy()
    start = perf_counter()
    result = sorter(working)
    elapsed = perf_counter() - start
    if result != expected:
        raise AssertionError("Sorter did not return the correct ascending list")
    if not math.isfinite(elapsed) or elapsed < 0:
        raise RuntimeError("Clock did not produce a finite nonnegative duration")
    return elapsed


def benchmark(sizes=(100, 300), repeats=3, seed=0, sorters=None):
    sizes = tuple(sizes)
    if not 1 <= len(sizes) <= 5:
        raise ValueError("Use one to five sizes")
    for n in sizes:
        _integer(n, "size", 0, 2000)
    _integer(repeats, "repeats", 1, 10)
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer, not bool")
    if sorters is None:
        sorters = {"selection": selection_sort2, "insertion": insertion_sort2}
    if (not isinstance(sorters, dict) or not 1 <= len(sorters) <= 2
            or not all(callable(sorter) for sorter in sorters.values())):
        raise ValueError("Use one or two named callable sorters")
    rows = []
    for n in sizes:
        shapes = make_workloads(n, seed)
        for shape, values in shapes.items():
            for name, sorter in sorters.items():
                samples = [time_sort(sorter, values) for _ in range(repeats)]
                rows.append({
                    "algorithm": name, "shape": shape, "n": n,
                    "repeats": repeats, "seconds": median(samples),
                })
    return rows


if __name__ == "__main__":
    print("Measured medians: 3 runs; generation, copying, validation and printing excluded.")
    print("Small two-sort review experiment, not Big-O proof.")
    for row in benchmark():
        print(row["algorithm"], row["shape"], row["n"],
              format(row["seconds"], ".9f"), "seconds")
