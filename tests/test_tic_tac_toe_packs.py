"""Independent bitboard, reachable-state, source-role and console checks."""

import ast
from contextlib import redirect_stdout
from copy import deepcopy
from functools import lru_cache
import inspect
import io
import itertools
from pathlib import Path
import random
import runpy
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ["AM14-Tic-Tac-Toe-UI", "AM14-Tic-Tac-Toe-AI",
           "AM14-Tic-Tac-Toe-AI-Test", "AM14-Tic-Tac-Toe-AI-with-Forks"]
MASKS = (7, 56, 448, 73, 146, 292, 273, 84)


def won(cells, mark):
    bits = sum(1 << i for i, cell in enumerate(cells) if cell == mark)
    return any(bits & mask == mask for mask in MASKS)


def status(cells):
    x, o = won(cells, "X"), won(cells, "O")
    if x and o:
        raise ValueError("two winners")
    return "X_won" if x else "O_won" if o else "ongoing" if " " in cells else "draw"


def changed(cells, index, mark):
    return cells[:index] + (mark,) + cells[index + 1:]


def board(cells):
    return [list(cells[i:i+3]) for i in (0, 3, 6)]


def threats(cells, mark):
    if status(cells) != "ongoing":
        return []
    return [i for i, cell in enumerate(cells) if cell == " " and won(changed(cells, i, mark), mark)]


def forks(cells, mark):
    if status(cells) != "ongoing":
        return []
    result = []
    for i, cell in enumerate(cells):
        if cell == " ":
            trial = changed(cells, i, mark)
            if not won(trial, mark) and len(threats(trial, mark)) >= 2:
                result.append(i)
    return result


@lru_cache(maxsize=1)
def reachable():
    states = set()
    def visit(cells, player):
        key = (cells, player)
        if key in states:
            return
        states.add(key)
        if status(cells) == "ongoing":
            for i, cell in enumerate(cells):
                if cell == " ":
                    visit(changed(cells, i, player), "O" if player == "X" else "X")
    for start in ("X", "O"):
        visit((" ",) * 9, start)
    return sorted(states)


class Choice:
    def __init__(self, last=False, mutate=False):
        self.last, self.mutate, self.calls = last, mutate, []

    def choice(self, choices):
        self.calls.append(deepcopy(choices))
        value = deepcopy(choices[-1] if self.last else choices[0])
        if self.mutate and isinstance(choices, list):
            choices[:] = [[0, 0]]
        return value


def scripted(values):
    answers = iter(values)
    def read(prompt):
        try:
            value = next(answers)
        except StopIteration:
            raise EOFError from None
        if isinstance(value, BaseException):
            raise value
        return value
    return read


def replay(outcome):
    cells, player = (" ",) * 9, outcome["start_player"]
    for actor, row, col in outcome["moves"]:
        if status(cells) != "ongoing" or actor != player or cells[row*3+col] != " ":
            raise AssertionError("illegal or post-terminal trace")
        cells = changed(cells, row*3+col, actor)
        player = "O" if player == "X" else "X"
    if board(cells) != outcome["board"]:
        raise AssertionError("trace/board mismatch")
    expected = status(cells)
    if outcome["status"] != "cancelled" and expected != outcome["status"]:
        raise AssertionError("trace/status mismatch")
    winner = expected[0] if expected.endswith("_won") else None
    if outcome["winner"] != winner:
        raise AssertionError("trace/winner mismatch")


def policy_outcomes(module, actor, start):
    """Explore every legal opponent move and every possible random fallback."""
    @lru_cache(None)
    def visit(cells, turn):
        terminal = status(cells)
        if terminal != "ongoing":
            return {terminal: ()}
        if turn == actor:
            rng = Choice()
            if "ai_player_move" in module:
                move = module["ai_player_move"](board(cells), rng, actor)
            else:
                move = module["random_player_move"](board(cells), rng)
            options = rng.calls[0] if rng.calls else [move]
            indices = [row*3+col for row, col in options]
        else:
            indices = [i for i, cell in enumerate(cells) if cell == " "]
        outcomes = {}
        for index in indices:
            if cells[index] != " ":
                raise AssertionError("policy chose occupied square")
            for result, path in visit(changed(cells, index, turn), "O" if turn == "X" else "X").items():
                outcomes.setdefault(result, ((turn, index//3, index%3),) + path)
        return outcomes
    return visit((" ",)*9, start)


class TicTacToePacks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modules = [runpy.run_path(str(ROOT / folder / "solution/main.py"), run_name="checked_ttt")
                       for folder in FOLDERS]

    def test_matching_incomplete_starters_and_reminder_runs(self):
        for folder, reference, count in zip(FOLDERS, self.modules, (13, 15, 14, 17)):
            path = ROOT / folder / "starter/main.py"
            text = path.read_text()
            functions = [node for node in ast.parse(text).body if isinstance(node, ast.FunctionDef)]
            self.assertEqual(len(functions), count)
            learner = runpy.run_path(str(path), run_name="checked_learner")
            for node in functions:
                self.assertEqual(inspect.signature(learner[node.name]), inspect.signature(reference[node.name]))
                self.assertEqual(len(node.body), 2)
                self.assertIsInstance(node.body[1], ast.Raise)
                self.assertEqual(node.body[1].exc.func.id, "NotImplementedError")
            self.assertNotIn("solution", text)
            completed = subprocess.run([sys.executable, "-B", "main.py"], cwd=path.parent,
                                       capture_output=True, text=True, timeout=10)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn("Read README.md", completed.stdout)

    def test_all_imports_are_quiet_and_do_not_prompt(self):
        for folder in FOLDERS:
            for role in ("starter", "solution"):
                output = io.StringIO()
                with redirect_stdout(output), patch("builtins.input", side_effect=AssertionError("prompt")):
                    runpy.run_path(str(ROOT / folder / role / "main.py"), run_name="quiet_ttt")
                self.assertEqual(output.getvalue(), "")

    def test_board_shape_domains_and_fresh_rows(self):
        malformed = (None, (), [], [[" "]]*3, [[False]*3]*3, [["."]*3]*3,
                     [[" "]*3, (" ",)*3, [" "]*3])
        for module in self.modules:
            for value in malformed:
                with self.assertRaises(ValueError):
                    module["duplicate_board"](value)
            first, second = module["make_board"](), module["make_board"]()
            first[0][0] = "X"
            self.assertEqual(second, [[" "]*3 for _ in range(3)])
            self.assertEqual(first[1][0], " ")
            copy = module["duplicate_board"](first)
            self.assertTrue(all(a is not b for a, b in zip(copy, first)))
            for player in (None, "x", "", True):
                with self.assertRaises(ValueError):
                    module["win"](first, player)

    def test_all_19683_symbol_boards_against_bitmask_wins(self):
        for cells in itertools.product((" ", "X", "O"), repeat=9):
            value = board(cells)
            for module in self.modules:
                self.assertEqual(module["win"](value, "X"), won(cells, "X"))
                self.assertEqual(module["win"](value, "O"), won(cells, "O"))
                self.assertEqual(module["finished"](value), " " not in cells)

    def test_reachable_status_moves_and_apply_mutation(self):
        self.assertEqual(len(reachable()), 10956)
        for cells, player in reachable():
            value = board(cells)
            expected = status(cells)
            available = [[i//3, i%3] for i, cell in enumerate(cells)
                         if cell == " " and expected == "ongoing"]
            for module in self.modules:
                self.assertEqual(module["game_status"](value), expected)
                self.assertEqual(module["legal_moves"](value), available)
                for row, col in available:
                    result = module["apply_move"](value, player, row, col)
                    self.assertEqual(result, board(changed(cells, row*3+col, player)))
                    self.assertTrue(all(a is not b for a, b in zip(result, value)))
                self.assertEqual(value, board(cells))

    def test_invalid_occupied_and_terminal_moves(self):
        for module in self.modules:
            value = [["X", "X", "X"], [" ", "O", " "], [" ", " ", "O"]]
            for row, col in ((0, 0), (1, 0), (-1, 0), (3, 0), (True, 0), (0, 1.0)):
                with self.assertRaises(ValueError):
                    module["apply_move"](value, "O", row, col)
            with self.assertRaises(ValueError):
                module["game_status"]([["X"]*3, ["O"]*3, [" "]*3])
            value = module["make_board"]()
            value[0][0] = "X"
            with self.assertRaises(ValueError):
                module["apply_move"](value, "O", 0, 0)

    def test_winning_candidates_and_basic_priority_on_all_reachable_states(self):
        for cells, player in reachable():
            value, before = board(cells), board(cells)
            for module in self.modules[1:]:
                expected = [[i//3, i%3] for i in threats(cells, player)]
                self.assertEqual(module["winning_moves"](value, player), expected)
                for i in range(9):
                    self.assertEqual(module["test_win"](value, i//3, i%3, player), i in threats(cells, player))
            for module in self.modules[1:3]:
                available = [i for i, cell in enumerate(cells) if cell == " " and status(cells) == "ongoing"]
                if not available:
                    self.assertIsNone(module["ai_player_move"](value, Choice(), player))
                    continue
                opponent = "X" if player == "O" else "O"
                own, opposing = threats(cells, player), threats(cells, opponent)
                priority = own or opposing or [i for i in (4, 0, 2, 6, 8) if i in available] or available
                move = module["ai_player_move"](value, Choice(), player)
                self.assertEqual(move, [priority[0]//3, priority[0]%3])
            self.assertEqual(value, before)

    def test_fork_candidates_on_all_reachable_states(self):
        module = self.modules[3]
        for cells, player in reachable():
            value = board(cells)
            expected = forks(cells, player)
            self.assertEqual(module["fork_moves"](value, player), [[i//3, i%3] for i in expected])
            for i in range(9):
                self.assertEqual(module["test_fork"](value, i//3, i%3, player), i in expected)
            self.assertEqual(value, board(cells))

    def test_immediate_win_is_not_fork_and_distinct_threat_coordinates(self):
        module = self.modules[3]
        value = [["X", "X", " "], ["O", " ", " "], [" ", " ", "O"]]
        self.assertFalse(module["test_fork"](value, 0, 2, "X"))
        value = [["X", " ", "X"], [" ", "O", " "], [" ", " ", " "]]
        self.assertTrue(module["test_fork"](value, 2, 0, "X"))
        # The center completes two lines after this candidate, but is one coordinate.
        value = [["O", "X", " "], ["X", " ", "X"], [" ", " ", "O"]]
        self.assertFalse(module["test_fork"](value, 2, 1, "X"))

    def test_fork_ai_is_legal_and_honors_win_block_fork_priority(self):
        module = self.modules[3]
        for cells, player in reachable():
            value = board(cells)
            move = module["ai_player_move"](value, Choice(), player)
            if status(cells) != "ongoing":
                self.assertIsNone(move)
            else:
                index = move[0]*3+move[1]
                self.assertEqual(cells[index], " ")
                opponent = "X" if player == "O" else "O"
                priority = threats(cells, player) or threats(cells, opponent) or forks(cells, player)
                if priority:
                    self.assertEqual(index, priority[0])
            self.assertEqual(value, board(cells))

    def test_opposite_corner_multiple_fork_defense(self):
        module = self.modules[3]
        value = [["X", " ", " "], [" ", "O", " "], [" ", " ", "X"]]
        self.assertEqual(module["fork_moves"](value, "X"), [[0, 2], [2, 0]])
        move = module["ai_player_move"](value, Choice())
        self.assertEqual(move, [0, 1])
        trial = module["apply_move"](value, "O", *move)
        forced = module["winning_moves"](trial, "O")
        self.assertEqual(len(forced), 1)
        self.assertFalse(module["test_fork"](trial, *forced[0], "X"))

    def test_random_selection_terminal_and_mutating_rng_copy(self):
        for module in (self.modules[0], self.modules[2]):
            value = module["make_board"]()
            value[0][0] = "X"
            before = deepcopy(value)
            self.assertEqual(module["random_player_move"](value, Choice(last=True, mutate=True)), [2, 2])
            self.assertEqual(value, before)
            value[0] = ["X"]*3
            self.assertIsNone(module["random_player_move"](value, Choice()))
            with self.assertRaises(ValueError):
                module["random_player_move"](before, object())
            class Bad:
                def choice(self, choices):
                    choices.append([0, 0])
                    return [0, 0]
            with self.assertRaises(ValueError):
                module["random_player_move"](before, Bad())
        for module in self.modules[1:]:
            value = [["X", "O", "X"], [" ", "X", " "], ["O", "X", "O"]]
            self.assertEqual(module["ai_player_move"](value, Choice(last=True, mutate=True)), [1, 2])
            class CorruptingChoice:
                def choice(self, choices):
                    choices.append([0, 0])
                    return [0, 0]
            with self.assertRaises(ValueError):
                module["ai_player_move"](value, CorruptingChoice())

    def test_coordinate_records_and_exact_ascii_render(self):
        for module in (self.modules[0], self.modules[1], self.modules[3]):
            for text, expected in (("  +0\r\n", 0), ("-0", 0), ("02", 2), (" QUIT ", None)):
                self.assertEqual(module["parse_coordinate"](text), expected)
            for text in ("", "3", "-1", "1.0", "١", "1_0", "0 1", None, True, "9"*5000):
                with self.assertRaises(ValueError):
                    module["parse_coordinate"](text)
            value = [["X", " ", "O"], [" ", "X", " "], ["O", " ", " "]]
            expected = " X |   | O \n---+---+---\n   | X |   \n---+---+---\n O |   |   \n"
            self.assertEqual(module["render_board"](value), expected)
            output = []
            module["print_board"](value, output.append)
            self.assertEqual(output, [expected])

    def test_quit_eof_and_interrupt_at_both_prompts(self):
        for module in (self.modules[0], self.modules[1], self.modules[3]):
            for inputs in (("quit",), ("1", "quit"), (), ("1",), (KeyboardInterrupt(),), ("1", KeyboardInterrupt())):
                output = []
                outcome = module["play"]("X", scripted(inputs), output.append, Choice())
                self.assertEqual(outcome["status"], "cancelled")
                self.assertEqual(outcome["moves"], [])
                self.assertIsNone(outcome["winner"])
                self.assertEqual(output[-1], "Game cancelled.")
                replay(outcome)

    def test_invalid_pair_and_occupied_retry_do_not_advance_turn(self):
        for module in (self.modules[0], self.modules[1], self.modules[3]):
            inputs = ("bad", "0", "oops", "0", "0", "0", "0", "quit")
            output = []
            outcome = module["play"]("X", scripted(inputs), output.append, Choice())
            self.assertEqual([move[0] for move in outcome["moves"]], ["X", "O"])
            self.assertEqual(outcome["moves"][0], ("X", 0, 0))
            self.assertEqual(outcome["status"], "cancelled")
            self.assertTrue(any("occupied" in item for item in output))
            replay(outcome)

    def test_unexpected_callback_errors_propagate_and_config_validates_before_io(self):
        for module in (self.modules[0], self.modules[1], self.modules[3]):
            def broken(prompt):
                raise ValueError("callback failure")
            with self.assertRaisesRegex(ValueError, "callback failure"):
                module["play"]("X", broken, lambda message: None)
            output = []
            with self.assertRaises(ValueError):
                module["play"]("Z", scripted([]), output.append)
            self.assertEqual(output, [])
            with self.assertRaises(RuntimeError):
                module["play"]("X", scripted([]), lambda message: (_ for _ in ()).throw(RuntimeError("output")))

    def test_call_time_defaults_random_start_and_direct_reference_runs(self):
        for folder, module in zip(FOLDERS, self.modules):
            if folder.endswith("AI-Test"):
                continue
            with patch("builtins.input", side_effect=EOFError), patch("builtins.print") as output:
                outcome = module["main"]("X")
                self.assertEqual(outcome["status"], "cancelled")
                self.assertTrue(output.called)
            outcome = module["play"](None, scripted(["quit"]), lambda message: None, Choice(last=True))
            self.assertEqual(outcome["start_player"], "O")
            self.assertEqual(len(outcome["moves"]), 1)
            result = subprocess.run([sys.executable, "-B", "main.py"], cwd=ROOT/folder/"solution",
                                    input="quit\n", capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Game cancelled.", result.stdout)

    def test_bounded_games_and_seeded_evaluation_counts_rates_and_freshness(self):
        module = self.modules[2]
        for start in (None, "X", "O"):
            for seed in range(10):
                outcome = module["play_game"](start, random.Random(seed))
                self.assertLessEqual(len(outcome["moves"]), 9)
                replay(outcome)
            first = module["evaluate"](100, 7, start)
            second = module["evaluate"](100, 7, start)
            self.assertEqual(first, second)
            self.assertEqual(sum(first[key] for key in ("x_wins", "o_wins", "draws")), 100)
            for key, rate in first["rates"].items():
                self.assertEqual(rate, first[key]/100)
            if first["first_x_win"]:
                replay(first["first_x_win"])
                self.assertIsNot(first["first_x_win"]["board"], second["first_x_win"]["board"])
        zero = module["evaluate"](0)
        self.assertEqual(zero["rates"], {"x_wins": 0.0, "o_wins": 0.0, "draws": 0.0})
        self.assertIsNone(zero["first_x_win"])

    def test_custom_experiment_strategy_copy_and_invalid_results(self):
        module = self.modules[2]
        def modifying(value, rng):
            available = module["legal_moves"](value)
            value[0][:] = ["O"]*3
            return available[0]
        outcome = module["play_game"]("X", Choice(), modifying, modifying)
        replay(outcome)
        for move in (None, [True, 0], [3, 0], [0], "00"):
            with self.assertRaises(ValueError):
                module["play_game"]("X", Choice(), lambda value, rng: move)
        def occupied(value, rng):
            return [0, 0]
        with self.assertRaises(ValueError):
            module["play_game"]("X", Choice(), occupied, occupied)
        advanced = self.modules[3]["ai_player_move"]
        basic = module["ai_player_move"]
        for policy in (basic, advanced):
            outcome = module["play_game"]("X", Choice(), lambda value, rng: basic(value, rng, "X"), policy)
            replay(outcome)

    def test_experiment_configuration_and_honest_main(self):
        module = self.modules[2]
        for games in (-1, 10001, True, 1.0):
            with self.assertRaises(ValueError):
                module["evaluate"](games)
        for arguments in ({"seed": True}, {"seed": "0"}, {"start_player": "x"}, {"x_move_fn": 3}, {"o_move_fn": []}):
            with self.assertRaises(ValueError):
                module["evaluate"](0, **arguments)
        with patch("builtins.print") as output:
            report = module["main"](0)
            self.assertEqual(report["games"], 0)
            self.assertTrue(any("do not prove optimality" in call.args[0] for call in output.call_args_list))

    def test_all_legal_opponents_both_marks_orders_and_random_fallbacks(self):
        for actor, start in itertools.product(("X", "O"), repeat=2):
            opponent = "O" if actor == "X" else "X"
            outcomes = policy_outcomes(self.modules[3], actor, start)
            self.assertEqual(set(outcomes), {actor+"_won", "draw"})
            basic = policy_outcomes(self.modules[1], actor, start)
            expected = {actor+"_won", "draw"}
            if start == opponent:
                expected.add(opponent+"_won")
            self.assertEqual(set(basic), expected)

    def test_complete_console_wins_draws_and_terminal_messages(self):
        for module in (self.modules[0], self.modules[1], self.modules[3]):
            for start in ("X", "O"):
                for expected, trace in policy_outcomes(module, "O", start).items():
                    state = {"completed": -1}
                    output = []
                    def display(text):
                        output.append(text)
                        if "---+---+---" in text:
                            state["completed"] += 1
                    class TraceChoice:
                        def choice(self, choices):
                            actor, row, col = trace[state["completed"]]
                            if actor != "O":
                                raise AssertionError("unexpected computer turn")
                            return [row, col]
                    inputs = [str(number) for actor, row, col in trace if actor == "X"
                              for number in (row, col)]
                    outcome = module["main"](start, scripted(inputs), display, TraceChoice())
                    self.assertEqual(outcome["status"], expected)
                    self.assertEqual(outcome["moves"], list(trace))
                    self.assertLessEqual(len(outcome["moves"]), 9)
                    self.assertEqual(output[-1], "Draw." if expected == "draw" else expected[0]+" wins.")
                    replay(outcome)

    def test_known_basic_loss_is_reproducible_and_separate_from_learner_work(self):
        inputs = ["0", "0", "2", "1", "2", "0", "2", "2"]
        outcome = self.modules[1]["play"]("X", scripted(inputs), lambda text: None, Choice())
        self.assertEqual(outcome["status"], "X_won")
        self.assertEqual(outcome["moves"], [("X",0,0), ("O",1,1), ("X",2,1),
                                            ("O",0,2), ("X",2,0), ("O",1,0), ("X",2,2)])
        replay(outcome)


if __name__ == "__main__":
    unittest.main()
