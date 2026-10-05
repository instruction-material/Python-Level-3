# Check-In 3: ASCII file sorting

This remains a core review project. Retain the supplied input.txt and implement
the four TODO functions in main.py using a sorting algorithm already studied.
Initial Run gives a reminder. Imports must not open files or run sorting.

1. Implement read_letters(path="input.txt") with UTF-8 text and a context manager.
   Each record contains exactly one ASCII character, excluding the CR/LF line
   delimiter. A final line may omit its newline; CRLF/LF records both work.
   A literal single space or tab is a valid character and must not be stripped.
   Empty files give []; blank, multi-character and non-ASCII records raise
   ValueError with the one-based line number. Missing/unreadable files propagate
   the normal file exception rather than creating substitute data.
2. Implement sort_letters(letters), returning a fresh list in ascending ASCII
   code order without changing the input. Retain duplicates. Use a previously
   implemented bubble, merge or quicksort, not built-in sort as the implementation.
   Input is a list of the same valid characters; invalid values raise ValueError.
3. Implement write_letters(letters, path="output.txt"). Validate the whole list
   before opening output, then write one character plus newline per record.
   Return None. A valid run deliberately overwrites output.txt; invalid values
   must leave an existing output unchanged.
4. Implement sort_file(input_path="input.txt", output_path="output.txt").
   Reject identical input/output files, including path, symlink or hardlink
   aliases, with ValueError. Read/validate the full input before writing output,
   retain the source bytes, and return the sorted list. Malformed source must
   leave any existing output unchanged.
5. After completing TODOs, call sort_file() under the direct-run guard. Run from
   starter with Python 3, or confirm importing the starter and input.txt into the
   site's Python IDE. Reopen output.txt, compare it with an independent expected
   order and save/export the project after inspection.

Explain newline handling, numeric ASCII ordering and the sorting algorithm's
work. Predict a small fixture before execution, discuss one trace with a course
facilitator, then test different data independently. Include empty input,
duplicates, spaces, uppercase/lowercase, absent final newline and rejected
malformed records. Use temporary test files so testing does not overwrite the
supplied example or existing personal files. The completed reference stays in
solution; do not copy its answer into the starter.
