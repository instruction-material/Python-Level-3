"""Player-led guessing of a random secret, with validated input and quiet imports."""

import random
import re


def _interval(low, high):
    if type(low) is not int or type(high) is not int or not 1 <= low <= high <= 100:
        raise ValueError("Bounds must be integers with 1 <= low <= high <= 100.")


def parse_guess(text, low=1, high=100):
    """Return an in-range signed ASCII integer, or None for quit."""
    _interval(low, high)
    if not isinstance(text, str):
        raise ValueError("A guess must be a string.")
    token = text.strip()
    if token.casefold() == "quit":
        return None
    if re.fullmatch(r"[+-]?[0-9]+", token) is None:
        raise ValueError("Enter an ASCII integer or quit.")
    try:
        guess = int(token)
    except ValueError as error:
        raise ValueError("The integer text is too long.") from error
    if not low <= guess <= high:
        raise ValueError("The guess must be in the game's interval.")
    return guess


def guess_feedback(guess, secret):
    """Return higher/lower/correct for validated integer values from 1 to 100."""
    for number in (guess, secret):
        if type(number) is not int or not 1 <= number <= 100:
            raise ValueError("Guess and secret must be integers from 1 through 100.")
    if guess < secret:
        return "higher"
    if guess > secret:
        return "lower"
    return "correct"


def play(secret=None, low=1, high=100, max_guesses=7, input_fn=None, output_fn=None):
    """Return status/secret/accepted guesses; invalid input never consumes a try."""
    _interval(low, high)
    if type(max_guesses) is not int or not 1 <= max_guesses <= 7:
        raise ValueError("max_guesses must be an integer from 1 through 7.")
    input_fn = input if input_fn is None else input_fn
    output_fn = print if output_fn is None else output_fn
    if not callable(input_fn) or not callable(output_fn):
        raise ValueError("Input and output callbacks must be callable.")
    if secret is None:
        secret = random.randint(low, high)
    if type(secret) is not int or not low <= secret <= high:
        raise ValueError("The secret must be an integer in the game's interval.")
    guesses = []

    def finish(status, message):
        output_fn(message)
        return {"status": status, "secret": secret, "guesses": guesses[:]}

    output_fn(f"Guess the secret integer from {low} through {high} in {max_guesses} tries.")
    while len(guesses) < max_guesses:
        try:
            text = input_fn(f"{max_guesses - len(guesses)} tries left (integer/quit): ")
        except (EOFError, KeyboardInterrupt):
            return finish("cancelled", "Game cancelled.")
        try:
            guess = parse_guess(text, low, high)
        except ValueError:
            output_fn(f"Invalid guess. Enter an integer from {low} through {high}, or quit.")
            continue
        if guess is None:
            return finish("cancelled", "Game cancelled.")
        guesses.append(guess)
        feedback = guess_feedback(guess, secret)
        if feedback == "correct":
            return finish("won", f"You win: {secret} was the secret.")
        output_fn("Try a higher number." if feedback == "higher" else "Try a lower number.")
    return finish("lost", f"All tries used; the secret was {secret}.")


if __name__ == "__main__":
    play()
