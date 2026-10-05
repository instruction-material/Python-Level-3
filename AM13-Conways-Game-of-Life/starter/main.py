"""Learner scaffold. Complete README.md before selecting a simulation run."""

GRID_HEIGHT = 30
GRID_WIDTH = 60


def parse_coordinates(lines, height=30, width=60):
    """Parse physical coordinate records into a fresh list of integer pairs."""
    raise NotImplementedError("Implement parse_coordinates from README.md")


def read_coordinates(path, height=30, width=60):
    """Read UTF-8 coordinates and close the source with a context manager."""
    raise NotImplementedError("Implement read_coordinates from README.md")


def make_grid(coords, height=30, width=60):
    """Validate all coordinates and construct a fresh Boolean grid."""
    raise NotImplementedError("Implement make_grid from README.md")


def count_neighbors(grid, i, j):
    """Count the eight in-bounds neighbors, excluding the addressed cell."""
    raise NotImplementedError("Implement count_neighbors from README.md")


def neighbors(grid, alive, i, j):
    """Return the addressed cell's next B3/S23 state."""
    raise NotImplementedError("Implement neighbors from README.md")


def next_generation(grid):
    """Produce a fresh synchronous generation without changing the input."""
    raise NotImplementedError("Implement next_generation from README.md")


def render_board(grid):
    """Return O/- rows with exactly one LF per row."""
    raise NotImplementedError("Implement render_board from README.md")


def print_board(game, output_fn=None):
    """Send the complete rendering once; return None."""
    raise NotImplementedError("Implement print_board from README.md")


def run(grid, generations=5, delay=0.0, output_fn=None, sleep_fn=None):
    """Display generation zero and updates; return status, grid, generations."""
    raise NotImplementedError("Implement run from README.md")


def main(path="repeat.in", height=30, width=60, generations=5, delay=0.0,
         output_fn=None, sleep_fn=None):
    """Validate configuration, read coordinates, build the board and run."""
    raise NotImplementedError("Implement main from README.md")


if __name__ == "__main__":
    print("Implement the ten tasks in README.md; then select a bounded or continuous run.")
