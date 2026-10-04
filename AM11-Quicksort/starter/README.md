# Partition and quicksort exercise

Run `python main.py` from this folder, or confirm the site's Python IDE import.
Implement partition before recursive sorting; initial Run only gives a reminder.

`partition(lst, pivot)` takes a pivot **value**, not an index. Return three new
lists in order: less, equal, greater. Preserve input and order within each group.
A pivot not present in the list is valid and gives an empty equal group.

`quicksort(lst, rng=None)` returns a sorted **new** list and never changes the
input, including empty/singleton cases. Select a pivot from the current input,
partition, recursively sort only less/greater groups, and combine the results.
Use the optional `rng` object for repeatable tests (`random.Random(0)`), or the
`random` module when None. Preserve duplicates and equal-group order.

Optional shuffling practice: `shuffle(lst, num_swaps)` mutates by random swaps,
returns None, and treats empty/singleton input safely. Reject non-integer,
negative, and boolean swap counts with ValueError. A fixed number of random
swaps is **not** a uniform permutation. `shuffle2(lst)` removes randomly selected
items into a new list, returning that list and leaving the original empty.

Check empty/singleton, negatives, repeated pivots, sorted/reversed data, partition
membership/order, and mutation/identity contracts. Do not use built-in sorting
inside the sort; use it only as an oracle. Explain expected `O(n log n)` time,
quadratic worst-case time and deep-recursion limits for consistently bad pivots.
This allocating implementation is not an in-place quicksort: balanced partitions
have linear peak list storage plus a logarithmic call stack; worst-case retained
partitions and recursion can require quadratic storage and linear stack depth.
Keep extensions optional and reference answers separate.
