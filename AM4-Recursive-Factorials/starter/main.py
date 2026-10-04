"""AM4: implement a recursive factorial for a nonnegative integer."""


def recursive_factorial(num):
    """Return num factorial, including the zero case. Do not use math.factorial."""
    # TODO: choose the stopping case, then reduce num toward it.
    raise NotImplementedError("Implement recursive_factorial before running the checks.")


if __name__ == "__main__":
    try:
        for number in (0, 1, 5):
            print(number, recursive_factorial(number))
    except NotImplementedError as error:
        print(error)
