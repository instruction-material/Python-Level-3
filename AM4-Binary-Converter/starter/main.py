"""AM4 supplemental: implement both decimal-to-binary approaches."""


def to_binary_iterative(number):
    """Return a nonnegative integer's binary digits as text, with no 0b prefix."""
    # TODO: collect remainders and preserve the correct digit order.
    raise NotImplementedError("Implement to_binary_iterative before running the checks.")


def to_binary_recursive(number):
    """Return the same digits using a stopping case and smaller recursive input."""
    # TODO: keep all arithmetic integer-based, including for large integers.
    raise NotImplementedError("Implement to_binary_recursive before running the checks.")


if __name__ == "__main__":
    try:
        for value in (0, 1, 6, 2**60 + 7):
            print(value, to_binary_iterative(value), to_binary_recursive(value))
    except NotImplementedError as error:
        print(error)
