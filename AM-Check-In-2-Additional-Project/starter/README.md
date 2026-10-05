# Check-In 2: two-sort timing experiment

This remains a core review project. Compare selection and insertion after
implementing them, before AM11 adds bubble, merge and quicksort to a larger
comparison. Both sorts here are ascending; this is intentionally different from
Check-In 2's descending selection trace.

1. Implement selection_sort2(lst) and insertion_sort2(lst). Both modify a list
   in place and return the same list object. Empty/singleton lists work; use
   independent sorted results only as test oracles.
2. Implement make_workloads(n, seed=0). Use a local seeded random generator for n
   integer values from 1 through max(1, 10*n), then derive fresh ascending and
   descending copies. Return random, sorted and reversed shape lists containing
   the same multiset. Preparation is outside measured sorting time.
3. Implement time_sort(sorter, values): compute the oracle and copy values before
   starting time.perf_counter; time only the sorting call. Stop the clock before
   validating the returned ascending list. Incorrect output raises AssertionError;
   the original values stay unchanged. Return finite nonnegative measured seconds.
4. Implement benchmark(sizes=(100, 300), repeats=3, seed=0, sorters=None). Each
   algorithm/repetition receives a fresh copy of the same shape, never the
   preceding algorithm's sorted working list. Return one row per size, shape and
   algorithm, with algorithm, shape, n, repeats and seconds (the measured median).
   Default sorters are selection and insertion; an optional mapping supports one
   or two named callable implementations.
5. Print a small labeled timing table under the direct-run guard, not during
   import. Do not round short runs to zero and then claim equal performance.
   Generation, copying, oracle computation, validation and printing are excluded.
6. Explain how observed shape/size differences relate to algorithm work. A timing
   table is measured evidence on this machine, not a proof of Big-O or a promise
   that one implementation always wins. Predict a result before measuring, then
   discuss one trace and try an independently selected small input.

Bounds: one to five sizes, each integer 0-2000; repeats is integer 1-10; bool is
not an integer parameter here. seed is an integer, not bool. Invalid bounds raise
ValueError. Use the small defaults first; large explicit experiments may exceed
a browser execution budget and can instead run locally with Python 3. No timing
runs happen on import. Initial starter Run prints a reminder until TODOs are
implemented. Keep the completed reference separate from the attempt.
