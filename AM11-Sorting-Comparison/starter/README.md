# Sorting comparison challenge

Run `python main.py` from this folder or confirm its Python IDE import. Initial
Run gives a reminder. Bring the already tested AM8-AM11 algorithms into the TODO
functions, then implement the experiment. Keep the solution reference separate.

The local experiment compares numeric lists, not arbitrary incomparable objects.
Selection, insertion and basic bubble sort return the same mutated list; merge
sort and quicksort return a new sorted list. `partition` takes a pivot value.
Copy the original before **every** algorithm and repeat so an in-place sorter
never changes another algorithm's workload. Label basic versus optimized variants.

Implement the experiment contracts:

- `make_workloads(size, rng)`: require an integer size from 0 to 2000 (not bool).
  Generate shared random data, derive sorted/reversed copies, and add a
  duplicate-heavy list of that length. Return a dictionary with keys
  `random`, `sorted`, `reversed`, `duplicates`. Use `random.Random(seed)`.
- `time_sort(sorter, values)`: prepare an independent `sorted(values)` oracle
  and working copy **before** starting `time.perf_counter()`. Time only the
  sorting call. Stop timing, then compare the result with the oracle; raise
  AssertionError for incorrect output and never report its speed.
- `benchmark(sizes=(100, 300), repeats=3, seed=0, algorithms=None)`: require
  one to five sizes, each an integer from 0 to 2000, and integer repeats 1 to 10;
  reject bool as an integer. Use the five sorters by default, or a supplied
  name-to-function dictionary for small tests. Return one row per size/shape/sort
  with keys `size`, `shape`, `algorithm`, `repeats`, `median_seconds`.
  Report the median of measured repeat timings; do not insert historical guesses.

Generation, copies, oracle sorting, validation and printing are **outside** the
timed region. Do not use `pop(0)` in merge sort because it shifts list elements.
Verify tiny and duplicate-heavy cases before measuring. Use the same seed and
record interpreter, hardware, input shape, size, repeats, and algorithm variant.
The supplied reference defaults to small bounded experiments; do not remove the
bounds for an unattended run. Label any omitted experiment as skipped, not measured.
Small timings vary with machine/load and do not prove asymptotic complexity.
Pair measured evidence with a separate operation-count explanation.
