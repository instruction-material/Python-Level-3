"""Computer-led interval guessing; imports never start a game."""


def _interval(low, high):
    if type(low) is not int or type(high) is not int or not 1 <= low <= high <= 100:
        raise ValueError("Bounds must be integers with 1 <= low <= high <= 100.")


def parse_feedback(text):
    """Normalize exactly yes/above/below/quit; reject any other response."""
    if not isinstance(text, str):
        raise ValueError("Feedback must be a string.")
    response = text.strip().casefold()
    if response not in ("yes", "above", "below", "quit"):
        raise ValueError("Use yes, above, below or quit.")
    return response


def midpoint(low, high):
    """Return the lower integer midpoint of a valid inclusive interval."""
    _interval(low, high)
    return (low + high) // 2


def update_bounds(low, high, guess, feedback):
    """Return a strictly smaller interval for above/below, or raise ValueError."""
    _interval(low, high)
    if type(guess) is not int or not low <= guess <= high:
        raise ValueError("The guess must be an integer in the current interval.")
    response = parse_feedback(feedback)
    if response == "above":
        next_low, next_high = guess + 1, high
    elif response == "below":
        next_low, next_high = low, guess - 1
    else:
        raise ValueError("Only above/below update the interval.")
    if next_low > next_high:
        raise ValueError("Feedback leaves no possible number.")
    return next_low, next_high


def play(low=1, high=100, max_guesses=7, input_fn=None, output_fn=None):
    """Return a confirmed/inferred/contradiction/exhausted/cancelled outcome."""
    _interval(low, high)
    if type(max_guesses) is not int or not 1 <= max_guesses <= 7:
        raise ValueError("max_guesses must be an integer from 1 through 7.")
    input_fn = input if input_fn is None else input_fn
    output_fn = print if output_fn is None else output_fn
    if not callable(input_fn) or not callable(output_fn):
        raise ValueError("Input and output callbacks must be callable.")
    guesses = []

    def finish(status, number, message):
        output_fn(message)
        return {
            "status": status,
            "number": number,
            "guesses": guesses[:],
            "bounds": (low, high),
        }

    output_fn(
        f"Think of an integer from {low} through {high}. "
        "above/below describe your number relative to the computer's guess."
    )
    while True:
        if low == high:
            return finish(
                "inferred", low,
                f"Only {low} remains if previous feedback is consistent; "
                "this is inferred, not confirmed.",
            )
        if len(guesses) == max_guesses:
            return finish("exhausted", None, "Guess limit reached; no number confirmed.")
        guess = midpoint(low, high)
        try:
            text = input_fn(
                f"Guess {len(guesses) + 1}/{max_guesses}: {guess}? "
                "(yes/above/below/quit) "
            )
        except (EOFError, KeyboardInterrupt):
            return finish("cancelled", None, "Game cancelled.")
        try:
            feedback = parse_feedback(text)
        except ValueError:
            output_fn("Invalid feedback. Use yes, above, below or quit.")
            continue
        if feedback == "quit":
            return finish("cancelled", None, "Game cancelled.")
        guesses.append(guess)
        if feedback == "yes":
            return finish("confirmed", guess, f"Confirmed by feedback: {guess}.")
        try:
            low, high = update_bounds(low, high, guess, feedback)
        except ValueError:
            return finish(
                "contradiction", None,
                "Feedback contradicts the current interval; no number confirmed.",
            )


if __name__ == "__main__":
    play()
