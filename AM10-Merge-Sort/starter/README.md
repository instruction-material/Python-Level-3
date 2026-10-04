# Merge and merge sort exercise

Run `python main.py` from the starter folder or confirm its Python IDE import.
Initial Run gives a reminder; implement the four separate TODOs in order.

1. `merge(list_a, list_b)`: inputs must already be sorted. Track an index into
   each input, append the next smaller item, and append leftovers. Return a new
   list and preserve both inputs. Take the left-hand item on ties for stability.
2. `split(lst)`: recursively split at the midpoint and print singleton leaves
   from left to right. Empty input prints `[]`; this trace helper returns None
   and is not the sorting function.
3. `merge_sort(lst)`: recursively sort both halves, then call `merge`. Empty
   and singleton cases must also return a new list, not the input object.
4. `merge_sort2(lst)`: optional practice integrating the merge logic directly
   into the recursive sort, with the same value/identity/stability contract.

Use indexed merging, not repeated `pop(0)`, which shifts a Python list and
breaks the linear-merge cost model. Do not use built-in sorting in implementations.
Test empty inputs on either side, unequal lengths, odd lengths, negative values,
duplicates, and sorted/reversed lists. Check preserved inputs and new-list identity.
For a stability check, compare records by one numeric key and verify tied record
labels retain order. Explain linear merge work, logarithmic recursion depth,
`O(n log n)` sort time, and linear peak auxiliary storage (including slices and
output). Keep reference code separate from the learner's implementation.
