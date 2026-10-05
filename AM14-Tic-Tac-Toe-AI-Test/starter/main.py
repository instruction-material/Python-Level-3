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


def test_win(board, i, j, player):
    """Test one vacant candidate on copied rows; ended or occupied positions are false."""
    raise NotImplementedError("Implement test_win after predicting its self-checks.")


def winning_moves(board, player):
    """Return fresh row-major immediate winning coordinates for the named player."""
    raise NotImplementedError("Implement winning_moves after predicting its self-checks.")


def random_player_move(board, rng=None):
    """Choose uniformly from legal positions; return None when the game has ended."""
    raise NotImplementedError("Implement random_player_move after predicting its self-checks.")


def ai_player_move(board, rng=None, player="O"):
    """Choose own win, opponent block, center, first corner, then random legal side."""
    raise NotImplementedError("Implement ai_player_move after predicting its self-checks.")


def play_game(start_player=None, rng=None, x_move_fn=None, o_move_fn=None):
    """Run one fresh game with copy-isolated strategies and at most nine moves."""
    raise NotImplementedError("Implement play_game after predicting its self-checks.")


def evaluate(games=1000, seed=0, start_player=None, x_move_fn=None, o_move_fn=None):
    """Return seeded counts/rates and the first X win; default X is random and O basic."""
    raise NotImplementedError("Implement evaluate after predicting its self-checks.")


def main(games=1000, seed=0, start_player=None, output_fn=None):
    """Print default random-versus-basic results, their scope, and return the report."""
    raise NotImplementedError("Implement main after predicting its self-checks.")


if __name__ == "__main__":
    print("Read README.md, implement the learner functions, then change this guard to call main().")
