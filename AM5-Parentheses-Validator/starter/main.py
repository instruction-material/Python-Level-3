"""AM5-Parentheses-Validator: an incomplete learner exercise, separate from the reference."""


def parentheses(brackets):
    """Return whether a bracket-only string is balanced, using a stack."""
    # TODO: Reject mismatched closers and any non-bracket character.
    raise NotImplementedError("Implement parentheses before running the checks.")


def rec_parentheses(brackets):
    """Return the same bracket-only balance result using recursive reduction."""
    # TODO: Choose a stopping case and a reduction that makes the input shorter.
    raise NotImplementedError("Implement rec_parentheses before running the checks.")


if __name__ == "__main__":
    try:
        for text in ("", "([])", "([)]", "(()", "(a)"):
            print(repr(text), parentheses(text), rec_parentheses(text))
    except NotImplementedError as error:
        print(error)
