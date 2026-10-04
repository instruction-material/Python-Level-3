# AM7 Binary Search starter

Goal: implement bin_search_iter(lst, item) and bin_search_recur(lst, item).
The input list is already sorted in ascending order. Both return a Boolean
membership result, not an index, and leave the input unchanged. Repeated values
are allowed. Unsorted inputs are outside this exercise's contract.

Compare the target with the middle of the remaining interval. Decide which
interval can still contain it. The loop may track low/high indexes; recursion
may use slices or index bounds. Ensure each unsuccessful step makes the interval
strictly smaller, and decide how an empty interval stops the search.
Do not use in, index(), or a library search to implement the algorithms.

The checks cover an empty list, a one-item match, an end match, and a missing
target; both approaches should return False, True, True, False. Also test
first/middle matches, values outside the range, and duplicates. Explain why
sorting is required. With slices, distinguish logarithmic comparison counts
from the extra work and storage needed to copy the slices.

## Start and self-check

Open this starter in the site's Python IDE and confirm the import, or download
this folder and run `python3 main.py` locally. The initial Run prints an exercise
reminder, not a completed algorithm. Replace each TODO and `NotImplementedError`;
keep the function names and parameters. Run again to inspect the provided cases.
Compare with the expectations above, add another case, and explain the result
before reviewing the separate `../solution/` reference.
