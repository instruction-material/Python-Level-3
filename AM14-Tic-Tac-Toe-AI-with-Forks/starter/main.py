"""Learner Tic Tac Toe exercises. Read README.md before implementing each callable."""

import random
import re


def make_board():
    """Return a new empty 3x3 board with independently allocated rows."""
    raise NotImplementedError("Implement make_board after predicting its self-checks.")


def duplicate_board(board):
    """Validate and copy every row; no caller-owned list is reused."""
    raise NotImplementedError("Implement duplicate_board after predicting its self-checks.")


def win(board, player):
    """Check all eight winning lines for X or O without changing the board."""
    raise NotImplementedError("Implement win after predicting its self-checks.")


def finished(board):
    """Return whether all nine squares are occupied, independently of wins."""
    raise NotImplementedError("Implement finished after predicting its self-checks.")


def game_status(board):
    """Return ongoing/X_won/O_won/draw; reject simultaneous winners."""
    raise NotImplementedError("Implement game_status after predicting its self-checks.")


def legal_moves(board):
    """Return fresh row-major coordinate lists; terminal boards have no moves."""
    raise NotImplementedError("Implement legal_moves after predicting its self-checks.")


def apply_move(board, player, row, col):
    """Return a fresh board after one legal move; reject ended/occupied positions."""
    raise NotImplementedError("Implement apply_move after predicting its self-checks.")


def render_board(board):
    """Return an ASCII board with separators and a final LF; never print."""
    raise NotImplementedError("Implement render_board after predicting its self-checks.")


def print_board(board, output_fn=None):
    """Send the complete render to one call of the call-time output callback."""
    raise NotImplementedError("Implement print_board after predicting its self-checks.")


def parse_coordinate(text):
    """Return a signed ASCII coordinate 0..2, or None for case-insensitive quit."""
    raise NotImplementedError("Implement parse_coordinate after predicting its self-checks.")


def test_win(board, i, j, player):
    """Test one vacant candidate on copied rows; ended or occupied positions are false."""
    raise NotImplementedError("Implement test_win after predicting its self-checks.")


def winning_moves(board, player):
    """Return fresh row-major immediate winning coordinates for the named player."""
    raise NotImplementedError("Implement winning_moves after predicting its self-checks.")


def test_fork(board, i, j, player):
    """Test a non-winning candidate creating at least two distinct immediate threats."""
    raise NotImplementedError("Implement test_fork after predicting its self-checks.")


def fork_moves(board, player):
    """Return fresh row-major non-winning fork coordinates without mutation."""
    raise NotImplementedError("Implement fork_moves after predicting its self-checks.")


def ai_player_move(board, rng=None, player="O"):
    """Choose own win, opponent block, own fork, fork defense, center, corner, side."""
    raise NotImplementedError("Implement ai_player_move after predicting its self-checks.")


def play(start_player=None, input_fn=None, output_fn=None, rng=None):
    """Play human X versus computer O; invalid input retries, quit/EOF cancels."""
    raise NotImplementedError("Implement play after predicting its self-checks.")


def main(start_player=None, input_fn=None, output_fn=None, rng=None):
    """Run the guarded console game and return its explicit final outcome."""
    raise NotImplementedError("Implement main after predicting its self-checks.")


if __name__ == "__main__":
    print("Read README.md, implement the learner functions, then change this guard to call main().")
