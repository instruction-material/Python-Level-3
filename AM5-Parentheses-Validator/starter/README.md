# AM5 Parentheses Validator starter

Implement parentheses(brackets) with a stack, then rec_parentheses(brackets)
with recursive pair reduction. Both return a Boolean for a bracket-only string
using (), [], and {}. Empty input is balanced. Non-bracket characters are
rejected, not silently ignored.

Track which opening bracket must match the next closing bracket. Decide how
premature closers and leftover openers fail. For recursion, remove a complete
adjacent pair and make the input strictly shorter.

For "", "([])", "([)]", "(()", and "(a)", both functions should return
True, True, False, False, False. Add another nested case and a premature closer.
Explain why the two approaches must agree even though their internal work differs.

## Start and verify

Open the starter in the site's Python IDE and confirm the import, or run
`python3 main.py` locally. Initial Run prints an exercise reminder. Replace the
TODO and `NotImplementedError` statements while keeping names and parameters.
Try the checks above and explain the result before consulting the reference.

The `../solution/` folder is separate instructor/reference material.
