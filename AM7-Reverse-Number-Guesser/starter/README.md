# Reverse Number Guesser

## Purpose and role

This is the required computer-led binary-search game. A player privately chooses
an integer in an inclusive interval; the computer narrows that interval using
feedback. This differs from the optional Number Guesser, where the computer
holds a random secret and the player chooses guesses.

Work in this incomplete starter. The completed reference in solution is separate.
Initial Run only prints a reminder; no answers are imported automatically.

## Four callable tasks

1. `parse_feedback(text)`: require a string, strip surrounding whitespace and
   normalize case. Accept exactly `yes`, `above`, `below`, `quit`; return
   the normalized command. Anything else raises ValueError. Retain the original
   yes command, not an arbitrary response treated as success.
2. `midpoint(low, high)`: return the lower integer midpoint. Bounds are builtin
   integers, not Boolean, satisfying 1 <= low <= high <= 100. Invalid bounds
   raise ValueError.
3. `update_bounds(low, high, guess, feedback)`: validate those bounds and an
   integer guess in that interval. Above means the player's number is greater
   than the guess; below means smaller. Return a new (low, high) tuple that
   excludes the wrong guess and strictly shrinks the interval. Accept only
   above/below here; yes/quit belong to the game loop. Reject an empty resulting
   interval with ValueError rather than guessing from inconsistent bounds.
4. `play(low=1, high=100, max_guesses=7, input_fn=None, output_fn=None)`:
   validate configuration before prompting. max_guesses is a builtin integer
   from 1 to 7; bounds use the same domain. None callbacks use input/print at
   call time. An input callback receives a prompt and returns a string; output
   receives a message. Invalid callbacks raise ValueError.

## State and outcome contract

- Choose a midpoint from the current interval. Invalid feedback prints a retry
  message, preserves the interval and does not consume an attempt.
- An accepted yes/above/below response records that midpoint in a fresh guesses
  list and consumes one attempt. Quit, EOF or KeyboardInterrupt cancels without
  recording the interrupted guess. Do not use generic exceptions as success.
- Yes yields status `confirmed` and that number, based on the player's claim.
- If one value remains, including an initially singleton interval, stop with
  status `inferred` and explicitly say this depends on consistent prior feedback,
  not an affirmative confirmation. Do not consume another prompt/attempt.
- Feedback excluding all candidates yields `contradiction`. Reaching the limit
  while multiple candidates remain yields `exhausted`. Neither is a success.
- Return a dictionary with status, number, guesses and bounds. Number is an
  integer only for confirmed/inferred; otherwise None. Bounds is the last valid
  inclusive interval, even after a contradictory response. Each return owns a
  new guesses list. No global game state is retained.

Seven accepted midpoint responses suffice to identify every value from 1 to
100 only with consistent, truthful feedback. Arbitrary or mistaken feedback
cannot prove a secret. A smaller configured limit may genuinely exhaust.

## Independent checks and discussion

Predict a short interval trace before running it. Check every secret from 1
through 100 with scripted truthful feedback, strict interval shrinking, boundary
guesses and no more than seven accepted responses. Separately test blank/unknown
responses, mixed case, contradiction in a two-value interval, a singleton,
a deliberately insufficient limit, quit and EOF. Check statuses and messages,
not merely whether the console stopped. A course facilitator can walk one trace
through the candidate interval; independently test different values afterward.

## Run, import and retain work

Confirm opening this starter in the site's Python IDE. Read main.py and this
README before filling the TODOs. Implement and test the helpers, then replace
the reminder with a guarded play() call. Enter yes/above/below/quit through the
IDE's standard-input prompt. Imports must never prompt, print or start a game.
Locally, run `python3 main.py` from starter. Save/export the project, then reopen
the workspace. There are no extra dependencies or input files.
