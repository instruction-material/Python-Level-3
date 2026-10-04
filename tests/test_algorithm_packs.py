"""Verify authored exercise scaffolds separately from reference implementations."""

import ast
import contextlib
import inspect
import io
from pathlib import Path
import runpy
import subprocess
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = {
    "AM4-Recursive-Factorials": ("recursive_factorial",),
    "AM4-Recursive-Exponents": ("exponent",),
    "AM4-Fibonacci-Numbers": ("fibonacci",),
    "AM4-Binary-Converter": ("to_binary_iterative", "to_binary_recursive"),
    "AM6-Linear-Search": ("linear_search",),
    "AM7-Binary-Search": ("bin_search_iter", "bin_search_recur"),
}


def load_module(project, role):
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout), patch(
        "builtins.input", side_effect=AssertionError("Import must not request input.")
    ):
        module = runpy.run_path(str(ROOT / project / role / "main.py"))
    if stdout.getvalue():
        raise AssertionError("Import must not print a demonstration.")
    return module


class AlgorithmPackTests(unittest.TestCase):
    def test_starters_remain_distinct_incomplete_exercises(self):
        for project, names in CONTRACTS.items():
            with self.subTest(project=project):
                starter_path = ROOT / project / "starter" / "main.py"
                solution_path = ROOT / project / "solution" / "main.py"
                starter_source = starter_path.read_text()
                self.assertNotEqual(starter_source, solution_path.read_text())
                starter = load_module(project, "starter")
                solution = load_module(project, "solution")
                definitions = {
                    node.name: node
                    for node in ast.parse(starter_source).body
                    if isinstance(node, ast.FunctionDef)
                }
                for name in names:
                    self.assertEqual(
                        inspect.signature(starter[name]), inspect.signature(solution[name])
                    )
                    # No hidden completed algorithm is placed before the exercise.
                    body = definitions[name].body
                    self.assertEqual(len(body), 2)
                    self.assertIsInstance(body[0], ast.Expr)
                    self.assertIsInstance(body[0].value, ast.Constant)
                    self.assertIsInstance(body[0].value.value, str)
                    self.assertIsInstance(body[1], ast.Raise)
                    arguments = [1] * len(inspect.signature(starter[name]).parameters)
                    with self.assertRaises(NotImplementedError):
                        starter[name](*arguments)

    def test_all_starters_run_with_exercise_feedback(self):
        for project in CONTRACTS:
            with self.subTest(project=project):
                completed = subprocess.run(
                    [sys.executable, "-B", str(ROOT / project / "starter" / "main.py")],
                    capture_output=True,
                    text=True,
                    timeout=5,
                    check=True,
                )
                self.assertIn("Implement ", completed.stdout)
                self.assertEqual(completed.stderr, "")

    def test_factorial_reference(self):
        factorial = load_module("AM4-Recursive-Factorials", "solution")["recursive_factorial"]
        for value, expected in ((0, 1), (1, 1), (2, 2), (5, 120), (8, 40320)):
            with self.subTest(value=value):
                self.assertEqual(factorial(value), expected)

    def test_exponent_reference(self):
        exponent = load_module("AM4-Recursive-Exponents", "solution")["exponent"]
        for base in (-3, -1, 0, 1, 2, 5):
            for power in range(8):
                with self.subTest(base=base, power=power):
                    self.assertEqual(exponent(base, power), base**power)

    def test_fibonacci_uses_one_based_positions(self):
        fibonacci = load_module("AM4-Fibonacci-Numbers", "solution")["fibonacci"]
        for position, expected in enumerate((0, 1, 1, 2, 3, 5, 8, 13, 21, 34), start=1):
            with self.subTest(position=position):
                self.assertEqual(fibonacci(position), expected)

    def test_binary_references_preserve_large_integer_digits(self):
        module = load_module("AM4-Binary-Converter", "solution")
        values = list(range(256)) + [2**53 + 7, 2**60 + 7, 2**80 + 19, 2**256 - 1]
        for name in CONTRACTS["AM4-Binary-Converter"]:
            for value in values:
                with self.subTest(function=name, value=value):
                    self.assertEqual(module[name](value), bin(value)[2:])

    def test_linear_search_reference(self):
        search = load_module("AM6-Linear-Search", "solution")["linear_search"]
        for values in ([], [1], [1, 2, 3], [3, 1, 3, 2], ["a", "b", "a"]):
            for target in (0, 1, 2, 3, 4, "a", "b", "z"):
                original = values[:]
                with self.subTest(values=values, target=target):
                    self.assertIs(search(values, target), target in values)
                    self.assertEqual(values, original)

    def test_binary_search_references(self):
        module = load_module("AM7-Binary-Search", "solution")
        for name in CONTRACTS["AM7-Binary-Search"]:
            for values in ([], [1], [1, 4], [1, 4, 5, 8], [-5, -2, 0, 4, 4, 9]):
                for target in range(-6, 11):
                    original = values[:]
                    with self.subTest(function=name, values=values, target=target):
                        self.assertIs(module[name](values, target), target in values)
                        self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
