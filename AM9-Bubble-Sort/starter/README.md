# Bubble sort exercise

Run `python main.py` from this folder or confirm its import into the site's Python
IDE. The initial reminder does not run a completed algorithm.

Implement `bubble_sort_in_place(values)` with adjacent comparisons and a shrinking
unsorted range; return the same list. Implement `bubble_sort_improved(values)`
with a swap flag reset for each pass; stop after a pass with no swaps. Implement
`bubble_sort_copy(values)` on a new shallow copy; preserve the original, even when
empty or a singleton. Swap only strictly out-of-order neighbors to retain ties.

Check empty, singleton, duplicate, negative, sorted, and reversed inputs against
an independent built-in-sort oracle. Check identity/mutation too. Trace one pass
and explain why the sorted suffix no longer needs comparison. Count comparisons
on already sorted input to verify the early exit, not just output equality.
Basic bubble sort remains quadratic even on sorted input; the improved variant
has a linear best case and quadratic worst case. In-place variants use constant
auxiliary space; copying uses linear extra space. Keep answers in the starter,
separate from the solution reference.
