"""Two-sort review experiment. See README.md; no automatic benchmark."""


def selection_sort2(lst):
    """Sort ascending in place; return the same list."""
    raise NotImplementedError("Implement selection_sort2 before calling it.")


def insertion_sort2(lst):
    """Sort ascending in place; return the same list."""
    raise NotImplementedError("Implement insertion_sort2 before calling it.")


def make_workloads(n, seed=0):
    """Prepare shared random, sorted and reversed shapes outside timing."""
    raise NotImplementedError("Implement make_workloads before calling it.")


def time_sort(sorter, values):
    """Copy before timing; validate afterward; return measured seconds."""
    raise NotImplementedError("Implement time_sort before calling it.")


def benchmark(sizes=(100, 300), repeats=3, seed=0, sorters=None):
    """Return rows of measured medians for the bounded experiment."""
    raise NotImplementedError("Implement benchmark before calling it.")


if __name__ == "__main__":
    print("Implement the sorting and experiment TODOs; run only small, deliberate benchmarks.")
