# Two-Player Conway's Game of Life: required ownership project

Extend the required single-player simulation with owned cells, legal paired edits
and alternating turns. Both Conway projects are core. Reuse learner-written grid
and parsing ideas, but keep this independently runnable pack separate: it teaches
ownership and turn/state reasoning rather than duplicating an animation.

Confirm **Open in Python IDE** to import the incomplete `main.py`, this README,
`player1.in` and `player2.in`. Initial Run prints a reminder. Complete functions
before replacing the guarded reminder with `main()`. Locally run
`python3 main.py` from this folder. Reference answers stay separate.

## Rules, ownership and turn order

The default board has 10 rows and 10 columns. Cells are exactly integers:
`0` dead, `1` Player O, `2` Player X (Booleans rejected). Eight neighbors,
finite boundaries and synchronous B3/S23 are the same as the first project.
A surviving cell retains its current owner even if opposing neighbors are the
majority. A dead cell born from exactly three neighbors belongs to their majority
owner. No birth occurs at any other count.

O starts, then X, alternating after each accepted turn, independent of cell
counts. A legal turn grows a cell at a dead position and kills one opponent
cell. Validate both choices before changing anything. Apply the pair first,
check extinction, then run one synchronous generation if both players remain.
Check extinction again. Do not run a generation before O's first edit.

Initial files have five cells each, not squares. Reject overlap between the two
initial patterns. A full board has no legal grow: automatically pass that turn,
advance one generation and alternate. This explicit full-board policy completes
an otherwise unspecified edge case. A pass counts as a turn.

## Input and validation contract

- Dimensions are positive integers; Booleans are not integers for this contract.
  Coordinates are zero-based `(row, column)` pairs of integers, within the board.
  Coordinate collections are lists of two-item tuples or lists.
- `parse_coordinates` accepts a list of string records. Each nonblank physical
  record contains exactly two signed ASCII decimal integers separated by
  whitespace. Surrounding whitespace and one terminal LF, CR or CRLF are allowed;
  embedded/new repeated record delimiters, extra fields, decimals, Unicode digits
  and out-of-range indexes raise `ValueError`. Blank records are skipped.
  Return a fresh list of tuples in input order, preserving duplicates.
- `read_coordinates` opens the supplied path in UTF-8 read mode using `with`,
  then parses physical records. Missing files and ordinary file/decoding errors
  propagate. It never writes input. A final record need not end in a newline.
- Validate a complete coordinate collection before constructing a board.
  Duplicate coordinates for one pattern are idempotent. Rows must be separately
  allocated. Inputs remain unchanged and returned boards have fresh rows.
- Every board operation rejects an empty/ragged/non-list board or wrong cell
  types with `ValueError`. An empty pattern means an all-dead positive-size board,
  not `[]`. Addressed cells must be in bounds. `neighbors(..., alive, ...)`
  additionally checks that `alive` has the exact required type and matches that
  current cell. Validate before invoking output callbacks.
- Optional callbacks resolve at call time: `output_fn=None` uses
  `sys.stdout.write`; output callbacks accept one string. Noncallable configured
  callbacks raise `ValueError`. There are no prompts, sleeps or file reads on
  import. Helpers return fresh data and never write files.

## Fourteen callable tasks

Keep `main.py` signatures; private helpers are allowed.

1. `parse_coordinates(lines, height=10, width=10)` and
2. `read_coordinates(path, height=10, width=10)`: implement the shared contract.
3. `make_grid(player1_coords, player2_coords, height=10, width=10)`: validate
   both lists and their nonoverlap, then return a fresh owned board.
4. `neighbor_counts(grid, i, j)`: return a fresh tuple `(O_count, X_count)`.
5. `neighbors(grid, alive, i, j)`: return integer next ownership, following
   survival retention and three-neighbor birth majority.
6. `next_generation(grid)`: return a fresh synchronous board of the same shape.
7. `count_board(grid)`: return a fresh list `[O_count, X_count]`.
8. `render_board(grid)`: return zero-based column indexes in a header and row
   indexes before each row, using `O`, `X`, `-`. Right-align row indexes to
   the digits in height minus one, and columns/symbols to the digits in width
   minus one, with one separating space and no trailing spaces. Finish every
   line with LF. For `[[1, 0], [0, 2]]`, return
   `"  0 1\n0 O -\n1 - X\n"`.
9. `print_board(game, output_fn=None)`: send the complete rendering once and
   return `None`.
10. `parse_move(text, height=10, width=10)`: return one tuple from exactly one
    coordinate record. Blank or non-string input raises `ValueError`.
11. `apply_turn(grid, player, grow, kill)`: player must be exactly integer 1
    or 2. Grow must select dead; kill must select opponent. Reject invalid pairs
    with `ValueError` without mutation. Return a fresh edited board.
12. `board_status(grid)`: return `ongoing` if both have cells, `o_wins` if
    only O, `x_wins` if only X, `draw` if neither. Check actual counts.
13. `play(grid, max_turns=50, input_fn=None, output_fn=None)`: validate
    configuration; copy/display the initial board and both counts; check initial
    extinction before prompting. `max_turns` is a nonnegative integer, not
    Boolean, or `None`. Zero returns the initial terminal result or `limit`.
    `input_fn=None` resolves built-in `input` at call time; callbacks accept
    the prompt string. For each non-full-board turn ask grow, then kill. Accept
    surrounding-whitespace/case-insensitive `quit` at either prompt as
    cancellation, and treat input EOF or KeyboardInterrupt as cancellation.
    Invalid records or illegal pairs report `Invalid turn` and retry the same
    player with no edit and no turn consumed. If either coordinate record is
    invalid, begin a new pair. Report both counts after edits and each generation.
    Follow the phase order above and stop on initial, post-edit or post-generation
    extinction. Never announce a winner on cancellation or turn limit.
    Return a fresh dictionary with exactly `status`, `grid`, `turns`,
    `next_player`. Status is one of the four board states, `cancelled`, or
    `limit`; a returned outcome never has `ongoing`. Turns counts accepted
    edit pairs/passes only; next_player is 1 initially and toggles after each.
    Output errors and unexpected input callback errors propagate.
14. `main(player1_path="player1.in", player2_path="player2.in", height=10,
    width=10, max_turns=50, input_fn=None, output_fn=None)`: validate
    configuration before opening either input, read both patterns, build and
    return `play`'s result. No output files or import-time activity.

## Workflow and self-checks

- Read the indexed board before entering `row column`, for example `0 0`.
  Do not enter Python tuple syntax. With the supplied patterns, O can grow at
  `0 0` and kill X at `4 8`. Predict the edited board and generation before
  running; those moves are an input example, not a strategy recommendation.
- Before editing the loop, trace surviving ownership under an opposing majority,
  majority births, a corner and simultaneous extinction. Test invalid grow,
  own-cell kill, out-of-range coordinates, cancellation at each prompt and an
  invalid pair followed by a valid pair. The invalid attempt must change nothing.
- Check an initial terminal board, post-edit last-opponent removal,
  post-generation wins/draw and a full-board automatic pass. Counts do not select
  the next player. Keep original inputs and intermediate generations distinct.
- Default Run caps accepted turns at 50; invalid attempts do not use this cap
  and repeated invalid input may still need cancellation. Select the original
  continue-until-terminal game explicitly with `main(max_turns=None)`.
  Cycles need not end naturally. Use `quit` or local Ctrl-C during input;
  IDE Stop may terminate the worker without a returned outcome.
- To use different patterns, change the guarded filename arguments. All original
  bytes stay unchanged. Save/export both `.in` files with the project ZIP,
  reopen saved work and repeat a short game. Import never runs the game.
- Walk through the same predict/implement/check sequence alone or with a course
  facilitator. Present a complete turn trace, explaining why edits precede the
  generation and why a survivor keeps its owner. O(height × width) generation
  work assumes constant-size private neighbor checks after one validation pass.
