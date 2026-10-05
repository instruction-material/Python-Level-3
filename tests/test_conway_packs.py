"""Independent Conway rule, source-role, pattern and console regression checks."""

import ast
from contextlib import redirect_stdout
from copy import deepcopy
import hashlib
import inspect
import io
import itertools
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SINGLE = "AM13-Conways-Game-of-Life"
MULTI = "AM13-Two-Player-Conways"
# Frozen LF and configured CRLF digests from baseline efd0cdfb190a9110ec1a160786e13f724a60153f.
ASSET_DIGESTS = {
    "AM13-Conways-Game-of-Life/b-heptomino-shuttle.in": (
        "7a36638a57420f796c466c4395b1231e61ba0404f29d88b309d33c56a225fbf4",
        "ab3309cb01d9ff922be2574106ceaf9a119067570da54a3b2c8cf75bb5f5c6c1",
    ),
    "AM13-Conways-Game-of-Life/boat.in": (
        "68fb15811ce8e5c1f3b118dd7d95b57fbf26bad89c6ea171261aa5c49c348013",
        "96df9b8467c5a4a1f754af34a1c0fa5ed3d5a1070a348965ea0c387f4a6066c9",
    ),
    "AM13-Conways-Game-of-Life/design1.in": (
        "7923908dd9291bf04ef3d3ca2b303d07ece53192dd8d5c148c9560ea175b1e8a",
        "2e543fc99f8ebf87d29308fe25492f02eb6460b98bdcfa823d672cb8818f870c",
    ),
    "AM13-Conways-Game-of-Life/f-pentomino.in": (
        "9869ce538ea1808027456e429a39a2997fe7f8852b36f7d79cbff89032cd9c70",
        "a462f9ec31fae8af72f4e8204ceaf4039fc1ee3b00865fca8c8efa36c94a24d3",
    ),
    "AM13-Conways-Game-of-Life/hertz-oscillator.in": (
        "600584759ce1122384b96c56b26be689af4b7906aa508477f5a80b9a05e3c345",
        "b1e0e55a660baa77af76e1872ed91eca50d8b5597d1b496812d4c7c8529a6679",
    ),
    "AM13-Conways-Game-of-Life/repeat.in": (
        "48e3ffa23891bc27613df3aa2ec73f5fc0542f34ecca3323261635e724433377",
        "987c05f46519c516cf4140d53e128140b5380a393a44219d4647befdb0c4b961",
    ),
    "AM13-Conways-Game-of-Life/spaceship.in": (
        "21eeb302c63a9d362add7b82e7fd146b7764fc320cff64e5cf13e0429008f654",
        "f8a591afe7e7f7b07404dab0b812fc4a8be7fafaaaebc44128a371794c3cd9dc",
    ),
    "AM13-Conways-Game-of-Life/square.in": (
        "4cb6c005cc3d39e44353c489a4dc13776903d270a50186e8fe05a018537fa6e7",
        "661aecb29d2e59306f628be478c05441920533bbc423a53d2d32e2b4af18d5ed",
    ),
    "AM13-Two-Player-Conways/player1.in": (
        "b0352395372fd463e6a0c9a2f10a8be4650978fa1bb0c4ef9865f18ef267683b",
        "352173b777116ab32df5a3bb7ace2e9aef7529dce928badb10306d50d6c898fc",
    ),
    "AM13-Two-Player-Conways/player2.in": (
        "43cd440da61a1ed7d770c2bdfa3dc552085337d1c866c1881cbe3e49c72932f3",
        "c13377f8a56124aae81a3b89c5b003b7fc5bdaa5728022e0aef7d8c4a4ad31fa",
    ),
}


def load(folder, role="solution", filename="main.py"):
    return runpy.run_path(str(ROOT / folder / role / filename), run_name="checked_conway")


def oracle(board, owned=False):
    """Enumerate neighbor offsets independently of the reference's clipped loops."""
    result = []
    for row in range(len(board)):
        line = []
        for col in range(len(board[0])):
            values = [
                board[row + dr][col + dc]
                for dr, dc in itertools.product((-1, 0, 1), repeat=2)
                if (dr, dc) != (0, 0)
                and 0 <= row + dr < len(board)
                and 0 <= col + dc < len(board[0])
            ]
            live = sum(value != 0 for value in values)
            if board[row][col]:
                next_value = board[row][col] if live in (2, 3) else (0 if owned else False)
            elif live == 3:
                next_value = (1 if values.count(1) > values.count(2) else 2) if owned else True
            else:
                next_value = 0 if owned else False
            line.append(next_value)
        result.append(line)
    return result


def scripted(values, prompts=None):
    answers = iter(values)
    def read(prompt):
        if prompts is not None:
            prompts.append(prompt)
        try:
            value = next(answers)
        except StopIteration:
            raise EOFError from None
        if isinstance(value, BaseException):
            raise value
        return value
    return read


class ConwayPacks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.single = load(SINGLE)
        cls.multi = load(MULTI)

    def test_starters_match_signatures_and_remain_incomplete(self):
        for folder, reference, count in ((SINGLE, self.single, 10), (MULTI, self.multi, 14)):
            text = (ROOT / folder / "starter/main.py").read_text()
            tree = ast.parse(text)
            functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
            self.assertEqual(len(functions), count)
            learner = load(folder, "starter")
            for node in functions:
                self.assertEqual(len(node.body), 2)
                self.assertIsInstance(node.body[1], ast.Raise)
                self.assertEqual(inspect.signature(learner[node.name]),
                                 inspect.signature(reference[node.name]))
            self.assertNotIn("solution", text)
            result = subprocess.run([sys.executable, "-B", "main.py"],
                                    cwd=ROOT / folder / "starter", capture_output=True,
                                    text=True, timeout=5, check=True)
            self.assertIn("Implement the", result.stdout)
            self.assertEqual(result.stderr, "")

    def test_imports_are_quiet_and_legacy_wrappers_use_sibling_reference(self):
        for folder, reference in ((SINGLE, self.single), (MULTI, self.multi)):
            with redirect_stdout(io.StringIO()) as output, patch("builtins.input", side_effect=AssertionError), \
                    patch("time.sleep", side_effect=AssertionError):
                learner = load(folder, "starter")
                canonical = load(folder)
                with patch.dict(sys.modules, {"main": object()}):
                    wrapper = load(folder, filename=folder + ".py")
            self.assertEqual(output.getvalue(), "")
            self.assertIn("main", learner)
            for name in wrapper["_PUBLIC_NAMES"]:
                if callable(reference[name]):
                    self.assertEqual(inspect.signature(wrapper[name]),
                                     inspect.signature(canonical[name]))
                else:
                    self.assertEqual(wrapper[name], canonical[name])
            board = [[True, True], [True, True]] if folder == SINGLE else [[1, 2], [2, 1]]
            self.assertEqual(wrapper["next_generation"](board), canonical["next_generation"](board))

    def test_original_assets_match_frozen_git_bytes_and_starter_copies(self):
        for folder, reference, expected_count in ((SINGLE, self.single, 8), (MULTI, self.multi, 2)):
            assets = sorted((ROOT / folder / "solution").glob("*.in"))
            self.assertEqual(len(assets), expected_count)
            for asset in assets:
                local = asset.read_bytes()
                self.assertIn(hashlib.sha256(local).hexdigest(),
                              ASSET_DIGESTS[f"{folder}/{asset.name}"])
                self.assertEqual((ROOT / folder / "starter" / asset.name).read_bytes(), local)
                points = reference["read_coordinates"](asset)
                self.assertGreater(len(points), 0)
            if folder == MULTI:
                self.assertEqual([len(reference["read_coordinates"](a)) for a in assets], [5, 5])

    def test_coordinate_parsers_preserve_records_duplicates_and_domains(self):
        for ref in (self.single, self.multi):
            lines = [" +0 1\r\n", "\t", "2\t3\n", "0 1"]
            before = lines.copy()
            self.assertEqual(ref["parse_coordinates"](lines, 3, 4), [(0, 1), (2, 3), (0, 1)])
            self.assertEqual(lines, before)
            for bad in (None, "0 1", [0], ["1"], ["1 2 3"], ["1.0 0"],
                        ["١ 0"], ["0 4"], ["-1 0"], ["0 1\n2 3"], ["0 1\n\n"]):
                with self.subTest(bad=bad), self.assertRaises(ValueError):
                    ref["parse_coordinates"](bad, 3, 4)
            for height, width in ((0, 2), (2, 0), (True, 2), (2, 2.0)):
                with self.assertRaises(ValueError):
                    ref["parse_coordinates"]([], height, width)

    def test_coordinate_files_close_preserve_bytes_and_fail_honestly(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "pattern.in"
            path.write_bytes(b"0 0\r\n\r\n1 2")
            for ref in (self.single, self.multi):
                self.assertEqual(ref["read_coordinates"](path, 2, 3), [(0, 0), (1, 2)])
                self.assertEqual(path.read_bytes(), b"0 0\r\n\r\n1 2")
                with self.assertRaises(FileNotFoundError):
                    ref["read_coordinates"](Path(temp) / "missing")
                path.write_bytes(b"0 0\nmalformed")
                with self.assertRaises(ValueError):
                    ref["read_coordinates"](path, 2, 3)
                path.write_bytes(b"0 0\r\n\r\n1 2")
            self.assertEqual(path.read_bytes(), b"0 0\r\n\r\n1 2")
        for ref in (self.single, self.multi):
            for contents in ("0 0", "invalid"):
                stream = io.StringIO(contents)
                with patch("builtins.open", return_value=stream):
                    if contents == "invalid":
                        with self.assertRaises(ValueError):
                            ref["read_coordinates"]("pattern.in")
                    else:
                        self.assertEqual(ref["read_coordinates"]("pattern.in"), [(0, 0)])
                self.assertTrue(stream.closed)

    def test_make_grids_validate_all_points_duplicates_overlap_and_fresh_rows(self):
        points = [(0, 0), (0, 0)]
        self.assertEqual(self.single["make_grid"](points, 2, 3),
                         [[True, False, False], [False, False, False]])
        self.assertEqual(points, [(0, 0), (0, 0)])
        board = self.multi["make_grid"](points, [(1, 2)], 2, 3)
        self.assertEqual(board, [[1, 0, 0], [0, 0, 2]])
        self.assertIsNot(board[0], board[1])
        for bad in ([(False, 0)], [(0, 0), (2, 0)], [(0,)], "0 0"):
            with self.assertRaises(ValueError):
                self.single["make_grid"](bad, 2, 3)
        with self.assertRaises(ValueError):
            self.multi["make_grid"]([(0, 0)], [(0, 0)], 2, 3)
        with self.assertRaises(ValueError):
            self.multi["make_grid"]([], [(2, 0)], 2, 3)

    def test_grid_validation_is_strict_and_precedes_output(self):
        for ref, wrong in ((self.single, [[1]]), (self.multi, [[True]])):
            for grid in ([], [[]], [[0], []], [1], None, wrong):
                for operation in ("next_generation", "render_board"):
                    with self.subTest(operation=operation, grid=grid), self.assertRaises(ValueError):
                        ref[operation](grid)
                with self.assertRaises(ValueError):
                    ref["print_board"](grid, lambda text: self.fail("unexpected output"))
            good = [[True]] if ref is self.single else [[1]]
            with self.assertRaises(ValueError):
                ref["neighbors"](good, good[0][0], -1, 0)
            with self.assertRaises(ValueError):
                ref["neighbors"](good, False if ref is self.multi else 1, 0, 0)

    def test_single_generation_matches_exhaustive_rectangular_oracle(self):
        for cells in itertools.product((False, True), repeat=6):
            grid = [list(cells[:3]), list(cells[3:])]
            before = deepcopy(grid)
            result = self.single["next_generation"](grid)
            self.assertEqual(result, oracle(before))
            self.assertEqual(grid, before)
            self.assertIsNot(result, grid)
            for row in range(2):
                self.assertIsNot(result[row], grid[row])
                for col in range(3):
                    self.assertEqual(self.single["neighbors"](grid, grid[row][col], row, col),
                                     result[row][col])
        self.assertEqual(self.single["count_neighbors"]([[True, True], [True, False]], 0, 0), 2)

    def test_single_block_blinker_empty_and_one_cell_patterns(self):
        block = self.single["make_grid"]([(1, 1), (1, 2), (2, 1), (2, 2)], 4, 4)
        self.assertEqual(self.single["next_generation"](block), block)
        horizontal = self.single["make_grid"]([(2, 1), (2, 2), (2, 3)], 5, 5)
        vertical = self.single["make_grid"]([(1, 2), (2, 2), (3, 2)], 5, 5)
        self.assertEqual(self.single["next_generation"](horizontal), vertical)
        self.assertEqual(self.single["next_generation"](vertical), horizontal)
        self.assertEqual(self.single["next_generation"]([[True]]), [[False]])
        self.assertEqual(self.single["next_generation"]([[False, False]]), [[False, False]])

    def test_owned_generation_matches_exhaustive_oracle_and_preserves_inputs(self):
        for cells in itertools.product((0, 1, 2), repeat=6):
            board = [list(cells[:3]), list(cells[3:])]
            before = deepcopy(board)
            result = self.multi["next_generation"](board)
            self.assertEqual(result, oracle(before, owned=True))
            self.assertEqual(board, before)
            self.assertIsNot(result[0], result[1])
            self.assertIsNot(result[0], board[0])
        self.assertEqual(self.multi["neighbor_counts"]([[1, 2], [2, 0]], 0, 0), (0, 2))

    def test_owned_survivors_keep_owner_and_births_use_majority(self):
        board = [[2, 2, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(self.multi["neighbors"](board, 1, 1, 1), 1)
        board = [[1, 2, 0], [1, 0, 0], [0, 0, 0]]
        self.assertEqual(self.multi["neighbors"](board, 0, 1, 1), 1)
        reversed_owners = [[3 - cell if cell else 0 for cell in row] for row in board]
        self.assertEqual(self.multi["neighbors"](reversed_owners, 0, 1, 1), 2)

    def test_rendering_and_print_callbacks_are_exact_and_fresh(self):
        self.assertEqual(self.single["render_board"]([[True, False], [False, True]]), "O-\n-O\n")
        self.assertEqual(self.multi["render_board"]([[1, 0], [0, 2]]), "  0 1\n0 O -\n1 - X\n")
        text = self.multi["render_board"]([[0] * 12 for _ in range(11)])
        self.assertEqual(len(text.splitlines()), 12)
        self.assertTrue(text.splitlines()[0].endswith("10 11"))
        self.assertTrue(text.splitlines()[-1].startswith("10 "))
        self.assertTrue(all(line == line.rstrip() for line in text.splitlines()))
        for ref, grid in ((self.single, [[False]]), (self.multi, [[0]])):
            output = []
            self.assertIsNone(ref["print_board"](grid, output.append))
            self.assertEqual(output, [ref["render_board"](grid)])
            with redirect_stdout(io.StringIO()) as stream:
                ref["print_board"](grid)
            self.assertEqual(stream.getvalue(), output[0])
            with self.assertRaises(ValueError):
                ref["print_board"](grid, 3)

    def test_single_run_counts_delays_copies_and_default_output(self):
        board = [[True]]
        output, delays = [], []
        result = self.single["run"](board, 2, 0.25, output.append, delays.append)
        self.assertEqual(result, {"status": "completed", "grid": [[False]], "generations": 2})
        self.assertEqual(output, ["Generation 0\n", "O\n", "Generation 1\n", "-\n",
                                  "Generation 2\n", "-\n"])
        self.assertEqual(delays, [0.25, 0.25])
        self.assertEqual(board, [[True]])
        zero = self.single["run"](board, 0, output_fn=lambda text: None)
        self.assertIsNot(zero["grid"][0], board[0])
        self.assertEqual(zero["generations"], 0)
        with redirect_stdout(io.StringIO()) as stream:
            self.single["run"]([[False]], 1)
        self.assertEqual(stream.getvalue(), "Generation 0\n-\nGeneration 1\n-\n")

    def test_continuous_single_run_can_be_cancelled_without_false_completion(self):
        delays = []
        def stop(delay):
            delays.append(delay)
            if len(delays) == 3:
                raise KeyboardInterrupt
        result = self.single["run"]([[True]], None, 0.1, lambda text: None, stop)
        self.assertEqual(result, {"status": "cancelled", "grid": [[False]], "generations": 2})
        def callback(text):
            raise RuntimeError("callback failed")
        with self.assertRaises(RuntimeError):
            self.single["run"]([[False]], output_fn=callback)

    def test_single_configuration_is_checked_before_opening(self):
        for settings in ({"generations": True}, {"generations": -1}, {"delay": True},
                         {"delay": float("inf")}, {"delay": float("nan")},
                         {"delay": -0.1}, {"delay": 10 ** 1000}, {"sleep_fn": 3}, {"output_fn": 3}):
            with patch("builtins.open", side_effect=AssertionError("opened")), self.assertRaises(ValueError):
                self.single["main"]("missing.in", **settings)

    def test_single_main_and_legacy_direct_run_read_local_default_assets(self):
        for file in ("main.py", SINGLE + ".py"):
            result = subprocess.run([sys.executable, "-B", file], cwd=ROOT / SINGLE / "solution",
                                    capture_output=True, text=True, timeout=5, check=True)
            self.assertIn("Generation 5", result.stdout)
            self.assertEqual(result.stderr, "")
        output = []
        result = self.single["main"](ROOT / SINGLE / "solution/square.in", generations=2,
                                     output_fn=output.append)
        self.assertEqual(result["grid"], self.single["make_grid"](
            self.single["read_coordinates"](ROOT / SINGLE / "solution/square.in")))
        self.assertEqual(result["generations"], 2)

    def test_moves_validate_both_choices_before_mutation(self):
        board = [[1, 0], [0, 2]]
        self.assertEqual(self.multi["parse_move"](" +0 1\r\n", 2, 2), (0, 1))
        for bad in ("", "0, 1", "2 0", "0 1\n1 0", None):
            with self.assertRaises(ValueError):
                self.multi["parse_move"](bad, 2, 2)
        for player, grow, kill in ((True, (0, 1), (1, 1)), (3, (0, 1), (1, 1)),
                                   (1, (0, 0), (1, 1)), (1, (0, 1), (0, 0)),
                                   (1, (0, 1), (1, 0)), (1, (0, 1), (2, 2))):
            with self.assertRaises(ValueError):
                self.multi["apply_turn"](board, player, grow, kill)
            self.assertEqual(board, [[1, 0], [0, 2]])
        result = self.multi["apply_turn"](board, 1, (0, 1), (1, 1))
        self.assertEqual(result, [[1, 1], [0, 0]])
        self.assertIsNot(result[0], board[0])
        result[1][0] = 2
        self.assertEqual(board, [[1, 0], [0, 2]])

    def test_initial_extinction_and_zero_limit_do_not_prompt(self):
        for board, state in (([[1]], "o_wins"), ([[2]], "x_wins"), ([[0]], "draw")):
            result = self.multi["play"](board, input_fn=lambda prompt: self.fail("prompted"),
                                        output_fn=lambda text: None)
            self.assertEqual(result["status"], state)
            self.assertEqual(result["turns"], 0)
            self.assertEqual(result["next_player"], 1)
        result = self.multi["play"]([[1, 2]], 0, lambda prompt: self.fail("prompted"),
                                    lambda text: None)
        self.assertEqual(result["status"], "limit")
        self.assertEqual(result["grid"], [[1, 2]])

    def test_post_edit_win_precedes_generation(self):
        output = []
        result = self.multi["play"]([[1, 0], [0, 2]], input_fn=scripted(["0 1", "1 1"]),
                                    output_fn=output.append)
        self.assertEqual(result, {"status": "o_wins", "grid": [[1, 1], [0, 0]],
                                  "turns": 1, "next_player": 2})
        self.assertNotIn("After generation", "".join(output))

    def test_turn_order_is_edits_then_generation_and_alternates_not_counts(self):
        board = self.multi["make_grid"]([(1, 1), (1, 2), (2, 1), (2, 2)],
                                        [(1, 5), (1, 6), (2, 5), (2, 6)], 4, 8)
        edited = deepcopy(board)
        edited[0][0], edited[1][5] = 1, 0
        first = oracle(edited, owned=True)
        grow = next((r, c) for r in range(4) for c in range(8) if first[r][c] == 0)
        kill = next((r, c) for r in range(4) for c in range(8) if first[r][c] == 1)
        second = deepcopy(first)
        second[grow[0]][grow[1]], second[kill[0]][kill[1]] = 2, 0
        expected = oracle(second, owned=True)
        prompts, output = [], []
        result = self.multi["play"](board, 2, scripted(["0 0", "1 5",
                                    f"{grow[0]} {grow[1]}", f"{kill[0]} {kill[1]}"], prompts),
                                    output.append)
        self.assertEqual(result["grid"], expected)
        self.assertEqual(result["turns"], 2)
        self.assertEqual(result["next_player"], 1)
        self.assertEqual([p.split(":")[0] for p in prompts], ["Player O", "Player O", "Player X", "Player X"])
        text = "".join(output)
        self.assertLess(text.index("After Player O's edits"), text.index("After generation 1"))
        self.assertLess(text.index("After generation 1"), text.index("After Player X's edits"))
        self.assertEqual(board, self.multi["make_grid"](
            [(1, 1), (1, 2), (2, 1), (2, 2)], [(1, 5), (1, 6), (2, 5), (2, 6)], 4, 8))

    def test_invalid_turns_retry_same_player_and_preserve_board(self):
        board = [[1, 0], [0, 2]]
        prompts, output = [], []
        result = self.multi["play"](board, 1, scripted(
            ["bad", "0 0", "1 1", "0 1", "0 0", "0 1", "1 1"], prompts), output.append)
        self.assertEqual(result["status"], "o_wins")
        self.assertEqual(result["turns"], 1)
        self.assertTrue(all(p.startswith("Player O") for p in prompts))
        self.assertEqual("".join(output).count("Invalid turn"), 3)
        self.assertEqual(board, [[1, 0], [0, 2]])

    def test_quit_eof_and_interrupt_at_either_prompt_have_no_winner(self):
        board = [[1, 0], [0, 2]]
        for answer in ("  QuIt ", EOFError(), KeyboardInterrupt()):
            for answers in ([answer], ["0 1", answer]):
                output = []
                result = self.multi["play"](board, input_fn=scripted(answers), output_fn=output.append)
                self.assertEqual(result, {"status": "cancelled", "grid": board, "turns": 0, "next_player": 1})
                self.assertIsNot(result["grid"][0], board[0])
                self.assertNotIn("wins", "".join(output))

    def test_post_generation_draw_and_single_owner_win(self):
        result = self.multi["play"]([[1, 0, 0, 2, 2]], input_fn=scripted(["0 1", "0 3"]),
                                    output_fn=lambda text: None)
        self.assertEqual(result["status"], "draw")
        self.assertEqual(result["grid"], [[0, 0, 0, 0, 0]])
        board = self.multi["make_grid"]([(1, 1), (1, 2), (2, 1), (2, 2)],
                                        [(0, 6), (0, 7)], 5, 8)
        result = self.multi["play"](board, input_fn=scripted(["4 7", "0 6"]),
                                    output_fn=lambda text: None)
        self.assertEqual(result["status"], "o_wins")
        self.assertEqual(self.multi["count_board"](result["grid"]), [4, 0])

    def test_full_board_pass_advances_generation_without_input(self):
        board = [[1, 2], [2, 1]]
        output = []
        result = self.multi["play"](board, 1, lambda prompt: self.fail("prompted"), output.append)
        self.assertEqual(result, {"status": "limit", "grid": board, "turns": 1, "next_player": 2})
        self.assertIn("passes", "".join(output))
        self.assertIn("After generation 1", "".join(output))
        self.assertNotIn("wins", "".join(output))

    def test_owned_configuration_and_unexpected_callback_errors(self):
        for settings in ({"max_turns": True}, {"max_turns": -1}, {"max_turns": 1.2},
                         {"input_fn": 3}, {"output_fn": 3}):
            with patch("builtins.open", side_effect=AssertionError("opened")), self.assertRaises(ValueError):
                self.multi["main"]("missing", "missing2", **settings)
        for error in (RuntimeError("input failed"), ValueError("input callback failed")):
            with self.assertRaises(type(error)):
                self.multi["play"]([[1, 0, 2]], input_fn=scripted([error]), output_fn=lambda text: None)
        def bad_output(text):
            raise RuntimeError("output failed")
        with self.assertRaises(RuntimeError):
            self.multi["play"]([[1, 0, 2]], output_fn=bad_output)
        result = self.multi["play"]([[1, 0, 2]], None, scripted(["quit"]), lambda text: None)
        self.assertEqual(result["status"], "cancelled")

    def test_owned_default_callbacks_main_and_direct_legacy_entry_points(self):
        with patch("builtins.input", return_value="quit"), redirect_stdout(io.StringIO()) as output:
            result = self.multi["main"](ROOT / MULTI / "solution/player1.in",
                                        ROOT / MULTI / "solution/player2.in")
        self.assertEqual(result["status"], "cancelled")
        self.assertIn("Player O has 5", output.getvalue())
        for filename in ("main.py", MULTI + ".py"):
            result = subprocess.run([sys.executable, "-B", filename],
                                    cwd=ROOT / MULTI / "solution", input="quit\n",
                                    capture_output=True, text=True, timeout=5, check=True)
            self.assertIn("Cancelled; no winner", result.stdout)
            self.assertNotIn("wins", result.stdout)
            self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
