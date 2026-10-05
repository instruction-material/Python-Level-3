"""Owned B3/S23 reference: alternate legal edit pairs, then synchronous generations."""

import re
import sys


def _dimensions(height, width):
    if type(height) is not int or type(width) is not int or height < 1 or width < 1:
        raise ValueError("height and width must be positive integers")


def _point(point, height, width):
    if not isinstance(point, (list, tuple)) or len(point) != 2:
        raise ValueError("coordinates must be two-item lists or tuples")
    row, col = point
    if type(row) is not int or type(col) is not int or not (0 <= row < height and 0 <= col < width):
        raise ValueError("coordinates must be integer indexes inside the board")
    return row, col


def _coordinates(coords, height, width):
    if not isinstance(coords, list):
        raise ValueError("coordinates must be a list")
    return [_point(point, height, width) for point in coords]


def _reporter(output_fn):
    report = sys.stdout.write if output_fn is None else output_fn
    if not callable(report):
        raise ValueError("output_fn must be callable or None")
    return report

def parse_coordinates(lines, height=10, width=10):
    """Parse physical coordinate records, preserving order and duplicates."""
    _dimensions(height, width)
    if not isinstance(lines, list):
        raise ValueError("lines must be a list of strings")
    coords = []
    for number, line in enumerate(lines, 1):
        if not isinstance(line, str):
            raise ValueError(f"line {number}: record must be a string")
        text = line.removesuffix("\n").removesuffix("\r")
        if "\r" in text or "\n" in text:
            raise ValueError(f"line {number}: embedded record delimiter")
        fields = text.split()
        if not fields:
            continue
        if len(fields) != 2 or any(re.fullmatch(r"[+-]?[0-9]+", field) is None for field in fields):
            raise ValueError(f"line {number}: expected two ASCII decimal integers")
        try:
            coords.append(_point(tuple(map(int, fields)), height, width))
        except ValueError as error:
            raise ValueError(f"line {number}: invalid or out-of-range coordinates") from error
    return coords


def read_coordinates(path, height=10, width=10):
    """Read UTF-8 coordinates with a context manager; preserve file bytes."""
    _dimensions(height, width)
    with open(path, "r", encoding="utf-8") as source:
        return parse_coordinates(source.readlines(), height, width)


def _grid_shape(grid):
    if not isinstance(grid, list) or not grid or not isinstance(grid[0], list) or not grid[0]:
        raise ValueError("grid must be a nonempty rectangular list of lists")
    width = len(grid[0])
    if any(not isinstance(row, list) or len(row) != width or
           any(type(cell) is not int or cell not in (0, 1, 2) for cell in row) for row in grid):
        raise ValueError("grid must be rectangular and contain integer states 0, 1, 2")
    return len(grid), width


def _neighbor_counts(grid, row, col):
    counts = [0, 0]
    for r in range(max(0, row - 1), min(len(grid), row + 2)):
        for c in range(max(0, col - 1), min(len(grid[0]), col + 2)):
            if (r, c) != (row, col) and grid[r][c]:
                counts[grid[r][c] - 1] += 1
    return tuple(counts)


def _next_cell(grid, row, col):
    owner = grid[row][col]
    o_count, x_count = _neighbor_counts(grid, row, col)
    live = o_count + x_count
    if owner:
        return owner if live in (2, 3) else 0
    if live == 3:
        return 1 if o_count > x_count else 2
    return 0


def make_grid(player1_coords, player2_coords, height=10, width=10):
    """Build a fresh owned grid; reject overlaps before assigning any cells."""
    _dimensions(height, width)
    first = _coordinates(player1_coords, height, width)
    second = _coordinates(player2_coords, height, width)
    if set(first) & set(second):
        raise ValueError("initial player coordinates must not overlap")
    grid = [[0] * width for _ in range(height)]
    for owner, points in ((1, first), (2, second)):
        for row, col in points:
            grid[row][col] = owner
    return grid


def neighbor_counts(grid, i, j):
    """Return fresh (O, X) counts for the eight finite-board neighbors."""
    height, width = _grid_shape(grid)
    _point((i, j), height, width)
    return _neighbor_counts(grid, i, j)


def neighbors(grid, alive, i, j):
    """Preserve surviving owners and assign births by three-neighbor majority."""
    height, width = _grid_shape(grid)
    _point((i, j), height, width)
    if type(alive) is not int or alive != grid[i][j]:
        raise ValueError("alive must match the integer cell at (i, j)")
    return _next_cell(grid, i, j)


def next_generation(grid):
    """Return a synchronous fresh owned grid with independently allocated rows."""
    height, width = _grid_shape(grid)
    return [[_next_cell(grid, row, col) for col in range(width)] for row in range(height)]


def count_board(grid):
    """Return a fresh [O, X] list, preserving the original main reference shape."""
    _grid_shape(grid)
    return [sum(cell == owner for row in grid for cell in row) for owner in (1, 2)]


def render_board(grid):
    """Return aligned zero-based row/column indexes, O/X/- symbols and LF rows."""
    height, width = _grid_shape(grid)
    row_width, cell_width = len(str(height - 1)), len(str(width - 1))
    lines = [" " * (row_width + 1) + " ".join(str(c).rjust(cell_width) for c in range(width))]
    for index, row in enumerate(grid):
        symbols = ["-" if cell == 0 else "O" if cell == 1 else "X" for cell in row]
        lines.append(str(index).rjust(row_width) + " " + " ".join(s.rjust(cell_width) for s in symbols))
    return "\n".join(lines) + "\n"


def print_board(game, output_fn=None):
    """Send the complete rendered board once to a call-time output callback."""
    text = render_board(game)
    _reporter(output_fn)(text)


def parse_move(text, height=10, width=10):
    """Parse one row/column answer; blank and non-string answers are invalid."""
    points = parse_coordinates([text], height, width)
    if len(points) != 1:
        raise ValueError("move must contain exactly one coordinate pair")
    return points[0]


def apply_turn(grid, player, grow, kill):
    """Validate both moves before copying: grow dead, kill opponent, change no input."""
    height, width = _grid_shape(grid)
    if type(player) is not int or player not in (1, 2):
        raise ValueError("player must be integer 1 or 2")
    grow_row, grow_col = _point(grow, height, width)
    kill_row, kill_col = _point(kill, height, width)
    if grid[grow_row][grow_col] != 0:
        raise ValueError("grow must select a dead cell")
    if grid[kill_row][kill_col] != 3 - player:
        raise ValueError("kill must select an opponent cell")
    result = [row.copy() for row in grid]
    result[grow_row][grow_col] = player
    result[kill_row][kill_col] = 0
    return result


def board_status(grid):
    """Distinguish ongoing, O win, X win and simultaneous extinction."""
    o_count, x_count = count_board(grid)
    if o_count and x_count:
        return "ongoing"
    if o_count:
        return "o_wins"
    if x_count:
        return "x_wins"
    return "draw"


def _play_settings(max_turns, input_fn, output_fn):
    if max_turns is not None and (type(max_turns) is not int or max_turns < 0):
        raise ValueError("max_turns must be a nonnegative integer or None")
    read = input if input_fn is None else input_fn
    if not callable(read):
        raise ValueError("input_fn must be callable or None")
    return read, _reporter(output_fn)


def _show(grid, report):
    print_board(grid, report)
    o_count, x_count = count_board(grid)
    report(f"Player O has {o_count} cells alive\nPlayer X has {x_count} cells alive\n")


def _choose_turn(grid, player, read):
    symbol = "O" if player == 1 else "X"
    height, width = len(grid), len(grid[0])
    try:
        grow_text = read(f"Player {symbol}: grow row column, or quit: ")
    except (EOFError, KeyboardInterrupt):
        return "cancelled", None
    if isinstance(grow_text, str) and grow_text.strip().lower() == "quit":
        return "cancelled", None
    try:
        grow = parse_move(grow_text, height, width)
    except ValueError as error:
        return "invalid", str(error)
    try:
        kill_text = read(f"Player {symbol}: kill opponent row column, or quit: ")
    except (EOFError, KeyboardInterrupt):
        return "cancelled", None
    if isinstance(kill_text, str) and kill_text.strip().lower() == "quit":
        return "cancelled", None
    try:
        return "accepted", apply_turn(grid, player, grow, parse_move(kill_text, height, width))
    except ValueError as error:
        return "invalid", str(error)


def play(grid, max_turns=50, input_fn=None, output_fn=None):
    """O starts; accepted edit/pass, extinction check, generation, check, alternate."""
    _grid_shape(grid)
    read, report = _play_settings(max_turns, input_fn, output_fn)
    current, turns, player = [row.copy() for row in grid], 0, 1
    _show(current, report)
    status = board_status(current)
    while status == "ongoing" and (max_turns is None or turns < max_turns):
        symbol = "O" if player == 1 else "X"
        if any(cell == 0 for row in current for cell in row):
            choice, updated = _choose_turn(current, player, read)
            if choice == "cancelled":
                status = "cancelled"
                break
            if choice == "invalid":
                report(f"Invalid turn; board and player unchanged: {updated}\n")
                continue
            current = updated
            report(f"After Player {symbol}'s edits\n")
            _show(current, report)
        else:
            report(f"Player {symbol} passes: no dead cell is available to grow.\n")
        turns += 1
        player = 3 - player
        status = board_status(current)
        if status == "ongoing":
            current = next_generation(current)
            report(f"After generation {turns}\n")
            _show(current, report)
            status = board_status(current)
    if status == "ongoing":
        status = "limit"
    messages = {
        "o_wins": "Player O wins; Player X has no cells.\n",
        "x_wins": "Player X wins; Player O has no cells.\n",
        "draw": "Both players have no cells; draw.\n",
        "cancelled": "Cancelled; no winner is declared.\n",
        "limit": "Turn limit reached; no winner is declared.\n",
    }
    report(messages[status])
    return {"status": status, "grid": current, "turns": turns, "next_player": player}


def main(player1_path="player1.in", player2_path="player2.in", height=10, width=10,
         max_turns=50, input_fn=None, output_fn=None):
    """Validate configuration and both input patterns before starting a fresh game."""
    _dimensions(height, width)
    _play_settings(max_turns, input_fn, output_fn)
    grid = make_grid(read_coordinates(player1_path, height, width),
                     read_coordinates(player2_path, height, width), height, width)
    return play(grid, max_turns, input_fn, output_fn)


if __name__ == "__main__":
    main()
