# Insertion sort exercise

Run `python main.py` locally from this folder, or confirm the site's Python IDE
import and use Run. Initial Run is a reminder; implement the TODOs in the starter.

Implement `insertion_sort1(lst)` by inserting each next item into a new sorted
result; leave the original unchanged. Implement `insertion_sort2(lst)` by moving
the next item left through the sorted prefix of the original; return the same
list. Move an item past another only when it is strictly smaller, so equal-valued
items retain their relative order (stability).

Do not use built-in sorting in the algorithms. Use it only as a test oracle.
Check empty/singleton, sorted, reversed, negative, and duplicate-heavy inputs.
Check both result values and list identity/mutation, including the singleton
new-list case. Trace the growing sorted prefix, noting when backward movement
stops. Explain linear best-case comparisons and quadratic reversed-input work;
the new-list version uses linear extra space, the in-place version constant
auxiliary space. The separate solution is reference material, not starter code.
