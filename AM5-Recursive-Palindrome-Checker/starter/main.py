"""AM5-Recursive-Palindrome-Checker: an incomplete learner exercise, separate from the reference."""


def is_palindrome(text):
    """Return whether text is a literal, case-sensitive palindrome."""
    # TODO: Choose stopping cases, compare the ends, then reduce the middle.
    raise NotImplementedError("Implement is_palindrome before running the checks.")


if __name__ == "__main__":
    try:
        for text in ("", "a", "abba", "abc"):
            print(repr(text), is_palindrome(text))
    except NotImplementedError as error:
        print(error)
