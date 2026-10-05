"""Independent oracles for the three migrated fundamentals practice packs."""

import ast
from collections import Counter
import contextlib
import inspect
import io
from itertools import combinations, permutations, product
import math
from pathlib import Path
import runpy
import subprocess
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PACKS = {
    "AM2-Functions-Practice": (
        "product", "average", "count_letter", "count_seven",
        "exponent", "factorial", "hailstone"
    ),
    "AM2-Lists-Practice": (
        "make_numbers", "make_evens", "make_squares", "sum_lists", "minimum",
        "maximum", "sum_list_of_lists", "flatten_list", "max_list"
    ),
    "AM3-Python-Fundamentals-Problem-Set": (
        "double", "starts_with_a", "num_of_evens", "sum_of_numbers",
        "index_of_largest_number", "all_squares", "largest_power_of_two",
        "factorial_sum", "largest_divisor", "largest_product", "sums_to_zero",
        "most_common_numbers", "reverse_string", "count_vowels", "count_pairs",
        "swap_min_max"
    ),
}


def load(project, role="solution"):
    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch(
        "builtins.input", side_effect=AssertionError("Import requested input")
    ), patch("time.sleep", side_effect=AssertionError("Import slept")):
        module = runpy.run_path(str(ROOT / project / role / "main.py"))
    if output.getvalue():
        raise AssertionError("Import ran demonstrations")
    return module


def exact_hailstone_length(n):
    terms = 1
    for _ in range(10000):
        if n == 1:
            return terms
        n = n >> 1 if n % 2 == 0 else 3 * n + 1
        terms += 1
    raise AssertionError("Independent bounded oracle did not reach one")


class FundamentalsPackTests(unittest.TestCase):
    def test_starters_are_distinct_incomplete_and_import_safe(self):
        for project, names in PACKS.items():
            starter, reference = load(project, "starter"), load(project)
            source = (ROOT / project / "starter/main.py").read_text()
            self.assertNotEqual(source, (ROOT / project / "solution/main.py").read_text())
            definitions = {
                n.name: n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)
            }
            self.assertEqual(set(definitions), set(names))
            for name in names:
                with self.subTest(project=project, function=name):
                    self.assertEqual(inspect.signature(starter[name]), inspect.signature(reference[name]))
                    body = definitions[name].body
                    self.assertEqual(len(body), 2)
                    self.assertIsInstance(body[0], ast.Expr)
                    self.assertIsInstance(body[0].value.value, str)
                    self.assertIsInstance(body[1], ast.Raise)
                    with self.assertRaises(NotImplementedError):
                        starter[name](*([1] * len(inspect.signature(starter[name]).parameters)))
            result = subprocess.run(
                [sys.executable, "-B", str(ROOT / project / "starter/main.py")],
                capture_output=True, text=True, timeout=5, check=True
            )
            self.assertIn("Implement ", result.stdout)
            self.assertEqual(result.stderr, "")

    def test_arithmetic_functions_match_independent_numeric_oracles(self):
        module = load("AM2-Functions-Practice")
        for a, b, c in product(range(-3, 4), repeat=3):
            self.assertEqual(module["product"](a, b, c), math.prod((a, b, c)))
            self.assertEqual(module["average"](a, b), (a + b) / 2)
        self.assertEqual(module["product"](1.5, -2, 0.5), -1.5)
        self.assertEqual(module["average"](-0.5, 1.5), 0.5)
        for a in (-3, -1, 0, 1, 2, 1.5):
            for b in range(8):
                self.assertEqual(module["exponent"](a, b), a ** b)
        for n in range(13):
            self.assertEqual(module["factorial"](n), math.factorial(n))

    def test_letter_and_integer_digit_contracts(self):
        module = load("AM2-Functions-Practice")
        for word in ("", "bookkeeper", "aAa", "7 77", "!?"):
            for letter in ("a", "A", "e", "7", " ", "!"):
                self.assertEqual(module["count_letter"](word, letter), word.count(letter))
        for n in (0, 7, -7, 177877, -707, 2 ** 60 + 7):
            self.assertEqual(module["count_seven"](n), str(abs(n)).count("7"))
        # This also avoids Python's optional int-to-string digit-count limit.
        self.assertEqual(module["count_seven"](7 * 10 ** 5000 + 7), 2)
        for args in (("abc", ""), ("abc", "ab"), ("abc", 1), (1, "a")):
            with self.assertRaises(ValueError):
                module["count_letter"](*args)
        for n in (True, 7.0, "7", None):
            with self.assertRaises(ValueError):
                module["count_seven"](n)

    def test_integer_exponent_factorial_and_hailstone_domains(self):
        module = load("AM2-Functions-Practice")
        for bad in (-1, 0.5, True, "2", None):
            with self.assertRaises(ValueError):
                module["exponent"](2, bad)
            with self.assertRaises(ValueError):
                module["factorial"](bad)
        for bad in (0, -1, 1.5, True, "2", None):
            with self.assertRaises(ValueError):
                module["hailstone"](bad)
        for bad in (-1, 1.5, True, "2", None):
            with self.assertRaises(ValueError):
                module["hailstone"](1, bad)

    def test_hailstone_uses_exact_integer_terms_and_bounded_transitions(self):
        hailstone = load("AM2-Functions-Practice")["hailstone"]
        for n in range(1, 201):
            expected = exact_hailstone_length(n)
            self.assertEqual(hailstone(n), expected)
            self.assertEqual(hailstone(n, expected - 1), expected)
            if expected > 1:
                with self.assertRaises(RuntimeError):
                    hailstone(n, expected - 2)
        self.assertEqual(exact_hailstone_length(18014398509481986), 412)
        self.assertEqual(hailstone(18014398509481986), 412)
        self.assertEqual(hailstone(1, 0), 1)
        self.assertEqual(hailstone(10, 6), 7)
        with self.assertRaises(RuntimeError):
            hailstone(2, 0)

    def test_generated_lists_have_exact_counts_and_fresh_identity(self):
        project = "AM2-Lists-Practice"
        module = load(project)
        expected = {
            "make_numbers": list(range(1, 21)),
            "make_evens": list(range(2, 41, 2)),
            "make_squares": [n ** 2 for n in range(1, 11)],
        }
        source = ast.parse((ROOT / project / "solution/main.py").read_text())
        definitions = {n.name: n for n in source.body if isinstance(n, ast.FunctionDef)}
        for name, values in expected.items():
            first, second = module[name](), module[name]()
            self.assertEqual(first, values)
            self.assertEqual(second, values)
            self.assertIsNot(first, second)
            first.append(999)
            self.assertEqual(second, values)
            self.assertTrue(any(isinstance(n, ast.For) for n in ast.walk(definitions[name])))

    def test_list_sums_and_extrema_exhaustive_bounded_inputs(self):
        module = load("AM2-Lists-Practice")
        cases = [list(v) for n in range(5) for v in product((-2, 0, 3), repeat=n)]
        for left in cases:
            saved = left.copy()
            if left:
                self.assertEqual(module["minimum"](left), min(left))
                self.assertEqual(module["maximum"](left), max(left))
            else:
                for name in ("minimum", "maximum"):
                    with self.assertRaises(ValueError):
                        module[name](left)
            for right in cases:
                other = right.copy()
                self.assertEqual(module["sum_lists"](left, right), sum(left) + sum(right))
                self.assertEqual(right, other)
            self.assertEqual(left, saved)

    def test_nested_list_empty_skip_order_and_mutation_policies(self):
        module = load("AM2-Lists-Practice")
        for nested in ([], [[]], [[], []], [[-5]], [[2, 2], [], [-7, -1], [0]]):
            saved = [inner.copy() for inner in nested]
            flat = [x for inner in nested for x in inner]
            self.assertEqual(module["sum_list_of_lists"](nested), sum(flat))
            result = module["flatten_list"](nested)
            self.assertEqual(result, flat)
            self.assertIsNot(result, nested)
            maxima = module["max_list"](nested)
            self.assertEqual(maxima, [max(inner) for inner in nested if inner])
            self.assertIsNot(maxima, nested)
            self.assertEqual(nested, saved)
        # The exercise implementations must use loops rather than ready-made helpers.
        tree = ast.parse((ROOT / "AM2-Lists-Practice/solution/main.py").read_text())
        functions = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
        self.assertFalse(any(
            isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            and n.func.id in ("sum", "min", "max")
            for f in functions for n in ast.walk(f)
        ))

    def test_fundamentals_numeric_functions_on_all_small_lists(self):
        module = load("AM3-Python-Fundamentals-Problem-Set")
        cases = [list(v) for n in range(6) for v in product((-2, 0, 3), repeat=n)]
        for values in cases:
            saved = values.copy()
            frequencies = Counter(values)
            modes = sorted(k for k, v in frequencies.items() if v == max(frequencies.values())) if frequencies else []
            doubled = module["double"](values)
            self.assertEqual(doubled, [2 * n for n in values])
            self.assertIsNot(doubled, values)
            self.assertEqual(module["num_of_evens"](values), sum(n % 2 == 0 for n in values))
            self.assertEqual(module["sum_of_numbers"](values), sum(values))
            self.assertEqual(module["sums_to_zero"](values), any(a + b == 0 for a, b in combinations(values, 2)))
            result = module["most_common_numbers"](values)
            self.assertEqual(result, modes)
            self.assertIsNot(result, values)
            self.assertEqual(module["count_pairs"](values), sum(v == 2 for v in frequencies.values()))
            if len(values) >= 2:
                self.assertEqual(module["largest_product"](values), max(a * b for a, b in combinations(values, 2)))
            self.assertEqual(values, saved)
        self.assertEqual(module["most_common_numbers"]([3, 6, 2, 2, 6]), [2, 6])
        self.assertFalse(module["sums_to_zero"]([0]))
        self.assertTrue(module["sums_to_zero"]([0, 0]))
        self.assertEqual(module["largest_product"]([-3, -8, 10]), 24)

    def test_distinct_largest_index_and_in_place_swap(self):
        module = load("AM3-Python-Fundamentals-Problem-Set")
        for n in range(1, 5):
            for values in permutations((-3, 0, 2, 5), n):
                working = list(values)
                original = working.copy()
                self.assertEqual(module["index_of_largest_number"](working), original.index(max(original)))
                self.assertEqual(working, original)
                expected = original.copy()
                low, high = original.index(min(original)), original.index(max(original))
                expected[low], expected[high] = expected[high], expected[low]
                self.assertIs(module["swap_min_max"](working), working)
                self.assertEqual(working, expected)

    def test_integer_tasks_match_exact_oracles_and_print_contract(self):
        module = load("AM3-Python-Fundamentals-Problem-Set")
        for n in range(40):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertIsNone(module["all_squares"](n))
            self.assertEqual(output.getvalue(), "".join(str(i * i) + "\n" for i in range(math.isqrt(n) + 1)))
        for n in list(range(1, 130)) + [2 ** 60 - 1, 2 ** 60, 2 ** 60 + 7]:
            self.assertEqual(module["largest_power_of_two"](n), n.bit_length() - 1)
        for n in range(13):
            self.assertEqual(module["factorial_sum"](n), sum(math.factorial(i) for i in range(1, n + 1)))
        for n in range(1, 101):
            self.assertEqual(module["largest_divisor"](n), max((d for d in range(1, n) if n % d == 0), default=None))

    def test_fundamentals_rejects_unsupported_domains_deliberately(self):
        module = load("AM3-Python-Fundamentals-Problem-Set")
        for name in ("all_squares", "largest_power_of_two", "factorial_sum", "largest_divisor"):
            for bad in (-1, 1.5, True, "2", None):
                with self.assertRaises(ValueError):
                    module[name](bad)
        for name in ("largest_power_of_two", "largest_divisor"):
            with self.assertRaises(ValueError):
                module[name](0)
        for name in ("index_of_largest_number", "swap_min_max"):
            for bad in ([], [1, 1]):
                saved = bad.copy()
                with self.assertRaises(ValueError):
                    module[name](bad)
                self.assertEqual(bad, saved)
        for bad in ([], [3]):
            with self.assertRaises(ValueError):
                module["largest_product"](bad)

    def test_string_case_empty_and_character_policies(self):
        module = load("AM3-Python-Fundamentals-Problem-Set")
        words = ["", "a", "Apple", "apple", "ant", "banana", " a"]
        result = module["starts_with_a"](words)
        self.assertEqual(result, ["a", "apple", "ant"])
        self.assertIsNot(result, words)
        self.assertEqual(words, ["", "a", "Apple", "apple", "ant", "banana", " a"])
        for text in ("", "Hello, World!", "aAeEiIoOuUyY", "Áé y", "  ?"):
            self.assertEqual(module["reverse_string"](text), text[::-1])
            self.assertEqual(module["count_vowels"](text), sum(c in "aAeEiIoOuU" for c in text))

    def test_complete_briefs_and_direct_run_references(self):
        for project, names in PACKS.items():
            brief = (ROOT / project / "starter/README.md").read_text()
            for name in names:
                self.assertIn(name + "(", brief)
            self.assertIn("separate", brief)
            result = subprocess.run(
                [sys.executable, "-B", str(ROOT / project / "solution/main.py")],
                capture_output=True, text=True, timeout=5, check=True
            )
            self.assertTrue(result.stdout)
            self.assertEqual(result.stderr, "")
        functions = (ROOT / "AM2-Functions-Practice/starter/README.md").read_text()
        self.assertIn("## Optional challenges", functions)
        self.assertIn("General convergence is not", functions)
        fundamentals = (ROOT / "AM3-Python-Fundamentals-Problem-Set/starter/README.md").read_text()
        numbered = [line.split(".")[0] for line in fundamentals.splitlines() if line.split(".")[0].isdigit()]
        self.assertEqual(numbered, [str(n) for n in range(1, 17)])


if __name__ == "__main__":
    unittest.main()
