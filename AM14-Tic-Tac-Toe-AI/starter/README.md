# Tic Tac Toe AI

Upgrade learner-written UI code with a copied-board rule-based computer strategy. Keep the same game rules and console outcomes; the new work is move evaluation and priority.

This numbered project remains required core work. The four stages have distinct purposes; reuse verified learner-written work between them rather than importing completed reference answers.

## Start and run

Open this `starter/` folder in the site IDE after its confirmation prompt, or open `main.py` locally with Python 3. Only standard-library modules are needed. Initial Run prints a reminder. Every public callable is deliberately incomplete. Read the contract, predict a small case, implement the relevant function and test it independently. Private helper organization is a learner choice.

After implementation, use `main(start_player="X")` for a predictable human-first game or `main()` for a randomly selected starting player. Type `quit` at either coordinate prompt to stop. Change the final guard from its reminder to `main()` when ready.

## Board and shared contracts

Use a list of three list rows, each with three exact string cells: `" "`, `"X"` or `"O"`. Coordinates are exact integers 0, 1 or 2; Boolean values are not coordinates. Rows run top to bottom and columns left to right. Three matching marks in any row, column or diagonal win. A full board without a winner is a draw. There is no wrapping.

Helpers validate shape and cell/player domains. They intentionally do not reject mark-count imbalance: hypothetical candidate analysis can place the same mark twice. Actual games start empty, alternate accepted moves and stop immediately after a win or draw. `game_status` rejects simultaneous winners. `win` tests the eight lines; `finished` tests occupancy independently of wins. `legal_moves` returns fresh row-major `[row, col]` lists and returns an empty list for an ended game. `make_board`, `duplicate_board` and `apply_move` allocate fresh rows. Candidate evaluation and all caller-owned boards remain unchanged. `apply_move` rejects an occupied coordinate or an ended game before editing.

`rng=None` resolves Python's `random` module at call time; a supplied source needs a callable `choice(sequence)`. Random moves select uniformly from the finite list of available squares with the standard random source. A supplied source's returned move must belong to the original legal list, even if it mutates its received copy. Strategy helpers return a fresh coordinate list or `None` for an ended game. Invalid arguments raise `ValueError`; unexpected callback errors propagate.
## Console and result contract

Human X plays computer O. `start_player=None` chooses X or O with the supplied random source, preserving the original random-start purpose. Explicit `"X"` or `"O"` makes the order predictable. `input_fn=None` and `output_fn=None` resolve the current built-in input and print at call time. Validate configuration before printing or reading.

Prompt separately for row and column. `parse_coordinate` trims surrounding whitespace and accepts signed ASCII integer text whose value is 0..2, or case-insensitive `quit` (returns `None`). Empty text, decimals, Unicode digits, out-of-range values and non-text records are invalid. A malformed coordinate or occupied square retries the whole row/column pair without changing the board or advancing the turn. Quit at either prompt, EOF or an input KeyboardInterrupt returns cancellation. Unexpected input/output/strategy errors propagate; cancellation never announces a winner.

Print the initial board and each accepted move. `render_board` returns three ASCII rows with `|` dividers, `---+---+---` row separators and a final LF. `print_board` sends that string in one callback call; default print adds its ordinary newline. There are no sleeps, screen-clearing commands or files.

`play` and `main` return a fresh dictionary with `status` (`X_won`, `O_won`, `draw` or `cancelled`), `winner` (X/O only for a win, otherwise None), a fresh `board`, accepted `moves` as `(player,row,col)` tuples in order, and `start_player`. A completed game needs at most nine accepted moves; arbitrarily repeated invalid human input is not a termination guarantee.
## Basic strategy

`test_win` validates a candidate/player, returns false for occupied or ended positions, and tests a copied board. `winning_moves` returns fresh immediate winning coordinates in row-major order. `ai_player_move(board, rng=None, player="O")` uses this exact priority: first own immediate win; first opponent immediate win to block; center; first open corner in top-left, top-right, bottom-left, bottom-right order; a random remaining legal side. Default O preserves the original computer role; player X permits explicit comparisons.

An immediate win takes precedence over blocking. This heuristic is the taught strategy, not a claim of optimal play. Keep a trace of a losing position when evaluation finds one.

## Callable tasks

| Callable | Contract |
| --- | --- |
| `make_board()` | Return a new empty 3x3 board with independently allocated rows. |
| `duplicate_board(board)` | Validate and copy every row; no caller-owned list is reused. |
| `win(board, player)` | Check all eight winning lines for X or O without changing the board. |
| `finished(board)` | Return whether all nine squares are occupied, independently of wins. |
| `game_status(board)` | Return ongoing/X_won/O_won/draw; reject simultaneous winners. |
| `legal_moves(board)` | Return fresh row-major coordinate lists; terminal boards have no moves. |
| `apply_move(board, player, row, col)` | Return a fresh board after one legal move; reject ended/occupied positions. |
| `render_board(board)` | Return an ASCII board with separators and a final LF; never print. |
| `print_board(board, output_fn=None)` | Send the complete render to one call of the call-time output callback. |
| `parse_coordinate(text)` | Return a signed ASCII coordinate 0..2, or None for case-insensitive quit. |
| `test_win(board, i, j, player)` | Test one vacant candidate on copied rows; ended or occupied positions are false. |
| `winning_moves(board, player)` | Return fresh row-major immediate winning coordinates for the named player. |
| `ai_player_move(board, rng=None, player="O")` | Choose own win, opponent block, center, first corner, then random legal side. |
| `play(start_player=None, input_fn=None, output_fn=None, rng=None)` | Play human X versus computer O; invalid input retries, quit/EOF cancels. |
| `main(start_player=None, input_fn=None, output_fn=None, rng=None)` | Run the guarded console game and return its explicit final outcome. |

## Walkthrough sequence

1. Carry forward verified learner-written board and console functions; keep reference answers separate.
2. Implement test_win and winning_moves; predict the winning coordinate without changing the real board.
3. Implement the stated win/block/center/corner/side priority, including a position offering both an own win and an opponent threat.
4. Test both marks and starting orders, then record a remaining weak position for the evaluation stage.

## Independent self-checks

- Own X at (0,0),(0,1) completes (0,2); occupied candidates are false.
- On an empty board, the basic AI takes the center. With center occupied and no threat, the first available original-order corner is chosen.
- Both marks take their own immediate win before an opponent block; evaluating candidates does not mutate any input row.

Keep tests outside the submitted game logic. Explain the representation, a legal move, the terminal checks, one strategy decision and the evidence boundary during the presentation. No network requests or file writing are part of these projects.

## Source provenance and reference access

The original catalog places all four numbered AM14 projects in curriculum and names their UI, basic strategy, experiment and fork purposes. The original reference snapshots are retained in Git at `efd0cdfb190a9110ec1a160786e13f724a60153f`; their original public helper names and default X/O roles are preserved. Validation, quiet imports, bounded selection, reproducibility and explicit cancellation are authored corrections. Completed answers live separately in `../solution/main.py`. Inspect them after attempting the relevant task.
