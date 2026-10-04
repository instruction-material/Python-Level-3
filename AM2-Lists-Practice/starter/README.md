# Lists Practice: learner brief

Implement these nine tasks in main.py. Generate lists with loops, not manually
typed answers. During this review, implement sums and min/max with loops rather
than the built-in sum/min/max helpers; those helpers can serve as test oracles.
Imports must be quiet; keep test calls under the direct-run guard.

1. make_numbers(): return a fresh list of integers 1 through 20.
2. make_evens(): return a fresh list of the first twenty positive even numbers,
   from 2 through 40. Zero is not included.
3. make_squares(): return a fresh list of the first ten positive perfect squares,
   from 1 through 100. This is different from AM3's square-printing task.
4. sum_lists(l1, l2): return the numeric sum of both lists. Empty lists contribute
   zero; this does not concatenate the lists.
5. minimum(l): return the minimum value in a nonempty numeric list. Raise
   ValueError for an empty list.
6. maximum(l): return the maximum value with the same nonempty-list rule.
7. sum_list_of_lists(l): return the numeric sum of all inner lists. Empty outer
   or inner lists contribute zero.
8. flatten_list(l): return a fresh, one-level flattening in outer/inner order.
   Keep duplicates and skip empty inner lists. Empty outer input returns [].
9. max_list(l): use maximum to return each nonempty inner list's maximum, in
   order. Preserve the reference's deliberate policy of skipping empty inner
   lists; empty outer/all-empty input returns [].

None of these functions changes its input lists. Fresh-list functions must return
a different object even for an empty result.

## Self-check and walkthrough

Check generated list lengths and endpoints independently. Test negative values,
duplicates, one-item inputs, empty sums, rejected empty min/max, and mixed empty
and nonempty nested lists. Trace the accumulator and flattening order with an
instructor, then run tests on different data. Keep solution/main.py separate;
attempt the tasks before checking references. Initial Run prints a reminder.
No dependencies are required. Run python3 main.py from this starter directory.
