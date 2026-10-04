"""AM7: both searches require an input list already sorted in ascending order."""


def bin_search_iter(lst, item):
    """Return a bool indicating whether item occurs in sorted lst, using a loop."""
    # TODO: track the remaining interval and make it smaller on every step.
    raise NotImplementedError("Implement bin_search_iter before running the checks.")


def bin_search_recur(lst, item):
    """Return the same membership result using recursion."""
    # TODO: handle an empty search interval and recurse into a strictly smaller half.
    raise NotImplementedError("Implement bin_search_recur before running the checks.")


if __name__ == "__main__":
    try:
        for values, target in (([], 1), ([1], 1), ([1, 4, 5, 8], 8), ([1, 4, 5, 8], 6)):
            print(values, target, bin_search_iter(values, target), bin_search_recur(values, target))
    except NotImplementedError as error:
        print(error)
