# AM5 Substring Generator starter

Implement get_substrings(string). A substring is contiguous: "ac" is not a
substring of "abc". Return a lexicographically sorted list of distinct
substrings, including the empty string. Empty input returns [""].

Recursively remove characters from the ends, not arbitrary interior positions.
Deduplicate the generated results and use a stable final order. Use short
inputs, at most eight characters, while tracing this branching recursion.

For "ab", expect ["", "a", "ab", "b"]. For "aba", expect
["", "a", "ab", "aba", "b", "ba"]. Test "abc" and verify "ac" is absent.
Explain how overlapping recursive branches can generate duplicates.
Memoizing repeated subproblems is an optional later extension, not a prerequisite.

## Start and verify

Open the starter in the site's Python IDE and confirm the import, or run
`python3 main.py` locally. Initial Run prints an exercise reminder. Replace the
TODO and `NotImplementedError` statements while keeping names and parameters.
Try the checks above and explain the result before consulting the reference.

The `../solution/` folder is separate instructor/reference material.
