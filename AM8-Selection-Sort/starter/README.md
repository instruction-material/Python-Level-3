# Selection sort exercise

Run `python main.py` from this starter folder, or confirm the site's Python IDE
import and use Run. Initial Run prints an implementation reminder; functions
remain TODOs. Work in the starter, not the separate solution.

Implement `selection_sort1(lst)` first: repeatedly select the minimum remaining
value, remove it, and append it to a result. Return a **new** sorted list and leave
the input **empty**. This consuming contract is intentional, not a sorted-copy
contract. Then implement `selection_sort2(lst)`: choose each minimum from the
current unsorted suffix, swap it into position, and return the **same** list.

Use numbers and preserve every duplicate. Do not call `sorted()` or `list.sort()`
inside either implementation; they are useful as independent test oracles.
Check `[]`, `[7]`, `[2, 1]`, negative values, duplicates, and sorted/reversed data.
Keep a copy of each original so the consuming function does not erase the oracle
input. Check identity and final input state as well as value equality.

Trace the sorted prefix or shrinking input after each pass. Explain quadratic
time for both versions, linear result space for version 1, and constant auxiliary
space for version 2. In-place swapping is not a stable ordering for tied records.
