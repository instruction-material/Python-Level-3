"""AM4: this project uses positions 1 and 2 for the starting values 0 and 1."""


def fibonacci(n):
    """Return the nth Fibonacci value for a positive integer n."""
    # TODO: stop at the two starting positions; combine smaller calls afterward.
    raise NotImplementedError("Implement fibonacci before running the checks.")


if __name__ == "__main__":
    try:
        for position in (1, 2, 5, 8):
            print(position, fibonacci(position))
    except NotImplementedError as error:
        print(error)
