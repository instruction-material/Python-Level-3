# Tic Tac Toe AI Test

Measure the earlier rule-based AI against a random player with reproducible batches. Reuse learner-written board/strategy helpers; add bounded automated games, counts, rates and a reproducible loss trace.

This numbered project remains required core work. The four stages have distinct purposes; reuse verified learner-written work between them rather than importing completed reference answers.

## Start and run

Open this `starter/` folder in the site IDE after its confirmation prompt, or open `main.py` locally with Python 3. Only standard-library modules are needed. Initial Run prints a reminder. Every public callable is deliberately incomplete. Read the contract, predict a small case, implement the relevant function and test it independently. Private helper organization is a learner choice.

After implementation, run `main(games=1000, seed=0)` for the original-sized reproducible experiment. Use `main(games=10, seed=0, start_player="X")` for a short initial batch. Change the final guard from its reminder to `main()` when ready.

## Board and shared contracts

Use a list of three list rows, each with three exact string cells: `" "`, `"X"` or `"O"`. Coordinates are exact integers 0, 1 or 2; Boolean values are not coordinates. Rows run top to bottom and columns left to right. Three matching marks in any row, column or diagonal win. A full board without a winner is a draw. There is no wrapping.

Helpers validate shape and cell/player domains. They intentionally do not reject mark-count imbalance: hypothetical candidate analysis can place the same mark twice. Actual games start empty, alternate accepted moves and stop immediately after a win or draw. `game_status` rejects simultaneous winners. `win` tests the eight lines; `finished` tests occupancy independently of wins. `legal_moves` returns fresh row-major `[row, col]` lists and returns an empty list for an ended game. `make_board`, `duplicate_board` and `apply_move` allocate fresh rows. Candidate evaluation and all caller-owned boards remain unchanged. `apply_move` rejects an occupied coordinate or an ended game before editing.

`rng=None` resolves Python's `random` module at call time; a supplied source needs a callable `choice(sequence)`. Random moves select uniformly from the finite list of available squares with the standard random source. A supplied source's returned move must belong to the original legal list, even if it mutates its received copy. Strategy helpers return a fresh coordinate list or `None` for an ended game. Invalid arguments raise `ValueError`; unexpected callback errors propagate.
## Basic strategy

`test_win` validates a candidate/player, returns false for occupied or ended positions, and tests a copied board. `winning_moves` returns fresh immediate winning coordinates in row-major order. `ai_player_move(board, rng=None, player="O")` uses this exact priority: first own immediate win; first opponent immediate win to block; center; first open corner in top-left, top-right, bottom-left, bottom-right order; a random remaining legal side. Default O preserves the original computer role; player X permits explicit comparisons.

An immediate win takes precedence over blocking. This heuristic is the taught strategy, not a claim of optimal play. Keep a trace of a losing position when evaluation finds one.
## Reproducible experiment

`play_game(start_player=None, rng=None, x_move_fn=None, o_move_fn=None)` starts a fresh board. Defaults are random X and basic AI O. Each strategy receives `(copied_board, rng)` and returns a two-integer list or tuple for an originally legal square. A callback may change its private copy without changing the actual game. Invalid strategy results raise ValueError. Stop at the first win/draw and return the same fresh status/winner/board/moves/start_player dictionary used for console games. At most nine moves are accepted.

`evaluate(games=1000, seed=0, start_player=None, x_move_fn=None, o_move_fn=None)` uses one fresh `random.Random(seed)` across the batch. A nonnegative exact integer game count up to 10,000 is accepted; 1,000 preserves the original experiment size, and the cap is an authored bounded-run policy. Seed is an exact integer or None; None deliberately selects a non-reproducible run. Start player is X/O or None for a separately randomized choice each game. Validate configuration before running any game.

Return `games`, `seed`, `start_player`, `x_wins`, `o_wins`, `draws`, `rates` (those three count keys mapped to count/games fractions), and `first_x_win` (the first full X-win outcome, or None). Counts sum to games. A zero-game run has zero counts and 0.0 rates, with no fabricated outcome. The first loss trace is evidence for further debugging, not a complete game archive.

`main(games=1000, seed=0, start_player=None, output_fn=None)` runs the default random-X/basic-O experiment, prints counts, percentages and the test scope, then returns that report. Imports do not run a batch, prompt or print. Repeat the same seed/order/policies for reproducibility; compare X-first and O-first batches separately. When replacing a strategy, report its name and mark explicitly. Bring learner-written strategy functions into this project's file; do not import reference answers. A callback for X can call a learner's AI with `player="X"`.

Random-opponent results measure that opponent and configuration. Many wins do not prove optimality, and absence of sampled losses does not prove that no legal opponent can win. Independent exhaustive game-tree checks are a separate form of evidence. Custom callbacks must themselves terminate; nine accepted game moves do not bound arbitrary callback work.

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
| `test_win(board, i, j, player)` | Test one vacant candidate on copied rows; ended or occupied positions are false. |
| `winning_moves(board, player)` | Return fresh row-major immediate winning coordinates for the named player. |
| `random_player_move(board, rng=None)` | Choose uniformly from legal positions; return None when the game has ended. |
| `ai_player_move(board, rng=None, player="O")` | Choose own win, opponent block, center, first corner, then random legal side. |
| `play_game(start_player=None, rng=None, x_move_fn=None, o_move_fn=None)` | Run one fresh game with copy-isolated strategies and at most nine moves. |
| `evaluate(games=1000, seed=0, start_player=None, x_move_fn=None, o_move_fn=None)` | Return seeded counts/rates and the first X win; default X is random and O basic. |
| `main(games=1000, seed=0, start_player=None, output_fn=None)` | Print default random-versus-basic results, their scope, and return the report. |

## Walkthrough sequence

1. Port and retest learner-written board and basic strategy functions; avoid console prompts in an automated game.
2. Implement one fresh alternating game; verify legal moves, terminal detection and the nine-move bound.
3. Implement a seeded batch, exact count/rate bookkeeping and the first X-win trace.
4. Repeat seed/order configurations, separate X-first and O-first results and state what the tested opponent evidence establishes.
5. Use the retained trace to identify a weak basic-AI decision before the fork stage.

## Independent self-checks

- A zero-game batch returns zero counts/rates and no loss trace.
- Two batches with identical seed, order and default policies produce identical reports. Repeated reports use fresh mutable data.
- The three counts sum to the requested game count; each retained trace replays to its reported winner without post-win moves.
- A bad strategy coordinate fails explicitly; a strategy mutating its received board copy cannot mutate the actual game.

Keep tests outside the submitted game logic. Explain the representation, a legal move, the terminal checks, one strategy decision and the evidence boundary during the presentation. No network requests or file writing are part of these projects.

## Source provenance and reference access

The original catalog places all four numbered AM14 projects in curriculum and names their UI, basic strategy, experiment and fork purposes. The original reference snapshots are retained in Git at `efd0cdfb190a9110ec1a160786e13f724a60153f`; their original public helper names and default X/O roles are preserved. Validation, quiet imports, bounded selection, reproducibility and explicit cancellation are authored corrections. Completed answers live separately in `../solution/main.py`. Inspect them after attempting the relevant task.
