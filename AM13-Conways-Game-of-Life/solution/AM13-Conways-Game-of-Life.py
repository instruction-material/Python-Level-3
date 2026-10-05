"""Compatibility entry point. The canonical reference is sibling main.py."""

from pathlib import Path
from runpy import run_path

_reference = run_path(str(Path(__file__).with_name("main.py")), run_name="conway_reference")
_PUBLIC_NAMES = ["GRID_HEIGHT","GRID_WIDTH","parse_coordinates","read_coordinates","make_grid","count_neighbors","neighbors","next_generation","render_board","print_board","run","main"]
globals().update({name: _reference[name] for name in _PUBLIC_NAMES})

if __name__ == "__main__":
    main()
