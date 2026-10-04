"""AM5-Recursive-Sum-and-Max: an incomplete learner exercise, separate from the reference."""


def sum_recursion(values):
    """Return the recursive sum of a numeric list; the empty sum is zero."""
    # TODO: Choose a stopping case and combine a value with a smaller list.
    raise NotImplementedError("Implement sum_recursion before running the checks.")


def max_recursion(values):
    """Return the recursive maximum; raise ValueError for an empty list."""
    # TODO: Make the base case work for negative numbers, not just positive ones.
    raise NotImplementedError("Implement max_recursion before running the checks.")


if __name__ == "__main__":
    try:
        for values in ([4], [1, 2, 3], [-8, -3, -5]):
            print(values, sum_recursion(values), max_recursion(values))
        print("Empty sum:", sum_recursion([]))
    except NotImplementedError as error:
        print(error)
