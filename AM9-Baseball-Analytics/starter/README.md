# Baseball Analytics: keyed bubble-sort leaderboards

This core project applies the adjacent-comparison sort from AM9 to records rather
than single numbers. The ten supplied players and statistics are synthetic
practice data, not current baseball results. Preserve p1-p10 and playerList;
player_list is a compatible spelling for the same list.

## Assignment

Implement the three TODO functions in main.py. Initial Run gives a reminder;
imports must not print, sleep, request input or run a leaderboard.

1. bubble_baseball(players, stat) receives a list of four-field lists or tuples:
   name, batting average, home-run count and RBI count, in that order. Names are
   nonblank strings and remain exactly as supplied. Average is a finite int or
   float in [0, 1], excluding Boolean values. Both counts are nonnegative ints,
   also excluding Booleans. Validate every record, not only the selected field.
2. Recognize exactly the case-sensitive statistic names Average, Home Run and
   RBI. Unknown names, invalid containers, malformed records and invalid fields
   raise ValueError; identify the one-based record number for record errors.
3. Return a fresh list of names ranked from greatest to least selected statistic.
   Equal statistics retain their original input order. Empty input returns a
   fresh empty list; one player returns that name. Do not change the original
   outer list or any record. Do not remove duplicate names or tied records.
4. Adapt bubble sort using adjacent comparisons/swaps and a working outer copy.
   Do not use sorted or list.sort as the implementation. The descending,
   stable-tie and nonmutation policies clarify behavior the old snapshot did not
   guarantee; reversing an ascending list would reverse tied records too.
5. print_list(names) receives a list of strings, prints each preceded by one tab
   on its own line and returns None. Invalid input raises ValueError before any
   printing. An empty list prints nothing.
6. main() prints Average Leaderboard:, Home Run Leaderboard: and RBI Leaderboard:
   with their respective rankings and blank lines between groups. Return None
   and retain playerList unchanged. After completing the helpers, call main()
   under the direct-run guard, replacing the initial reminder.

## Work and check

Run from starter with Python 3, or confirm opening this starter in the site's
Python IDE. Predict the order of a small synthetic set with a tie, trace one
adjacent pass with a course facilitator, then test additional data independently.
Compare all three leaderboards with an independently computed expected ranking.
Check empty/singleton inputs, ties in several positions, duplicate names, unchanged
record identity, all three keys, unknown keys and every rejected field domain.
Save/export the project after checking it. The completed reference remains in
solution and is not part of the learner starter.

Explain which field each statistic selects, why equal adjacent values do not
swap, why descending reversal is not equivalent to stable descending sorting,
and how the working copy affects space. A no-swap early exit is a useful refinement;
it does not remove the quadratic worst case.
