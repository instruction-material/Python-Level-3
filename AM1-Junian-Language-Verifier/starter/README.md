# AM1 Junian Language Verifier starter

Fill run_verifier() with a program that reads one word and tests three rules:
the length is even, there are at least two vowels from a/e/i/o/u, and the
first and last letters differ. Ignore letter case when counting vowels and
comparing letters. Do not invent additional grammar rules for this exercise.

Report valid or invalid. For invalid input, print the specific failed rule
or rules, not only a generic rejection. Handle empty input without indexing
missing characters; it fails the vowel rule.

"Lumo", "LUMO", and "ae" are valid. Test an odd-length input, a low-vowel
input, and a same-first-last input such as "Aa". Explain which condition
matches each rule. Trace the count before running, then compare with output.

## Start and verify

Open the starter in the site's Python IDE and confirm the import, or run
`python3 main.py` locally. Initial Run prints an exercise reminder. Replace the
TODO and `NotImplementedError` statements while keeping names and parameters.
Try the checks above and explain the result before consulting the reference.

The `../solution/` folder is separate instructor/reference material.
