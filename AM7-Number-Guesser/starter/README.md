# Number Guesser

## Purpose and role

This optional player-led game retains the original random secret in 1-100 and
at most seven accepted guesses. The player chooses numbers; the computer says
higher/lower. It is not a duplicate of the required Reverse Number Guesser,
where the computer chooses midpoints from feedback. Arbitrary guesses are not
guaranteed to win; a deliberate binary strategy can establish the seven-try bound.

Keep completed answers in solution separate from this incomplete starter.
Initial Run prints a reminder, not a hidden game implementation.

## Three callable tasks

1. `parse_guess(text, low=1, high=100)`: require a string and valid bounds
   (builtin integers, not Boolean, with 1 <= low <= high <= 100). Strip surrounding
   whitespace. Case-insensitive quit returns None. Otherwise accept an optional
   + or - sign followed by ASCII decimal digits only, then require the integer
   to lie in the interval. Blank input, decimals, underscores, internal spaces,
   non-ASCII digits, out-of-range values and non-string input raise ValueError.
   A number string exceeding Python's integer-conversion limit also raises
   ValueError; it is not an accepted guess.
2. `guess_feedback(guess, secret)`: both values are builtin integers from 1
   through 100, excluding Boolean. Return higher when the guess is below the
   secret, lower when above it, and correct when equal. Invalid domains raise
   ValueError. Higher/lower tell the player how to change a guess.
3. `play(secret=None, low=1, high=100, max_guesses=7, input_fn=None, output_fn=None)`:
   validate bounds, a builtin integer limit from 1 through 7, and callbacks
   before starting. If secret is None, select it with random.randint(low, high)
   at call time, never on import. An injected secret must be a builtin integer
   in the configured interval and allows repeatable independent tests.

None callbacks use input/print at call time. An input callback receives a prompt
and returns text; output receives one message. Non-callable callbacks or invalid
configuration raise ValueError before input is requested.

## Attempts and outcomes

Invalid text/range input prints a retry message without consuming a try.
Each accepted integer, including a repeated wrong guess, consumes one try.
Quit, EOF or KeyboardInterrupt cancels without counting the interrupted input.
Keep prompts distinct from actual accepted guesses.

Return a fresh dictionary with status, secret and guesses. Status is won on
an exact accepted guess, lost after the limit of wrong guesses, or cancelled.
Guesses is a fresh list containing only accepted integers. The returned secret
supports tests/replay; do not reveal it on the console until a win or loss.
Cancellation must not print a win or disclose the secret. No game history is
shared across calls. Seven arbitrary guesses may lose, including seven repeats.

## Independent checks and discussion

Use injected secrets instead of relying on luck. Predict feedback on below,
above and exact guesses. Test every secret from 1-100 with a scripted binary
strategy, then test arbitrary repeated misses, a win on the last permitted
attempt, invalid text/range input, mixed-case quit, EOF and invalid configuration.
Check attempts and returned status, not only console output. Discuss the
difference between a strategy guarantee and the game's seven-try allowance with
a course facilitator; afterward test different secrets independently.

## Run, import and retain work

Confirm opening the starter in the Python IDE, read this README and fill the
three TODOs. After helper checks, replace the reminder with a guarded play()
call and use the IDE's standard-input prompt. Imports must not draw a random
secret, prompt, print or start a game. Locally run `python3 main.py` from starter.
Save/export the project and reopen the workspace. No input files or external
dependencies are needed.
