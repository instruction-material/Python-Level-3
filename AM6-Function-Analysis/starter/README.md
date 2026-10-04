# AM6 Function Analysis starter

This starter supplies the original fourteen functions f1 through f14 without
their reference complexity comments. The function bodies are the input to the
analysis task, not completed answers. Record a prediction before running code.

Use nonnegative integer n and m and short lists of integers (including negatives
and zero). Treat a primitive arithmetic/comparison operation and one print call
as one unit of work; ignore text-encoding costs in this introductory model.
For f8 through f10, n and m are independent. State best versus worst cases where
early exits matter, and check the m=0 boundary of f10 separately.

For each f1 through f14, record:
- the main counted operation;
- a raw operation-count expression or recurrence;
- a justified worst-case Big-O classification;
- any early-exit or boundary case that changes the count.

Inspect loops and recursion before measuring. Add one small function call under
the main guard (for example f1(4)) to check a prediction. Start with values no
larger than 8: nested loops can print a lot. Clock timing is optional supporting
evidence, not a proof of a complexity class. Review the separate solution
comments only after completing the classifications.

## Start and verify

Open the supplied source in the site's Python IDE and confirm the import, or
run `python3 main.py` locally. Run initially prints directions; classifications
are not generated automatically. The task above supplies the analysis record.

The `../solution/` folder is separate instructor/reference material.
