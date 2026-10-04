# AM4 Recursive Factorials starter

Goal: implement recursive_factorial(num) for a nonnegative integer, returning
an integer factorial. Include zero in the domain: zero factorial is 1.

Choose the smallest cases to return immediately. Then implement a recursive
step and trace the calls and returns for one input. Do not use math.factorial
to implement the exercise.

The existing checks use inputs 0, 1, and 5; expected results are 1, 1, and 120.
Try another small input. Explain the stopping case, how the input shrinks, and
how pending multiplications finish as the calls return.

## Start and self-check

Open this starter in the site's Python IDE and confirm the import, or download
this folder and run `python3 main.py` locally. The initial Run prints an exercise
reminder, not a completed algorithm. Replace each TODO and `NotImplementedError`;
keep the function names and parameters. Run again to inspect the provided cases.
Compare with the expectations above, add another case, and explain the result
before reviewing the separate `../solution/` reference.
