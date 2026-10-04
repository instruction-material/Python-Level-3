# AM4 Fibonacci Numbers starter

Goal: implement fibonacci(n) recursively for a positive integer position.
This project numbers the sequence from 1: position 1 is 0, position 2 is 1,
and each later value is the sum of the previous two. Return an integer.
This is a position, not a zero-based index.

Choose the two stopping cases, then combine calls at earlier positions.
Trace a small call before increasing the input: this simple recursive version
repeats work, so large positions are not useful starter tests.

The existing checks use positions 1, 2, 5, and 8; expected values are 0, 1, 3,
and 13. Write out the early sequence to check another small position.
Describe a call tree and identify a subproblem computed more than once.
An iterative comparison is an extension, not a replacement for recursion.

## Start and self-check

Open this starter in the site's Python IDE and confirm the import, or download
this folder and run `python3 main.py` locally. The initial Run prints an exercise
reminder, not a completed algorithm. Replace each TODO and `NotImplementedError`;
keep the function names and parameters. Run again to inspect the provided cases.
Compare with the expectations above, add another case, and explain the result
before reviewing the separate `../solution/` reference.
