"""AM5-Recursive-Cascade: an incomplete learner exercise, separate from the reference."""


def cascade(s):
    """Print nonempty prefixes of s from shortest to longest, using recursion."""
    # TODO: Decide what an empty input does and when each prefix is printed.
    raise NotImplementedError("Implement cascade before running the checks.")


def inverse_cascade(s):
    """Print the same prefixes in reverse order, using recursion."""
    # TODO: Move the print relative to the smaller recursive call.
    raise NotImplementedError("Implement inverse_cascade before running the checks.")


if __name__ == "__main__":
    try:
        cascade("dog")
        inverse_cascade("dog")
    except NotImplementedError as error:
        print(error)
