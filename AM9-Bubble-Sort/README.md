# AM9 Bubble Sort

Canonical source repository: `Python-Level-3`

Project goal: implement bubble sort, compare the basic and improved versions, and explain why the improved version can stop early when a list is already sorted.

## Structure

- `starter/` contains the implementation requirements.
- `solution/` contains a reference implementation with an in-place sort, an early-exit sort, and a copy-returning helper.

## Completion Checks

- Sorts a list containing positive numbers, repeated values, and values that start out of order.
- Preserves the original list when using the copy-returning helper.
- Explains the nested-loop structure and the reason the inner loop can shrink after each pass.
- Explains why the early-exit version is faster on an already sorted or nearly sorted list.
