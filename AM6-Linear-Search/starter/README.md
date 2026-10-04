# AM6 Linear Search starter

Goal: implement linear_search(values, target). Return True if the target occurs
in the list and False otherwise. The list need not be sorted. Return a Boolean,
not an index, and do not change the input list.

Scan one item at a time and distinguish an early match from finishing the scan.
Do not use in, index(), or count() to perform the search.

The checks cover an empty list, a beginning match, an end match, and a missing
target; expected results are False, True, True, False. Also test a middle match,
an unsorted list, and repeated values. Explain which input needs the fewest
comparisons and which needs the most.

## Start and self-check

Open this starter in the site's Python IDE and confirm the import, or download
this folder and run `python3 main.py` locally. The initial Run prints an exercise
reminder, not a completed algorithm. Replace each TODO and `NotImplementedError`;
keep the function names and parameters. Run again to inspect the provided cases.
Compare with the expectations above, add another case, and explain the result
before reviewing the separate `../solution/` reference.
