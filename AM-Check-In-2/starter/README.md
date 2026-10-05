# Check-In 2: analysis, searching and elementary sorting

This core review follows selection and insertion sort. Supplied weirdFunction,
function1 and function2 are code to analyze, so their bodies stay present without
classifications. The search/sort TODOs are intentionally incomplete. Initial Run
prints a reminder and imports stay quiet.

## Time-complexity reading and predictions

1. Define Big-O and state the input size and primitive-operation model.
2. Classify the growth of these mathematical expressions for positive n:
   n^2 + 1000n; log(n) + sqrt(n); 1*2*...*n. The third question concerns the
   expression's value, not the runtime of a loop multiplying n factors.
3. Analyze supplied weirdFunction(nums): distinguish its odd-length and
   even-length paths, then describe best/worst families of inputs.
4. Analyze supplied function1(nums), including the fixed inner-loop bound.
5. Analyze supplied function2(n) for positive integer n. Trace n = 50 before
   executing. Treat a print, index, comparison and arithmetic operation as unit
   cost for this model; arbitrary-size integer bit costs are a separate question.

## Search implementations

6. Explain what searching does and when linear and binary search apply.
7. Implement linear_search(l, v), returning True or False for membership without
   mutation. Empty input returns False; position determines work.
8. Implement bin_search_iter(lst, item) and bin_search_recur(lst, item).
   Inputs are already ascending. Both return Boolean membership and leave input
   unchanged. Use indices/bounds, not slicing, copying, sorting or a preliminary
   validation scan. Those preconditions must be established before the search.
9. Implement first_one_index(numbers) for an already sorted sequence consisting
   only of zeros then ones. Return the zero-based first-one index or -1 when no
   one exists, including empty input. With constant-cost indexing, the search
   must use logarithmically many accesses. Do not scan the input to validate it.

## Sorting and pass traces

10. Describe selection sort. Predict two descending selection passes on
    [2, 5, 10, 3, 6, 1]; one pass selects the maximum of the unsorted suffix.
11. Complete selectionSort(lst), sorting largest to smallest in place and
    returning that same list. Empty/singleton inputs work. Stability is not
    promised. selection_sort is the compatible reference-name alias.
12. Describe insertion sort. Predict three ascending insertion passes on
    [3, 7, 2, 5, 10, 1]. Passes insert indices 1, 2 and 3; index zero is not
    counted as an insertion pass.
13. Complete insertionSort(lst), sorting smallest to largest in place and
    returning that same list. Move only strict out-of-order values so ties retain
    their input order. insertion_sort is the compatible reference-name alias.
14. Explain the best/worst cases of both sorts using comparison/shift counts,
    not only a measured clock time.

## Self-checks and walkthrough

Predict before running supplied examples. Use found/missing targets, every first
one position, all zeros/all ones, empty/singleton lists, duplicates and negative
values. Verify mutation and returned identity separately from sorted output.
The different sort directions are intentional; the additional two-sort timing
project instead compares two ascending implementations for fair workloads.
Compare one trace with a course facilitator, then try different data independently.
Use the separate solution README only after an attempt; it contains classifications,
correct pass traces and the explanation of why recursive slices add copying cost.
