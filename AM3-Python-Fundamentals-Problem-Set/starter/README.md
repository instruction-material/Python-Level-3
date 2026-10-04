# Fundamentals Problem Set: learner brief

Implement all sixteen numbered tasks in main.py. Each task is independently
testable. Numeric-list inputs contain numbers; tasks about parity, products,
zero-sum pairs and modes use integers. Integer N parameters reject bool and
unsupported values with ValueError. Imports are quiet; demonstrations belong
under the direct-run guard. Only task 16 mutates its input list.

1. double(numbers): return a new list with every number doubled, in input order.
2. starts_with_a(words): return words starting with lowercase a, in input order.
   Empty strings do not match; uppercase A does not match.
3. num_of_evens(numbers): count even integers, including zero and negative evens.
4. sum_of_numbers(numbers): return the numeric sum; empty input returns zero.
5. index_of_largest_number(numbers): return the zero-based index of the largest
   number. Require a nonempty list of distinct numbers; otherwise raise ValueError.
6. all_squares(N): for a nonnegative integer N, print all nonnegative perfect
   squares <= N, including zero, one per line in increasing order. Return None.
7. largest_power_of_two(N): for a positive integer N, return the greatest integer
   x such that 2**x <= N. N=1 returns zero; N<=0 is unsupported.
8. factorial_sum(N): for a nonnegative integer N, return 1! + 2! + ... + N!.
   N=0 returns the empty sum, zero.
9. largest_divisor(N): for a positive integer N, return the largest positive
   divisor strictly smaller than N. N=1 has no such divisor and returns None.
10. largest_product(numbers): return the largest product of entries at two
    distinct positions. Equal values at different positions are allowed.
    Require at least two integers; otherwise raise ValueError.
11. sums_to_zero(numbers): return True if two distinct positions sum to zero.
    Empty/singleton input returns False; [0] is False while [0, 0] is True.
12. most_common_numbers(numbers): return a new list of all tied modes in
    ascending numeric order. [3, 6, 2, 2, 6] returns [2, 6]; empty input returns [].
13. reverse_string(str): return the reverse, preserving whitespace/punctuation.
14. count_vowels(str): count ASCII a/e/i/o/u in either case; do not count y.
15. count_pairs(numbers): count distinct values appearing exactly twice, not the
    number of their occurrences. A value appearing three times is not counted.
16. swap_min_max(numbers): swap the smallest and largest values in place and
    return that same list object. Require a nonempty list of distinct numbers;
    otherwise raise ValueError. A one-item list is unchanged.

Tasks 1, 2 and 12 return fresh lists, including empty results. All other list
tasks preserve their inputs except task 16.

## Self-check and walkthrough

For every task, first trace a normal example and an allowed boundary or rejected
domain. Write an independent assertion without calling the staff reference.
Check duplicate frequencies, negative products, two-distinct-position rules,
case policies, empty input and input identity. Review the trace with an instructor,
then test different data independently. Built-in helpers may be test oracles;
do not hard-code expected input lists into implementations. Keep references
separate in solution/main.py. Initial Run prints a reminder, not answers.
No dependencies are required. Run python3 main.py from this starter directory.
