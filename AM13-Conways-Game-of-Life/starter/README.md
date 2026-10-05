# Conway's Game of Life: required simulation project

Build a file-driven cellular automaton with synchronous updates. This is a required
core capstone. The separate two-player project adds ownership and strategy after
this simulation works; it has a distinct purpose and is also required.

Open the incomplete `starter`, not the separate `solution`. Confirm the site's
**Open in Python IDE** request to import `main.py`, this README and all eight
`.in` files. Initial Run prints a reminder. Complete functions before replacing
the guarded reminder with `main()`. For local work, open a terminal in this
folder and use `python3 main.py`. Relative filenames refer to that working folder.
Reference answers stay separate; read them after an attempt when checking work.

## Rules and board

Default size is 30 rows by 60 columns. A cell is exactly `False` (dead) or
`True` (alive) in a rectangular list of lists. The board is finite and does not
wrap: ignore neighbors outside its edges. Count the eight surrounding positions,
including diagonals and excluding the cell itself.

B3/S23 means a dead cell is born with exactly three live neighbors; a live cell
survives with exactly two or three. Every other cell is dead next generation.
Compute all next cells from the same current board, never partially updated rows.

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

## Ten callable tasks

Keep the signatures in `main.py`. Private helpers are allowed.

1. `parse_coordinates(lines, height=30, width=60)`: implement the shared record
   contract above.
2. `read_coordinates(path, height=30, width=60)`: return parsed coordinates and
   close the input even on failure.
3. `make_grid(coords, height=30, width=60)`: return a fresh Boolean board with
   exactly the requested coordinates alive.
4. `count_neighbors(grid, i, j)`: return the integer live-neighbor count.
5. `neighbors(grid, alive, i, j)`: return the next Boolean state for that cell.
6. `next_generation(grid)`: return a synchronous fresh board of the same shape.
7. `render_board(grid)`: return a string using `O` for live and `-` for dead,
   no spaces or indexes, exactly one LF after every row including the last.
8. `print_board(game, output_fn=None)`: send the complete rendered string to the
   output callback once and return `None`.
9. `run(grid, generations=5, delay=0.0, output_fn=None, sleep_fn=None)`: validate
   configuration, copy the initial board, display `Generation 0\n` and its
   rendering, then display each completed update as `Generation N\n` and its
   rendering. `generations` is a nonnegative integer (not Boolean) or `None`.
   Zero displays only the initial board. `delay` is finite and nonnegative
   (integer/float, not Boolean); call the sleep callback before each update only
   when delay is nonzero. `sleep_fn=None` resolves `time.sleep` at call time.
   Return a fresh dictionary with exactly `status`, `grid`, `generations`.
   Status is `completed` at the requested limit, or `cancelled` if a
   `KeyboardInterrupt` occurs during the display/update loop. Count only
   completed updates; return the most recently computed fresh board. Other
   callback errors propagate. A still life or empty pattern still uses the
   requested update count.
10. `main(path="repeat.in", height=30, width=60, generations=5, delay=0.0,
    output_fn=None, sleep_fn=None)`: validate configuration before opening,
    read the pattern, build the board and return `run`'s outcome. No input prompts
    and no output files.

## Patterns, run selection and checkpoints

Original patterns are supplied unchanged in both roles:
`repeat.in`, `square.in`, `boat.in`, `design1.in`, `f-pentomino.in`,
`hertz-oscillator.in`, `b-heptomino-shuttle.in`, `spaceship.in`.
All fit the default size; `spaceship.in` uses column 59, so a smaller board
must be checked against its coordinates. To select a different pattern, change
the guarded call to `main(path="square.in")`; the filename is not a console prompt.

- Before coding, trace one corner, one edge and one interior cell by hand.
  Predict the result before running. Test a single cell dying, a 2-by-2 block
  remaining stable, a three-cell blinker returning after two updates and an
  all-dead board remaining dead.
- Compare a copied input before/after an update; changing one returned row must
  not change another row or the original. Check a non-default rectangular board
  to expose hardcoded next-grid dimensions.
- Default Run makes five updates without pauses. The original continuous
  simulation is explicitly available as `main(generations=None, delay=0.5)`.
  Local Ctrl-C returns a cancelled outcome; the IDE Stop button may terminate
  the worker without returning an outcome. Continuous mode need not terminate
  naturally, even when a pattern becomes stable.
- Explain why one generation can take O(height × width) time and space when each
  cell uses a private constant-size neighbor count. Public single-cell helpers
  validate the whole board, so repeatedly calling those validating helpers
  would add work. Complexity claims must describe the implementation used.
- Save/export the project ZIP, including all pattern files; reopen saved work
  and run a different pattern. No pattern or reference is auto-executed on import.

For an instructor walkthrough, use the same sequence: predict, implement one
helper, compare evidence, then integrate. The presentation should explain the
finite boundary, simultaneous update and file-to-board path with one cell trace.
