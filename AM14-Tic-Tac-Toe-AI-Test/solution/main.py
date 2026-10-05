"""Finite Tic Tac Toe helpers; reference answers are separate from learner work."""

import random
import re


def _board(board):
    if (type(board) is not list or len(board) != 3
            or any(type(row) is not list or len(row) != 3 for row in board)
            or any(type(cell) is not str or cell not in (" ", "X", "O")
                   for row in board for cell in row)):
        raise ValueError("Use three list rows of three space/X/O strings.")


def _player(player):
    if type(player) is not str or player not in ("X", "O"):
        raise ValueError("The player must be X or O.")


def _coordinate(number):
    if type(number) is not int or not 0 <= number <= 2:
        raise ValueError("A coordinate must be an integer from 0 through 2.")


def _rng(rng):
    rng = random if rng is None else rng
    if not callable(getattr(rng, "choice", None)):
        raise ValueError("The random source must have a callable choice method.")
    return rng


def _move(move, available):
    if type(move) not in (list, tuple) or len(move) != 2:
        raise ValueError("A strategy must return a row/column pair.")
    row, col = move
    _coordinate(row)
    _coordinate(col)
    result = [row, col]
    if result not in available:
        raise ValueError("A strategy must choose an available square.")
    return result


def _start(start_player, rng):
    if start_player is None:
        start_player = rng.choice(("X", "O"))
    _player(start_player)
    return start_player


def make_board():
    """Return a new empty 3x3 board with independently allocated rows."""
    return [[" " for _ in range(3)] for _ in range(3)]


def duplicate_board(board):
    """Validate and copy every row; no caller-owned list is reused."""
    _board(board)
    return [row[:] for row in board]


def win(board, player):
    """Check all eight winning lines for X or O without changing the board."""
    _board(board)
    _player(player)
    lines = [board[row] for row in range(3)]
    lines += [[board[row][col] for row in range(3)] for col in range(3)]
    lines += [[board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)]]
    return any(all(cell == player for cell in line) for line in lines)


def finished(board):
    """Return whether all nine squares are occupied, independently of wins."""
    _board(board)
    return all(cell != " " for row in board for cell in row)


def game_status(board):
    """Return ongoing/X_won/O_won/draw; reject simultaneous winners."""
    _board(board)
    x_won, o_won = win(board, "X"), win(board, "O")
    if x_won and o_won:
        raise ValueError("A game board cannot have two winners.")
    if x_won:
        return "X_won"
    if o_won:
        return "O_won"
    return "draw" if finished(board) else "ongoing"


def legal_moves(board):
    """Return fresh row-major coordinate lists; terminal boards have no moves."""
    if game_status(board) != "ongoing":
        return []
    return [[row, col] for row in range(3) for col in range(3)
            if board[row][col] == " "]


def apply_move(board, player, row, col):
    """Return a fresh board after one legal move; reject ended/occupied positions."""
    _board(board)
    _player(player)
    _coordinate(row)
    _coordinate(col)
    if game_status(board) != "ongoing" or board[row][col] != " ":
        raise ValueError("The move needs an empty square in an ongoing game.")
    result = duplicate_board(board)
    result[row][col] = player
    return result


def _result(status, board, moves, start_player):
    return {"status": status, "winner": status[0] if status.endswith("_won") else None,
            "board": duplicate_board(board), "moves": moves[:], "start_player": start_player}


def test_win(board, i, j, player):
    """Test one vacant candidate on copied rows; ended or occupied positions are false."""
    _board(board)
    _player(player)
    _coordinate(i)
    _coordinate(j)
    if game_status(board) != "ongoing" or board[i][j] != " ":
        return False
    return win(apply_move(board, player, i, j), player)


def winning_moves(board, player):
    """Return fresh row-major immediate winning coordinates for the named player."""
    _player(player)
    return [move for move in legal_moves(board) if test_win(board, *move, player)]


def random_player_move(board, rng=None):
    """Choose uniformly from legal positions; return None when the game has ended."""
    rng = _rng(rng)
    available = legal_moves(board)
    return _move(rng.choice([move[:] for move in available]), available) if available else None


def ai_player_move(board, rng=None, player="O"):
    """Choose own win, opponent block, center, first corner, then random legal side."""
    rng = _rng(rng)
    _player(player)
    available = legal_moves(board)
    if not available:
        return None
    opponent = "X" if player == "O" else "O"
    for mark in (player, opponent):
        threats = winning_moves(board, mark)
        if threats:
            return threats[0]
    for move in ([1, 1], [0, 0], [0, 2], [2, 0], [2, 2]):
        if move in available:
            return move[:]
    return _move(rng.choice([move[:] for move in available]), available)


def play_game(start_player=None, rng=None, x_move_fn=None, o_move_fn=None):
    """Run one fresh game with copy-isolated strategies and at most nine moves."""
    if start_player is not None:
        _player(start_player)
    rng = _rng(rng)
    x_move_fn = random_player_move if x_move_fn is None else x_move_fn
    o_move_fn = ai_player_move if o_move_fn is None else o_move_fn
    if not callable(x_move_fn) or not callable(o_move_fn):
        raise ValueError("Both strategies must be callable.")
    start_player = _start(start_player, rng)
    player, board, moves = start_player, make_board(), []
    for _ in range(9):
        strategy = x_move_fn if player == "X" else o_move_fn
        move = _move(strategy(duplicate_board(board), rng), legal_moves(board))
        board = apply_move(board, player, *move)
        moves.append((player, *move))
        status = game_status(board)
        if status != "ongoing":
            return _result(status, board, moves, start_player)
        player = "O" if player == "X" else "X"
    raise RuntimeError("Nine legal moves must terminate a 3x3 game.")


def evaluate(games=1000, seed=0, start_player=None, x_move_fn=None, o_move_fn=None):
    """Return seeded counts/rates and the first X win; default X is random and O basic."""
    if type(games) is not int or not 0 <= games <= 10000:
        raise ValueError("games must be an integer from 0 through 10000.")
    if seed is not None and type(seed) is not int:
        raise ValueError("seed must be an integer or None.")
    if start_player is not None:
        _player(start_player)
    if ((x_move_fn is not None and not callable(x_move_fn))
            or (o_move_fn is not None and not callable(o_move_fn))):
        raise ValueError("Strategies must be callable or None.")
    rng = random.Random(seed)
    counts = {"x_wins": 0, "o_wins": 0, "draws": 0}
    first_x_win = None
    for _ in range(games):
        outcome = play_game(start_player, rng, x_move_fn, o_move_fn)
        key = {"X_won": "x_wins", "O_won": "o_wins", "draw": "draws"}[outcome["status"]]
        counts[key] += 1
        if outcome["status"] == "X_won" and first_x_win is None:
            first_x_win = outcome
    rates = {key: count / games if games else 0.0 for key, count in counts.items()}
    return {"games": games, "seed": seed, "start_player": start_player,
            **counts, "rates": rates, "first_x_win": first_x_win}


def main(games=1000, seed=0, start_player=None, output_fn=None):
    """Print default random-versus-basic results, their scope, and return the report."""
    output_fn = print if output_fn is None else output_fn
    if not callable(output_fn):
        raise ValueError("The output callback must be callable.")
    report = evaluate(games, seed, start_player)
    output_fn(f"Games: {games}; seed: {seed}; starting player: {start_player or 'random'}")
    output_fn(f"X RANDOM WINS: {report['x_wins']}")
    output_fn(f"O BASIC AI WINS: {report['o_wins']}")
    output_fn(f"DRAWS: {report['draws']}")
    for key, rate in report["rates"].items():
        output_fn(f"{key}: {100 * rate:.2f}%")
    output_fn("These results measure the tested random opponent and starting order; they do not prove optimality.")
    return report


if __name__ == "__main__":
    main()
