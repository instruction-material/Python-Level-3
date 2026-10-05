"""Incomplete reverse-number game. See README.md before implementing."""


def parse_feedback(text):
    """Normalize the four documented feedback commands or raise ValueError."""
    raise NotImplementedError("Implement parse_feedback.")


def midpoint(low, high):
    """Return the lower midpoint of the validated inclusive interval."""
    raise NotImplementedError("Implement midpoint.")


def update_bounds(low, high, guess, feedback):
    """Apply valid above/below feedback without accepting an empty interval."""
    raise NotImplementedError("Implement update_bounds.")


def play(low=1, high=100, max_guesses=7, input_fn=None, output_fn=None):
    """Run the documented game and return its explicit outcome dictionary."""
    raise NotImplementedError("Implement play.")


if __name__ == "__main__":
    print("Implement the four tasks in README.md, then replace this reminder with play().")
