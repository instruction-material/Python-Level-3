"""AM-Check-In-1-Additional-Project: an incomplete learner exercise, separate from the reference."""


def sum_print(nums):
    """Print running sums of nums in forward order; empty input prints nothing."""
    # TODO: Trace how the print position relates to the smaller recursive call.
    raise NotImplementedError("Implement sum_print before running the checks.")


def sum_print_reverse(nums):
    """Print the same running sums in reverse order; empty input prints nothing."""
    # TODO: Compare printing before and after the recursive call.
    raise NotImplementedError("Implement sum_print_reverse before running the checks.")


if __name__ == "__main__":
    try:
        sum_print([4, 5, 2])
        sum_print_reverse([4, 5, 2])
    except NotImplementedError as error:
        print(error)
