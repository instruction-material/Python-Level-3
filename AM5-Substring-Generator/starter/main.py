"""AM5-Substring-Generator: an incomplete learner exercise, separate from the reference."""


def get_substrings(string):
    """Return a sorted list of distinct contiguous substrings, including empty text."""
    # TODO: Remove characters only from the ends; do not skip interior characters.
    raise NotImplementedError("Implement get_substrings before running the checks.")


if __name__ == "__main__":
    try:
        for text in ("", "ab", "aba", "abc"):
            print(repr(text), get_substrings(text))
    except NotImplementedError as error:
        print(error)
