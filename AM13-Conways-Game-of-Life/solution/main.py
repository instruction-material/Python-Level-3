"""Finite-boundary B3/S23 reference. Continuous execution requires explicit selection."""

import math
import re
import sys
import time

GRID_HEIGHT = 30
GRID_WIDTH = 60

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

def parse_coordinates(lines, height=30, width=60):
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


def read_coordinates(path, height=30, width=60):
    """Read UTF-8 coordinates with a context manager; preserve file bytes."""
    _dimensions(height, width)
    with open(path, "r", encoding="utf-8") as source:
        return parse_coordinates(source.readlines(), height, width)


def _grid_shape(grid):
    if not isinstance(grid, list) or not grid or not isinstance(grid[0], list) or not grid[0]:
        raise ValueError("grid must be a nonempty rectangular list of lists")
    width = len(grid[0])
    if any(not isinstance(row, list) or len(row) != width or
           any(type(cell) is not bool for cell in row) for row in grid):
        raise ValueError("grid must be rectangular and contain only Boolean cells")
    return len(grid), width


def _neighbor_count(grid, row, col):
    return sum(
        grid[r][c]
        for r in range(max(0, row - 1), min(len(grid), row + 2))
        for c in range(max(0, col - 1), min(len(grid[0]), col + 2))
        if (r, c) != (row, col)
    )


def _next_cell(grid, row, col):
    count = _neighbor_count(grid, row, col)
    return count == 3 or (grid[row][col] and count == 2)


def make_grid(coords, height=30, width=60):
    """Build a fresh Boolean grid after validating all coordinates."""
    _dimensions(height, width)
    points = _coordinates(coords, height, width)
    grid = [[False] * width for _ in range(height)]
    for row, col in points:
        grid[row][col] = True
    return grid


def count_neighbors(grid, i, j):
    """Count eight in-bounds neighbors; exclude the cell and never wrap."""
    height, width = _grid_shape(grid)
    _point((i, j), height, width)
    return _neighbor_count(grid, i, j)


def neighbors(grid, alive, i, j):
    """Return the next cell state; alive must equal the addressed current cell."""
    height, width = _grid_shape(grid)
    _point((i, j), height, width)
    if type(alive) is not bool or alive != grid[i][j]:
        raise ValueError("alive must match the Boolean cell at (i, j)")
    return _next_cell(grid, i, j)


def next_generation(grid):
    """Return a synchronous fresh grid with independently allocated rows."""
    height, width = _grid_shape(grid)
    return [[_next_cell(grid, row, col) for col in range(width)] for row in range(height)]


def render_board(grid):
    """Return O/- rows, no spaces or indexes, and one LF per row."""
    _grid_shape(grid)
    return "".join("".join("O" if cell else "-" for cell in row) + "\n" for row in grid)


def print_board(game, output_fn=None):
    """Send the complete rendered board once to a call-time output callback."""
    text = render_board(game)
    _reporter(output_fn)(text)


def _run_settings(generations, delay, output_fn, sleep_fn):
    if generations is not None and (type(generations) is not int or generations < 0):
        raise ValueError("generations must be a nonnegative integer or None")
    try:
        valid_delay = type(delay) in (int, float) and math.isfinite(delay) and delay >= 0
    except OverflowError:
        valid_delay = False
    if not valid_delay:
        raise ValueError("delay must be a finite nonnegative number")
    sleep = time.sleep if sleep_fn is None else sleep_fn
    if not callable(sleep):
        raise ValueError("sleep_fn must be callable or None")
    return _reporter(output_fn), sleep


def run(grid, generations=5, delay=0.0, output_fn=None, sleep_fn=None):
    """Display generation zero and updates; None explicitly selects continuous mode."""
    _grid_shape(grid)
    report, sleep = _run_settings(generations, delay, output_fn, sleep_fn)
    current, updates = [row.copy() for row in grid], 0
    try:
        report("Generation 0\n")
        print_board(current, report)
        while generations is None or updates < generations:
            if delay:
                sleep(delay)
            current = next_generation(current)
            updates += 1
            report(f"Generation {updates}\n")
            print_board(current, report)
    except KeyboardInterrupt:
        status = "cancelled"
    else:
        status = "completed"
    return {"status": status, "grid": current, "generations": updates}


def main(path="repeat.in", height=30, width=60, generations=5, delay=0.0,
         output_fn=None, sleep_fn=None):
    """Validate configuration, read the pattern, build a grid and run."""
    _dimensions(height, width)
    _run_settings(generations, delay, output_fn, sleep_fn)
    return run(make_grid(read_coordinates(path, height, width), height, width),
               generations, delay, output_fn, sleep_fn)


if __name__ == "__main__":
    main()
