# Check-In 1: strings, recursion and stacks

This core review follows AM5. Attempt the questions and traces independently,
then walk through one trace with a course facilitator and test different inputs.
The supplied strangeFunction body is the problem to analyze, not an answer key.
Initial Run prints a reminder; implement the TODO functions before calling them.
Imports must not print, request input or run demonstrations.

## Functions and console workflow

1. Implement middle_letters(word), then ask for a word and print its middle
   characters without the first and last. Empty, one-character and two-character
   words return an empty string. The argument is a string.
2. Implement second_word(sentence), then ask for a sentence and print the second
   whitespace-delimited word. Multiple spaces and tabs separate words. Fewer
   than two words, or a nonstring input, raises ValueError.
3. Explain recursion, a base case and progress toward that base case.
4. Implement recursive num_pins(rows): rows is a nonnegative integer, not bool.
   Row sizes are 1, 2, ... through rows; zero rows needs zero pins. Unsupported
   domains raise ValueError. Trace the smaller problem and addition.
5. Implement recursive lucas(n), using one-based positions. The sequence begins
   2, 1, 3, 4, 7, 11; each later term adds the previous two. n is a positive
   integer, not bool; zero/negative/noninteger values raise ValueError.
6. Predict the exact output of the supplied strangeFunction(4) before running
   it. Record every call and print in order, then compare with actual output.
7. Explain last-in, first-out behavior. In main, create nums with 1 through 5,
   append a random integer from 1 through 10, print the stack, pop its top and
   print again. The remaining five values must be unchanged.
8. Implement make_word(keystrokes): # is backspace; all other characters,
   including whitespace, are literal. Backspace on an empty stack does nothing.
   Preserve case and character order. The original makeWord name is an alias.
   Check the four original examples: hi# -> h, ok## -> empty, ti#ger -> tger,
   and t### -> empty.
9. Complete main using the two input/output tasks and stack demonstration. Put
   its call under the direct-run guard only after replacing the initial reminder.
   Existing num_pins, lucas and make_word names remain; strange_function aliases
   the original strangeFunction tracing input.

Practice recursion with small inputs, such as rows 0-100 and n 1-20. The naive
Lucas recurrence repeats work exponentially; large calls are not a performance
benchmark and can exhaust Python's recursion limit. This review does not promise
unbounded recursion or unrestricted runtime.

## Self-checks

Use independent expected values for empty/short words, extra whitespace, missing
second words, pin row totals, the initial Lucas terms, leading/repeated backspace
and literal characters. Prediction notes precede execution. Functions return
values; main owns interaction. Keep tests under a direct-run guard and consult
the separate solution only after the attempt. Run from the starter folder with
Python 3, or confirm importing the starter into the site's Python IDE.
