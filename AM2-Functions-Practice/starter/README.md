# Functions Practice: learner brief

Implement the five required functions in main.py with loops and reusable return
values. This is iterative review; the later AM4 projects teach recursion.
Imports must not print or ask for input. Put demonstration calls under the
direct-run guard. Initial Run currently prints an exercise reminder.

1. product(a, b, c): return the product of three numeric inputs.
2. average(x, y): return the arithmetic mean of two numeric inputs.
3. count_letter(word, letter): count an exact, case-sensitive character in a
   string. An empty word gives zero. Reject a nonstring word or a letter that
   is not a one-character string with ValueError.
4. count_seven(number): count digit 7 in an integer's magnitude, ignoring a minus
   sign. Zero has no sevens. Reject nonintegers and bool with ValueError. Keep
   digit arithmetic exact; floating division can round a large integer.
5. exponent(a, b): use repeated multiplication for a**b. The exponent b is a
   nonnegative integer, not bool; reject other exponents with ValueError.
   An exponent of zero returns one, including the conventional 0**0 case here.

## Optional challenges

6. factorial(n): use a loop for n! with 0! = 1. Require a nonnegative integer,
   not bool, and reject unsupported input with ValueError.
7. hailstone(n, max_steps=10000): start from a positive integer. If it is even,
   halve it exactly; otherwise replace it with 3*n + 1. Stop at one. Return
   the number of terms including the starting term and final one: the chain
   from ten has seven terms. n must be a positive integer, not bool.
   max_steps caps transitions, not terms, and must be a nonnegative integer,
   not bool. Invalid domains raise ValueError. If the cap is reached before
   one, raise RuntimeError rather than hanging or returning a partial length.
   n=1 needs zero transitions and returns one. General convergence is not
   proved; bounded experiments do not establish the Hailstone conjecture.

## Self-check and walkthrough

First trace one normal case and one boundary before coding each function. Write
independent tests for zero, negative digit inputs, repeated/absent letters,
case differences and rejected domains. Trace the optional challenges separately
after the required functions work. Keep completed references in solution/main.py
separate from learner code; consult them only after an independent attempt.
No dependencies are required. Run python3 main.py from this starter directory.
