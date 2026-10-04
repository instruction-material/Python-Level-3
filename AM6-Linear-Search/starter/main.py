"""AM6: scan an input list without using the in operator to solve the search."""


def linear_search(values, target):
    """Return a bool indicating whether target occurs in values."""
    # TODO: distinguish finding an item from finishing the entire scan.
    raise NotImplementedError("Implement linear_search before running the checks.")


if __name__ == "__main__":
    try:
        for values, target in (([], 1), ([1, 2, 3], 1), ([1, 2, 3], 3), ([1, 2, 3], 4)):
            print(values, target, linear_search(values, target))
    except NotImplementedError as error:
        print(error)
