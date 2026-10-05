# Alternating file records into a dictionary

This core file-reading project builds a dictionary from ordered key/value records.
Keep the original input.txt beside main.py. This task reads and inspects data;
it does not require writing an output file. The reference remains in solution.

## Assignment

Implement the three TODO functions. Initial Run gives a reminder; imports must
not open coursework files, print data or request input.

1. parse_pairs(lines) receives a list of strings, one string per physical record,
   optionally ending in one LF, CRLF or CR delimiter. A string containing another
   CR/LF after removing that delimiter is invalid. Non-list input and non-string
   records raise ValueError. Return a fresh dictionary without changing lines.
2. Interpret records 1/2 as the first key/value, 3/4 as the second, and so on.
   Strip surrounding whitespace from both keys and values, intentionally matching
   the original parser. Interior spaces remain; values stay strings, not numbers.
   A blank key is invalid. An empty value is valid. Later duplicate keys replace
   earlier values. An empty record list returns a fresh empty dictionary.
3. Reject an odd record count with ValueError identifying the one-based final
   line that has a key but no following value. Reject blank keys or embedded
   record delimiters with their one-based line numbers. Do not silently discard
   blank lines: their position determines whether they are keys or values.
4. load_pairs(path="input.txt") reads UTF-8 with a context manager, obtains the
   records using readlines and passes them to the parser. Accept LF/CRLF files
   and a final record without a newline. A terminating newline does not create
   another empty record; a genuine empty value needs its own physical blank line.
   Propagate normal missing/unreadable-file and decoding errors; do not create
   substitute data or change the input bytes.
5. main(path="input.txt") loads, prints and returns the dictionary. After
   completing the helpers, call main() under the direct-run guard in place of
   the reminder. Run from starter with Python 3, or confirm importing main.py
   and input.txt into the site's Python IDE.

## Work and check

Predict a small four-record fixture before running it. Walk through the record
indexes with a course facilitator, then test separate temporary files independently.
Inspect the original ten pairs, including the whitespace on technology and tool.
Check empty input, a missing final newline, CRLF/LF, odd counts, blank keys, blank
values, duplicate keys and a missing file. Compare with an independently written
expected dictionary, not with a copy of the reference algorithm.

Explain why line position matters, why stripping differs from removing only the
newline, and how duplicate-key assignment changes a value without adding another
key. Save/export the workspace after inspection. Use temporary synthetic files
for malformed cases so the original example and personal files remain unchanged.
