# AM4 Binary Converter starter

Goal: implement to_binary_iterative(number) and to_binary_recursive(number).
Both accept a nonnegative integer and return the same string of binary digits,
without a 0b prefix. Zero must return "0". This is supplemental AM4 practice.

Review binary place value. In the loop version, track remainders and their digit
order. In the recursive version, choose a stopping case and a smaller input.
Use integer arithmetic: / produces a float and can lose information for large
integers, whereas // preserves an integer quotient. Do not implement either
function with bin() or binary formatting.

The checks use 0, 1, 6, and 2**60 + 7. The first three results should be
"0", "1", and "110"; compare the large case with bin(value)[2:] after finishing.
Check other inputs and require both approaches to agree. Explain why remainders
need a particular order and why zero is special.

## Start and self-check

Open this starter in the site's Python IDE and confirm the import, or download
this folder and run `python3 main.py` locally. The initial Run prints an exercise
reminder, not a completed algorithm. Replace each TODO and `NotImplementedError`;
keep the function names and parameters. Run again to inspect the provided cases.
Compare with the expectations above, add another case, and explain the result
before reviewing the separate `../solution/` reference.
