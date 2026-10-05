# Runtime Comparator

## Purpose and role

This required search experiment compares linear and iterative binary search on
the same numeric multiset and exactly the same query batch. It follows the
required Reverse Number Guesser, not a choice replacing it. This is distinct
from AM11's sorting comparison: the algorithms measured here search for values.

The starter contains five required tasks plus one explicitly optional recursive
search. Completed reference answers stay in solution. Initial Run gives a
reminder and does not run a million-item benchmark.

## Callable tasks and domains

1. `linear_search(list1, item)`: retain the original name and parameter spelling.
   Return Boolean membership without changing the list.
2. `bin_search_iter(lst, item)`: return Boolean membership on sorted input,
   including False for empty/missing cases. Use index bounds and preserve input.
   The caller prepares sorted values; no sorting or validation scan belongs
   inside either timed search.
3. `make_workload(size=2000, queries=50, seed=0)`: return a fresh (nums, targets)
   pair of lists, using a local random.Random(seed). Both contain generated
   integers from 0 through 100000, with duplicates retained. Do not change global
   random state. Size is a builtin integer in 0-5000, query count in 0-100 and
   seed is a builtin integer; Boolean is invalid. Invalid domains raise ValueError.
4. `compare_searches(nums, targets, repeats=3, clock=None)`: require lists of
   builtin integers (not Boolean), at most 5000 data items and 100 targets.
   Manually supplied negative integers are valid. Repeats is a builtin integer
   from 1-10. None selects time.perf_counter at call time; otherwise clock must
   be callable. Invalid configuration raises ValueError before timing.
5. `main(size=2000, queries=50, repeats=3, seed=0)`: create one workload, run
   the comparison, print measured rows plus Python version/implementation and
   seed, and return those rows. State what is and is not timed.

Optional: retain `bin_search_recur(lst, item)` for a separately explained
recursive comparison. The original reference uses list slices: O(log n)
comparisons do not make its total worst-case runtime logarithmic because
copying selected halves totals O(n). It is not part of the two-algorithm core
benchmark. Core completion does not require this helper.

The pure search functions assume the stated comparable numeric/sorted inputs.
Validate a workload outside those functions rather than adding linear scans
that invalidate the logarithmic search comparison.

## Comparable experiment contract

- Generate all data and queries before timing. Freeze one shared query sequence;
  do not generate fresh random targets inside either algorithm's timed region.
- Linear uses a copy in the original input order; binary uses a sorted copy of
  the same multiset. Sorting is preparation, excluded from search time.
- Compute expected membership independently before timing. Both algorithms
  must pass an untimed warm-up check before either is measured.
- Give each repeat a fresh working copy prepared before its start-clock call.
  Time only the full query loop and result collection, identically for both.
  Query-list construction, random generation, sorting, copying, oracle work,
  validation, printing and result verification stay outside the measured region.
- Verify every timed result afterward: exact Boolean answers must match the
  oracle, and working inputs must be unchanged. A mismatch raises AssertionError
  instead of reporting a successful experiment. Preserve nums and targets.
- Clock readings must be finite numeric int/float values, not Boolean, with a
  finite nonnegative elapsed time; invalid/nonmonotonic readings raise ValueError.
- Return two fresh row dictionaries in linear/binary order, each with algorithm,
  size, queries, hits, repeats, input_order and median_seconds. Hits counts
  successful queries, including repetitions, not distinct targets. Input order
  is original or sorted. The median is from measured full-batch seconds, not
  a guessed value or historical timing.

Defaults are 2000 values, 50 shared targets, three repeats and seed 0. Limits
allow deliberate small experiments without the original automatic million-item
workload. Empty data/queries are allowed and can measure loop/clock overhead;
do not mistake them for an algorithm-speed demonstration.

## Interpretation and independent checks

Predict membership independently on small lists, including negatives, duplicates,
hits, misses and empty cases. Check every result against that oracle. Verify
identical target reuse, fresh copies and exact timer boundaries with an injected
clock before relying on real timings. A course facilitator can trace one batch
and explain why preparation is excluded; independently vary sizes and targets.

Report environment, seed, workload/hit count and repeats. Original-order linear
hits may appear at different positions than in sorted input; this is a confound,
not proof that an algorithm always wins. Calling compare_searches with an already
sorted nums list can control that ordering difference. Local repeated medians
illustrate behavior, not Big-O proof or the end-to-end cost of preparing a
binary-search list. Never substitute rounded historical estimates for measurements.

## Run, import and retain work

Confirm importing the starter in the Python IDE, implement and check the five
core tasks, then replace the reminder with a guarded main() call. Reuse only
previously verified learner search code; do not import solution automatically.
Imports must not allocate workloads, draw random values, print or run timings.
Locally run `python3 main.py` from starter. Read the report, save/export and reopen
the workspace. This standard-library experiment needs no extra files/dependencies.
