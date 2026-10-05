# Check-In 3: advanced sorting and file input/output

This core review follows quicksort and file I/O. Preserve predictions before
running demonstrations. The supplied bubbleSort body is a correct unoptimized
baseline to trace and improve, not the optimized reference answer. Initial Run
prints a reminder; imports do not read/write files or request input.

## Sorting explanations, traces and coding

1. Explain adjacent comparisons, the sorted suffix and bubble-sort passes.
2. Predict two passes on [4, 8, 2, 1, 10, 0] using the supplied baseline. One pass
   is a complete left-to-right sweep; check the prediction only afterward.
3. Implement bubble_sort(lst) using a shrinking suffix and a per-pass swap flag
   that stops after a no-swap pass. Sort ascending in place and return the same
   list. Empty/singleton inputs work; strict comparisons preserve ties.
4. Explain best/worst work and count actual comparisons on sorted input, not only
   final output or timing. Compare the baseline and the optimized implementation.
5. Explain merge sort and why each input to merge must already be ascending.
6. Implement merge(listA, listB): use indices to return a fresh stable merged list
   without changing either input. Empty/unequal inputs and duplicates work. Take
   the left item on a tie. Avoid pop(0), which shifts Python lists and invalidates
   the linear-merge cost model. Complete TODOs before calling them.
7. Explain quicksort, its pivot and recursion-depth-sensitive work.
8. Implement partition(lst, pivot): pivot is a value, not an index. Return three
   fresh lists for less/equal/greater, preserving order within each, with the
   original unchanged. Empty input and a pivot absent from input both work.
9. Discuss balanced and unbalanced splits under a stated distinct-key model;
   duplicates belong in the equal group, not a non-progressing recursive call.

## File workflow

10. Implement write_letters(word, path="file.txt"), returning None. word is a
    string without CR/LF; empty input is allowed. Validate before opening output.
    Write each Unicode character followed by one newline using UTF-8 and a
    context manager. The explicit output file is overwritten on valid input.
11. Implement read_letter_counts(path="file.txt"): remove only record newlines,
    not meaningful spaces. Each record must have exactly one character; a blank
    or longer line raises ValueError identifying its one-based line number.
    Count literal, case-sensitive characters, including space or punctuation.
    Empty files give an empty dictionary. Missing/unreadable files raise the
    normal file exception; do not silently return invented data.
12. Complete main: ask for a word, write its characters, read the file back and
    print the counts. Call main only after replacing the direct-run reminder.
13. Explain read() versus readlines(), including trailing newlines and a last
    line without one. Test both with a small file; neither automatically splits
    text into words.

## Self-checks and walkthrough

Use empty, sorted, reversed, duplicate and uneven inputs. Verify sort mutation,
stable labels and fresh merge/partition identity separately. For files, use a
temporary test folder and independent expected character counts; malformed input
must not be silently trimmed into a valid record. Predict first, walk through one
trace with a course facilitator, then test different data independently.
Run with Python 3 from starter, or confirm importing it into the site's Python
IDE. Reopen generated file.txt in the project; save/export after inspection.
Keep the separate reference and its answer key outside the attempted starter.
