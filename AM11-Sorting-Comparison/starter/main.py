"""Sorting comparison: bring tested sorts here, then design a fair experiment."""


def selection_sort(lst):
    """TODO: use the tested in-place selection sort from AM8."""
    raise NotImplementedError("Implement or bring in tested selection_sort.")


def insertion_sort(lst):
    """TODO: use the tested in-place insertion sort from AM8."""
    raise NotImplementedError("Implement or bring in tested insertion_sort.")


def bubble_sort(lst):
    """TODO: use basic in-place bubble sort, labeling any optimization."""
    raise NotImplementedError("Implement or bring in tested bubble_sort.")


def merge_sort(lst):
    """TODO: return a sorted new list with indexed merging, not pop(0)."""
    raise NotImplementedError("Implement or bring in tested merge_sort.")


def partition(lst, pivot):
    """TODO: group values less/equal/greater than the pivot VALUE."""
    raise NotImplementedError("Implement or bring in tested partition.")


def quicksort(lst, rng=None):
    """TODO: return a sorted new list with optional repeatable random pivots."""
    raise NotImplementedError("Implement or bring in tested quicksort.")


def make_workloads(size, rng):
    """TODO: derive four input shapes; require an integer size from 0 to 2000."""
    raise NotImplementedError("Implement shared random/sorted/reversed/duplicate data.")


def time_sort(sorter, values):
    """TODO: time sorting only, using a copy, and reject incorrect results."""
    raise NotImplementedError("Implement checked timing with perf_counter.")


def benchmark(sizes=(100, 300), repeats=3, seed=0, algorithms=None):
    """TODO: return measured medians; bound sizes, size count and repeats."""
    raise NotImplementedError("Implement a bounded, repeatable sorting experiment.")


if __name__ == "__main__":
    print("Implement the experiment TODOs after sorting correctness checks pass.")
    print("Use random.Random(0) for repeatable data; see README.md for the contract.")
