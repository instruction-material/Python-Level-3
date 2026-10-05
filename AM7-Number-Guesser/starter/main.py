"""Incomplete player-led game. Completed reference code stays separate."""


def parse_guess(text, low=1, high=100):
    """Validate integer text and range, returning None only for quit."""
    raise NotImplementedError("Implement parse_guess.")


def guess_feedback(guess, secret):
    """Return higher, lower or correct for the documented integer inputs."""
    raise NotImplementedError("Implement guess_feedback.")


def play(secret=None, low=1, high=100, max_guesses=7, input_fn=None, output_fn=None):
    """Run the validated game with random or injected secret and explicit outcome."""
    raise NotImplementedError("Implement play.")


if __name__ == "__main__":
    print("Implement the three tasks in README.md, then replace this reminder with play().")
