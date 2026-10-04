# AM4 Recursive Exponents starter

Goal: implement exponent(base, power). The base is an integer and the power is
a nonnegative integer; return the resulting integer. This exercise uses the
programming convention that any base to power zero returns 1, including zero.

Choose a stopping case for the exponent. Design each later call to reduce the
power toward that case. Do not use ** or pow() to implement the function.

The existing checks use (2, 0), (2, 3), (5, 2), and (-2, 3); expected results
are 1, 8, 25, and -8. Compare extra small cases with base ** power after finishing.
Explain why the base stays fixed while the exponent changes.

## Start and self-check

Open this starter in the site's Python IDE and confirm the import, or download
this folder and run `python3 main.py` locally. The initial Run prints an exercise
reminder, not a completed algorithm. Replace each TODO and `NotImplementedError`;
keep the function names and parameters. Run again to inspect the provided cases.
Compare with the expectations above, add another case, and explain the result
before reviewing the separate `../solution/` reference.
