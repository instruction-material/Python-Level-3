# Check-In 3 reference key

Two full left-to-right baseline bubble passes on [4, 8, 2, 1, 10, 0] give
[2, 1, 4, 0, 8, 10]. The supplied baseline repeats n full n-1 comparison sweeps.
The optimized reference shrinks the suffix and actually stops after a no-swap
pass. Ten sorted items take nine comparisons, rather than the previous reference's
45 shrinking-only comparisons. Empty/singleton inputs take no pair comparisons.
The optimized best case is linear and worst case quadratic under unit-cost
comparison. Both preserve tie order through strict swaps.

Indexed merge combines two already ascending lists in linear total work and
linear output space, keeping inputs intact and taking left ties first. Repeated
pop(0) shifts a list and can make the old merge quadratic. Balanced merge sort
has n-log-n work; this helper is not a full merge-sort implementation.

partition treats pivot as a value and preserves order in its three new groups.
For distinct keys, balanced recursive quicksort splits give n-log-n work and
repeated one-sided splits quadratic work. Three-way equal-key grouping can stop
an all-equal input after linear work, so the distinct-key assumption matters.

write_letters validates before overwriting, writes one exact character plus
newline and closes the file through a context manager. read_letter_counts removes
only delimiters and deliberately rejects malformed records rather than counting
an empty key. Character counts are case sensitive. Empty files return {}.

read() returns the whole text as one string. readlines() returns a list of lines,
retaining their line endings where present; it does not split words. For text
"a b\nc" the results are "a b\nc" and ["a b\n", "c"], respectively.
