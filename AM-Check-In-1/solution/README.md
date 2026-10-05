# Check-In 1 reference notes

middle_letters uses the end-exclusive middle slice; an empty or short string
therefore has no middle characters. second_word splits whitespace and validates
the stated at-least-two-word precondition before indexing.

num_pins sums rows recursively, with zero/one as base cases. Its primitive work
and stack depth grow linearly in rows. Naive lucas has one-based base values 2
and 1; repeated recursive subproblems cause exponential work. Practice with small
inputs, not unrestricted deep recursion.

strangeFunction(4) prints 4, 3, 2, 1, 2 on separate lines. Each frame prints before
making the n-1 and n-2 calls; calls at two or below stop.

A list used as a stack supports append/pop at its end. The random demonstration
changes only the newly appended top element; popping restores [1, 2, 3, 4, 5].
make_word ignores backspace on an empty stack and joins the remaining characters.
Its returned string preserves case, spaces and order. Both original makeWord
and reference make_word names are available.

Reference functions import without interaction. Direct execution of main asks
for the two inputs and shows the original stack demonstration; it does not run
the tracing answer automatically.
