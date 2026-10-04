# AM5 Recursive Palindrome Checker starter

Implement is_palindrome(text), returning True or False. This exercise compares
the literal text: case, spaces, and punctuation are significant. Empty and
one-character strings are palindromes; no preprocessing is required.

Choose the stopping cases, compare the ends, and reduce to the middle when
appropriate. For "", "a", "abba", and "abc", expect True, True, True, False.
Also compare "Aa" with "aa" to check the case-sensitive contract.
Trace a short input and explain why every recursive call gets smaller.
Do not implement the checker with text[::-1]; reversal is a self-check only.

## Start and verify

Open the starter in the site's Python IDE and confirm the import, or run
`python3 main.py` locally. Initial Run prints an exercise reminder. Replace the
TODO and `NotImplementedError` statements while keeping names and parameters.
Try the checks above and explain the result before consulting the reference.

The `../solution/` folder is separate instructor/reference material.
