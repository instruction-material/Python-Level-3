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


def render_board(board):
    """Return an ASCII board with separators and a final LF; never print."""
    _board(board)
    rows = ["|".join(f" {cell} " for cell in row) for row in board]
    return "\n---+---+---\n".join(rows) + "\n"


def print_board(board, output_fn=None):
    """Send the complete render to one call of the call-time output callback."""
    output_fn = print if output_fn is None else output_fn
    if not callable(output_fn):
        raise ValueError("The output callback must be callable.")
    output_fn(render_board(board))


def parse_coordinate(text):
    """Return a signed ASCII coordinate 0..2, or None for case-insensitive quit."""
    if not isinstance(text, str):
        raise ValueError("A coordinate record must be text.")
    token = text.strip()
    if token.casefold() == "quit":
        return None
    if re.fullmatch(r"[+-]?[0-9]+", token) is None:
        raise ValueError("Enter an ASCII integer from 0 through 2 or quit.")
    try:
        coordinate = int(token)
    except ValueError as error:
        raise ValueError("The coordinate text is too long.") from error
    _coordinate(coordinate)
    return coordinate


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


def test_fork(board, i, j, player):
    """Test a non-winning candidate creating at least two distinct immediate threats."""
    _board(board)
    _player(player)
    _coordinate(i)
    _coordinate(j)
    if game_status(board) != "ongoing" or board[i][j] != " ":
        return False
    trial = apply_move(board, player, i, j)
    return not win(trial, player) and len(winning_moves(trial, player)) >= 2


def fork_moves(board, player):
    """Return fresh row-major non-winning fork coordinates without mutation."""
    _player(player)
    return [move for move in legal_moves(board) if test_fork(board, *move, player)]


def ai_player_move(board, rng=None, player="O"):
    """Choose own win, opponent block, own fork, fork defense, center, corner, side."""
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
    own_forks = fork_moves(board, player)
    if own_forks:
        return own_forks[0]
    opposing_forks = fork_moves(board, opponent)
    if len(opposing_forks) == 1:
        return opposing_forks[0]
    if len(opposing_forks) > 1:
        edges = [[0, 1], [1, 0], [1, 2], [2, 1]]
        ordered = [move for move in edges if move in available]
        ordered += [move for move in available if move not in edges]
        # A forcing threat is safe only if the compulsory block cannot win or fork.
        for move in ordered:
            trial = apply_move(board, player, *move)
            threats = winning_moves(trial, player)
            if len(threats) == 1:
                row, col = threats[0]
                if not test_win(trial, row, col, opponent) and not test_fork(trial, row, col, opponent):
                    return move[:]
        for move in ordered:
            if not fork_moves(apply_move(board, player, *move), opponent):
                return move[:]
    for move in ([1, 1], [0, 0], [0, 2], [2, 0], [2, 2]):
        if move in available:
            return move[:]
    return _move(rng.choice([move[:] for move in available]), available)


def play(start_player=None, input_fn=None, output_fn=None, rng=None):
    """Play human X versus computer O; invalid input retries, quit/EOF cancels."""
    input_fn = input if input_fn is None else input_fn
    output_fn = print if output_fn is None else output_fn
    if not callable(input_fn) or not callable(output_fn):
        raise ValueError("Input and output callbacks must be callable.")
    if start_player is not None:
        _player(start_player)
    rng = _rng(rng)
    start_player = _start(start_player, rng)
    player, board, moves = start_player, make_board(), []
    output_fn(f"{start_player} starts. Human X; computer O. Coordinates 0..2; quit cancels.")

    def finish(status):
        output_fn("Game cancelled." if status == "cancelled" else
                  "Draw." if status == "draw" else f"{status[0]} wins.")
        return _result(status, board, moves, start_player)

    print_board(board, output_fn)
    while True:
        if player == "X":
            coordinates = []
            for label in ("Row", "Column"):
                try:
                    text = input_fn(f"{label} (0..2/quit): ")
                except (EOFError, KeyboardInterrupt):
                    return finish("cancelled")
                try:
                    coordinate = parse_coordinate(text)
                except ValueError:
                    output_fn("Invalid coordinate. Retry the row/column pair.")
                    break
                if coordinate is None:
                    return finish("cancelled")
                coordinates.append(coordinate)
            if len(coordinates) != 2:
                continue
            row, col = coordinates
            if board[row][col] != " ":
                output_fn("That square is occupied. Retry the row/column pair.")
                continue
        else:
            row, col = ai_player_move(board, rng)
            output_fn(f"O chooses {row}, {col}.")
        board = apply_move(board, player, row, col)
        moves.append((player, row, col))
        print_board(board, output_fn)
        status = game_status(board)
        if status != "ongoing":
            return finish(status)
        player = "O" if player == "X" else "X"


def main(start_player=None, input_fn=None, output_fn=None, rng=None):
    """Run the guarded console game and return its explicit final outcome."""
    return play(start_player, input_fn, output_fn, rng)


if __name__ == "__main__":
    main()
