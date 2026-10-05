"""Compatibility entry point. The canonical reference is sibling main.py."""

from pathlib import Path
from runpy import run_path

_reference = run_path(str(Path(__file__).with_name("main.py")), run_name="conway_reference")
_PUBLIC_NAMES = ["parse_coordinates","read_coordinates","make_grid","neighbor_counts","neighbors","next_generation","count_board","render_board","print_board","parse_move","apply_turn","board_status","play","main"]
globals().update({name: _reference[name] for name in _PUBLIC_NAMES})

if __name__ == "__main__":
    main()
