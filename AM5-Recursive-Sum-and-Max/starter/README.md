# AM5 Recursive Sum and Max starter

Implement sum_recursion(values) and max_recursion(values) for short lists of
finite numbers. The empty sum is 0; the maximum of an empty list is undefined
and must raise ValueError. A one-item list returns that item. Do not mutate
the input. Use recursion, not sum() or max(), to implement the functions.

Decide the stopping cases and reduce the remaining list each time. Test [4],
[1, 2, 3], and [-8, -3, -5]. Expected sum/maximum pairs are 4/4, 6/3, -16/-3.
Check that the maximum does not incorrectly start at zero for negative inputs.
Test the empty sum separately and verify the empty maximum raises ValueError.
Compare finished results with the built-ins, and trace a smaller-list call.
List slices create copies; they are convenient here but are not cost-free.

## Start and verify

Open the starter in the site's Python IDE and confirm the import, or run
`python3 main.py` locally. Initial Run prints an exercise reminder. Replace the
TODO and `NotImplementedError` statements while keeping names and parameters.
Try the checks above and explain the result before consulting the reference.

The `../solution/` folder is separate instructor/reference material.
