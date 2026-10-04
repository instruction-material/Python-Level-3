"""AM4: compute a power with recursion rather than the ** operator."""


def exponent(base, power):
    """Return base raised to a nonnegative integer power."""
    # TODO: decide the zero-power case and a recursive step that reduces power.
    raise NotImplementedError("Implement exponent before running the checks.")


if __name__ == "__main__":
    try:
        for base, power in ((2, 0), (2, 3), (5, 2), (-2, 3)):
            print(base, power, exponent(base, power))
    except NotImplementedError as error:
        print(error)
