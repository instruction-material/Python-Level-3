# AM1 Juni Assistant starter

Fill run_assistant() with a command loop. Suggested numeric commands are
1 time, 2 date, 3 remember a name, 4 recall it, 5 fun fact, 6 joke, and 7 quit.
Implement at least three different responses plus a clear exit command.
The reference supports all seven and accepts quit or exit as well.

Keep a remembered name in the current session only. Use harmless example data,
not real personal information. If using random choices, select from the correct
response list. Exact command comparison is important: "12" is not command "1".

Try blank input, an unknown command, and an exit. The program should remain
responsive without indexing an empty string. Try recall before remembering,
then remember a name and recall it. Explain the loop's stopping condition.
The reference also exits cleanly if its input stream ends.

## Start and verify

Open the starter in the site's Python IDE and confirm the import, or run
`python3 main.py` locally. Initial Run prints an exercise reminder. Replace the
TODO and `NotImplementedError` statements while keeping names and parameters.
Try the checks above and explain the result before consulting the reference.

The `../solution/` folder is separate instructor/reference material.
