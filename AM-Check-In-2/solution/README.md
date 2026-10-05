# Check-In 2 reference key

For the primitive-operation model, the mathematical expression growths are
Theta(n^2), Theta(sqrt(n)) and Theta(n!), respectively. Computing the factorial
with a single loop takes n unit-cost multiplications, not n! operations. Real
arbitrary-size integer multiplication has bit costs excluded from this model.

weirdFunction has constant work on odd lengths and linear work on positive even
lengths. Its best/worst input families therefore differ by parity; empty input
takes constant overhead. function1 makes three prints per element: linear work.
function2 repeatedly halves a positive integer until at most two, giving
logarithmic depth and one print per frame.

Linear search is constant in the best found-at-front case and linear for missing
or last targets. Bounds-only binary searches use logarithmically many indexed
comparisons; the iterative variant has constant auxiliary space, recursive
bounds logarithmic stack depth. Sorted input is a precondition, not a free
validation step. The previous slicing recursion copied a geometric series of
sublist lengths: linear total copying, not logarithmic total Python runtime.

Two descending selection passes on [2, 5, 10, 3, 6, 1] give
[10, 6, 2, 3, 5, 1]. The old ascending trace was inconsistent with the task.
Selection retains quadratic comparison work even for sorted input and makes
no stability promise.

Three ascending insertion passes (indices 1, 2, 3) on [3, 7, 2, 5, 10, 1] give
[2, 3, 5, 7, 10, 1]. Sorted input needs linear comparisons; reverse input
quadratic shifts/comparisons. Strict comparisons preserve tie order.

first_one_index uses the boundary between zeros and ones, retaining a half-open
search interval. Empty/all-zero input returns -1; all-one input starts at zero.
It deliberately does not scan the sequence for domain validation.
