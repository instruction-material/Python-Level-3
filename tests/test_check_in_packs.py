"""Independent check-in oracles, preserved problem code and explicit file workflows."""

import ast
from collections import Counter
import contextlib
import inspect
import io
from itertools import product
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PACKS = {
    "AM-Check-In-1": ("middle_letters", "second_word", "num_pins", "lucas", "make_word", "main"),
    "AM-Check-In-2": ("selectionSort", "insertionSort", "linear_search",
                      "bin_search_iter", "bin_search_recur", "first_one_index"),
    "AM-Check-In-2-Additional-Project": (
        "selection_sort2", "insertion_sort2", "make_workloads", "time_sort", "benchmark"),
    "AM-Check-In-3": ("merge", "partition", "bubble_sort", "write_letters",
                      "read_letter_counts", "main"),
    "AM-Check-In-3-Additional-Project": (
        "read_letters", "sort_letters", "write_letters", "sort_file"),
}


def load(pack, role="solution"):
    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch(
        "builtins.input", side_effect=AssertionError("Import requested input")
    ), patch("time.sleep", side_effect=AssertionError("Import slept")), patch(
        "builtins.open", side_effect=AssertionError("Import opened coursework data")
    ), patch.object(Path, "open", side_effect=AssertionError("Import opened a Path")):
        module = runpy.run_path(str(ROOT / pack / role / "main.py"))
    if output.getvalue():
        raise AssertionError("Import printed or ran a demonstration")
    return module


class IndexedSequence:
    """Large virtual sequence; scans, iteration and slicing are forbidden."""

    def __init__(self, size, boundary=None):
        self.size, self.boundary, self.accesses = size, boundary, 0

    def __len__(self):
        return self.size

    def __iter__(self):
        raise AssertionError("Search iterated or copied the input")

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise AssertionError("Search sliced the input")
        if not 0 <= index < self.size:
            raise AssertionError("Search indexed outside its bounds")
        self.accesses += 1
        return index if self.boundary is None else int(index >= self.boundary)


class Record:
    def __init__(self, value, label):
        self.value, self.label = value, label

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value


class CheckInTests(unittest.TestCase):
    def test_starters_are_incomplete_distinct_import_safe_and_signature_matched(self):
        for pack, names in PACKS.items():
            path = ROOT / pack / "starter/main.py"
            source = path.read_text()
            self.assertNotEqual(source, (ROOT / pack / "solution/main.py").read_text())
            starter, reference = load(pack, "starter"), load(pack)
            definitions = {n.name: n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)}
            for name in names:
                with self.subTest(pack=pack, function=name):
                    self.assertEqual(inspect.signature(starter[name]), inspect.signature(reference[name]))
                    body = definitions[name].body
                    self.assertEqual(len(body), 2)
                    self.assertIsInstance(body[0].value.value, str)
                    self.assertIsInstance(body[1], ast.Raise)
                    with self.assertRaises(NotImplementedError):
                        starter[name](*([1] * len(inspect.signature(starter[name]).parameters)))
            result = subprocess.run(
                [sys.executable, "-B", str(path)], capture_output=True, text=True,
                check=True, timeout=5
            )
            self.assertIn("Implement ", result.stdout)
            self.assertEqual(result.stderr, "")
            self.assertGreater(len((path.parent / "README.md").read_text()), 1000)

    def test_supplied_problem_bodies_match_the_original_source_fixture(self):
        fixture = json.loads((ROOT / "tests/fixtures/check-in-provided-code.json").read_text())
        self.assertEqual(fixture["sourceRevision"], "6ed2caf76313b92163e3c450f6bd7192e518b9a5")
        self.assertEqual(len(fixture["functions"]), 5)
        for row in fixture["functions"]:
            original = ast.parse(row["source"]).body[0]
            current = next(n for n in ast.parse(
                (ROOT / row["path"]).read_text()
            ).body if isinstance(n, ast.FunctionDef) and n.name == original.name)
            self.assertEqual(ast.dump(current), ast.dump(original))
            self.assertNotIn("# ANSWER:", (ROOT / row["path"]).read_text())

    def test_strings_recursion_domains_and_compatibility_names(self):
        module = load("AM-Check-In-1")
        for word in ("", "a", "ab", "hello", " A! ", "ébc"):
            self.assertEqual(module["middle_letters"](word), word[1:-1])
        self.assertEqual(module["second_word"]("  one\t two   three "), "two")
        for invalid in ("", "one", "  one \t", 1, None):
            with self.assertRaises(ValueError):
                module["second_word"](invalid)
        for invalid in (1, None, False):
            with self.assertRaises(ValueError):
                module["middle_letters"](invalid)
        for rows in range(101):
            self.assertEqual(module["num_pins"](rows), rows * (rows + 1) // 2)
        previous, current = 2, 1
        for n in range(1, 19):
            self.assertEqual(module["lucas"](n), previous)
            previous, current = current, previous + current
        for invalid in (-1, 1.5, True, None):
            with self.assertRaises(ValueError):
                module["num_pins"](invalid)
            with self.assertRaises(ValueError):
                module["lucas"](invalid)
        with self.assertRaises(ValueError):
            module["lucas"](0)
        self.assertIs(module["makeWord"], module["make_word"])
        self.assertIs(module["strangeFunction"], module["strange_function"])

    def test_backspace_all_small_strings_and_literal_characters(self):
        module = load("AM-Check-In-1")
        cases = ["".join(chars) for n in range(8) for chars in product("Ab#", repeat=n)]
        cases += [" #a ##", "é#😃", "hi#", "ok##", "ti#ger", "t###"]
        for text in cases:
            expected = ""
            for character in text:
                expected = expected[:-1] if character == "#" else expected + character
            self.assertEqual(module["make_word"](text), expected)
        for invalid in (None, 1, False):
            with self.assertRaises(ValueError):
                module["make_word"](invalid)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            module["strangeFunction"](4)
        self.assertEqual(output.getvalue(), "4\n3\n2\n1\n2\n")

    def test_review_console_workflow_has_no_import_interaction(self):
        module = load("AM-Check-In-1")
        output = io.StringIO()
        with patch("builtins.input", side_effect=["hello", "one two three"]), patch(
            "random.randint", return_value=8
        ), contextlib.redirect_stdout(output):
            module["main"]()
        text = output.getvalue()
        self.assertIn("The middle letters: ell", text)
        self.assertIn("The second word of the sentence: two", text)
        self.assertIn("[1, 2, 3, 4, 5, 8]", text)
        self.assertTrue(text.endswith("[1, 2, 3, 4, 5]\n"))

    def test_search_membership_all_small_lists_and_first_one_boundaries(self):
        module = load("AM-Check-In-2")
        for n in range(6):
            for values in product((-1, 0, 1), repeat=n):
                unordered, ordered = list(values), sorted(values)
                for target in range(-2, 3):
                    self.assertIs(module["linear_search"](unordered, target), target in values)
                    for name in ("bin_search_iter", "bin_search_recur"):
                        self.assertIs(module[name](ordered, target), target in values)
                self.assertEqual(unordered, list(values))
                self.assertEqual(ordered, sorted(values))
        for n in range(129):
            for first in range(n + 1):
                values = [0] * first + [1] * (n - first)
                original = values.copy()
                self.assertEqual(module["first_one_index"](values), first if first < n else -1)
                self.assertEqual(values, original)

    def test_indexed_searches_are_logarithmic_without_scan_copy_or_slice(self):
        module = load("AM-Check-In-2")
        for size in (0, 1, 2, 3, 17, 1024, 1048576):
            for boundary in set((0, size // 2, max(0, size - 1), size)):
                sequence = IndexedSequence(size, boundary)
                expected = boundary if boundary < size else -1
                self.assertEqual(module["first_one_index"](sequence), expected)
                self.assertLessEqual(sequence.accesses, size.bit_length() + 2)
            for target in (-1, 0, size // 2, size - 1, size):
                for name in ("bin_search_iter", "bin_search_recur"):
                    sequence = IndexedSequence(size)
                    self.assertIs(module[name](sequence, target), 0 <= target < size)
                    self.assertLessEqual(sequence.accesses, 2 * size.bit_length() + 2)

    def test_sort_directions_identity_empty_cases_and_stable_insertions(self):
        review = load("AM-Check-In-2")
        experiment = load("AM-Check-In-2-Additional-Project")
        advanced = load("AM-Check-In-3")
        sorts = [(review["selection_sort"], True), (review["insertion_sort"], False),
                 (experiment["selection_sort2"], False), (experiment["insertion_sort2"], False),
                 (advanced["bubble_sort"], False), (advanced["bubbleSort"], False)]
        for n in range(6):
            for values in product((-1, 0, 1), repeat=n):
                for function, descending in sorts:
                    working = list(values)
                    self.assertIs(function(working), working)
                    self.assertEqual(working, sorted(values, reverse=descending))
        self.assertIs(review["selectionSort"], review["selection_sort"])
        self.assertIs(review["insertionSort"], review["insertion_sort"])
        for function in (review["insertion_sort"], experiment["insertion_sort2"], advanced["bubble_sort"]):
            records = [Record(2, "a"), Record(1, "b"), Record(2, "c"), Record(1, "d")]
            self.assertEqual([r.label for r in function(records)], ["b", "d", "a", "c"])

    def test_pass_trace_keys_match_actual_algorithms_without_learner_answers(self):
        examples = [
            ("AM-Check-In-2", "selection_sort", [2, 5, 10, 3, 6, 1], (2,), [10, 6, 2, 3, 5, 1]),
            ("AM-Check-In-2", "insertion_sort", [3, 7, 2, 5, 10, 1], (1, 4), [2, 3, 5, 7, 10, 1]),
            ("AM-Check-In-3", "bubbleSort", [4, 8, 2, 1, 10, 0], (0, 2), [2, 1, 4, 0, 8, 10]),
        ]
        for pack, name, values, bounds, expected in examples:
            source = ROOT / pack / "solution/main.py"
            function = next(n for n in ast.parse(source.read_text()).body
                            if isinstance(n, ast.FunctionDef) and n.name == name)
            loop = next(n for n in function.body if isinstance(n, ast.For))
            loop.iter.args = [ast.Constant(n) for n in bounds]
            ast.fix_missing_locations(function)
            namespace = {}
            exec(compile(ast.Module(body=[function], type_ignores=[]), str(source), "exec"), namespace)
            self.assertEqual(namespace[name](values.copy()), expected)
            self.assertIn(str(expected), (source.parent / "README.md").read_text())
            self.assertNotIn(str(expected), (ROOT / pack / "starter/README.md").read_text())

    def test_early_cutoff_really_counts_one_sorted_pass(self):
        class Counted(Record):
            count = 0

            def __gt__(self, other):
                Counted.count += 1
                return self.value > other.value
        module = load("AM-Check-In-3")
        values = [Counted(n, str(n)) for n in range(10)]
        module["bubble_sort"](values)
        self.assertEqual(Counted.count, 9)
        Counted.count = 0
        module["bubbleSort"](values)
        self.assertEqual(Counted.count, 90)

    def test_merge_partition_mutation_identity_order_and_ties(self):
        module = load("AM-Check-In-3")
        cases = [sorted(values) for n in range(5) for values in product((-1, 0, 1), repeat=n)]
        for left in cases:
            for right in cases:
                a, b = left.copy(), right.copy()
                result = module["merge"](a, b)
                self.assertEqual(result, sorted(left + right))
                self.assertEqual((a, b), (left, right))
                self.assertIsNot(result, a)
                self.assertIsNot(result, b)
        a = [Record(1, "a"), Record(1, "b")]
        b = [Record(1, "c"), Record(2, "d")]
        self.assertEqual([r.label for r in module["merge"](a, b)], ["a", "b", "c", "d"])
        for values in cases:
            for pivot in range(-2, 3):
                original = values.copy()
                groups = module["partition"](values, pivot)
                self.assertEqual(groups, ([v for v in values if v < pivot],
                                          [v for v in values if v == pivot],
                                          [v for v in values if v > pivot]))
                self.assertEqual(values, original)
                self.assertEqual(len({id(group) for group in groups}), 3)
                self.assertTrue(all(group is not values for group in groups))

    def test_word_files_preserve_characters_counts_and_reject_malformed_records(self):
        module = load("AM-Check-In-3")
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "file.txt"
            for word in ("", "aba", "aA a!é😃"):
                self.assertIsNone(module["write_letters"](word, target))
                self.assertEqual(target.read_text(), "".join(c + "\n" for c in word))
                self.assertEqual(module["read_letter_counts"](target), dict(Counter(word)))
            target.write_bytes(b"sentinel")
            for invalid in (None, True, "a\nb", "a\rb"):
                with self.assertRaises(ValueError):
                    module["write_letters"](invalid, target)
                self.assertEqual(target.read_bytes(), b"sentinel")
            target.write_bytes(b"A\r\n \r\na")
            self.assertEqual(module["read_letter_counts"](target), {"A": 1, " ": 1, "a": 1})
            for content, number in (("\n", 1), ("ab\n", 1), ("x\n\n", 2)):
                target.write_text(content)
                with self.assertRaisesRegex(ValueError, "line " + str(number)):
                    module["read_letter_counts"](target)
            with self.assertRaises(FileNotFoundError):
                module["read_letter_counts"](Path(directory) / "missing.txt")
            target.write_text("a b\nc")
            with target.open() as stream:
                self.assertEqual(stream.read(), "a b\nc")
            with target.open() as stream:
                self.assertEqual(stream.readlines(), ["a b\n", "c"])

    def test_ascii_file_sorting_domains_fresh_lists_and_output_reopening(self):
        module = load("AM-Check-In-3-Additional-Project")
        for letters in ([], ["b", "A", "a", " ", "A"], [chr(n) for n in range(128) if n not in (10, 13)]):
            original = letters.copy()
            result = module["sort_letters"](letters)
            self.assertEqual(result, sorted(original, key=ord))
            self.assertIsNot(result, letters)
            self.assertEqual(letters, original)
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / "input.txt", Path(directory) / "output.txt"
            for data, expected in ((b"", []), (b"b\r\nA\r\n \r\nA", [" ", "A", "A", "b"])):
                source.write_bytes(data)
                self.assertEqual(module["sort_file"](source, target), expected)
                self.assertEqual(source.read_bytes(), data)
                self.assertEqual(module["read_letters"](target), expected)
                self.assertEqual(target.read_text(), "".join(c + "\n" for c in expected))
            for invalid in ([""], ["ab"], ["é"], ["\n"], [None], "abc"):
                target.write_bytes(b"sentinel")
                with self.assertRaises(ValueError):
                    module["write_letters"](invalid, target)
                self.assertEqual(target.read_bytes(), b"sentinel")
                with self.assertRaises(ValueError):
                    module["sort_letters"](invalid)

    def test_file_input_errors_and_all_input_output_aliases_preserve_bytes(self):
        module = load("AM-Check-In-3-Additional-Project")
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / "input.txt", Path(directory) / "output.txt"
            target.write_bytes(b"sentinel")
            for content, number in (("\n", 1), ("ab\n", 1), ("a\né\n", 2)):
                source.write_text(content)
                with self.assertRaisesRegex(ValueError, "line " + str(number)):
                    module["sort_file"](source, target)
                self.assertEqual(target.read_bytes(), b"sentinel")
                self.assertEqual(source.read_text(), content)
            with self.assertRaises(FileNotFoundError):
                module["sort_file"](Path(directory) / "missing.txt", target)
            self.assertEqual(target.read_bytes(), b"sentinel")
            source.write_bytes(b"b\na\n")
            aliases = [source, Path(directory) / "." / "input.txt"]
            symbolic, hard = Path(directory) / "symbolic.txt", Path(directory) / "hard.txt"
            symbolic.symlink_to(source)
            os.link(source, hard)
            aliases += [symbolic, hard]
            for alias in aliases:
                with self.assertRaises(ValueError):
                    module["sort_file"](source, alias)
                self.assertEqual(source.read_bytes(), b"b\na\n")

    def test_experiment_has_three_shared_shapes_and_deliberate_bounds(self):
        module = load("AM-Check-In-2-Additional-Project")
        for n in (0, 1, 2, 17, 2000):
            shapes = module["make_workloads"](n, 17)
            self.assertEqual(set(shapes), {"random", "sorted", "reversed"})
            self.assertEqual(shapes, module["make_workloads"](n, 17))
            self.assertEqual(shapes["sorted"], sorted(shapes["random"]))
            self.assertEqual(shapes["reversed"], shapes["sorted"][::-1])
            self.assertEqual(len({id(values) for values in shapes.values()}), 3)
            self.assertEqual(len(shapes["random"]), n)
        for n in (-1, 2001, True, 1.5):
            with self.assertRaises(ValueError):
                module["make_workloads"](n)
        for sizes, repeats in (((), 1), ((1,) * 6, 1), ((-1,), 1), ((2001,), 1),
                               ((True,), 1), ((1,), 0), ((1,), 11), ((1,), True)):
            with self.assertRaises(ValueError):
                module["benchmark"](sizes, repeats)
        for seed in (True, "abc", 1.5):
            with self.assertRaises(ValueError):
                module["benchmark"]((1,), seed=seed)
        for sorters in ({}, {"a": 1}, {"a": sorted, "b": sorted, "c": sorted}):
            with self.assertRaises(ValueError):
                module["benchmark"]((1,), sorters=sorters)

    def test_timing_excludes_copy_oracle_validation_and_detects_wrong_output(self):
        module = load("AM-Check-In-2-Additional-Project")
        events = []

        class Input(list):
            def __iter__(self):
                events.append("oracle")
                return super().__iter__()

            def copy(self):
                events.append("copy")
                return list.copy(self)

        class Result(list):
            def __ne__(self, other):
                events.append("validation")
                return super().__ne__(other)

        ticks = iter((10, 12))

        def clock():
            events.append("clock")
            return next(ticks)

        def sorter(working):
            events.append("sort")
            return Result(sorted(working))

        with patch.dict(module["time_sort"].__globals__, {"perf_counter": clock}):
            self.assertEqual(module["time_sort"](sorter, Input([2, 1])), 2)
        self.assertEqual(events, ["oracle", "copy", "clock", "sort", "clock", "validation"])
        with self.assertRaises(AssertionError):
            module["time_sort"](lambda values: values, [2, 1])
        for finish in (-1, float("nan"), float("inf")):
            with patch.dict(module["time_sort"].__globals__, {"perf_counter": iter((0, finish)).__next__}):
                with self.assertRaises(RuntimeError):
                    module["time_sort"](sorted, [2, 1])

    def test_benchmark_fresh_inputs_and_medians_of_actual_samples(self):
        module = load("AM-Check-In-2-Additional-Project")
        shapes = {"random": [2, 1, 2], "sorted": [1, 2, 2], "reversed": [2, 2, 1]}
        original = {name: values.copy() for name, values in shapes.items()}
        received, held = {"a": [], "b": []}, []

        def sorter(name):
            def run(values):
                received[name].append(values.copy())
                held.append(values)
                values.sort()
                return values
            return run

        durations = [1, 5, 3] * 6
        ticks = iter([tick for i, duration in enumerate(durations) for tick in (10*i, 10*i+duration)])
        with patch.dict(module["benchmark"].__globals__, {
            "make_workloads": lambda n, seed: shapes, "perf_counter": ticks.__next__
        }):
            rows = module["benchmark"]((3,), 3, sorters={"a": sorter("a"), "b": sorter("b")})
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(row["seconds"] == 3 and row["repeats"] == 3 for row in rows))
        self.assertEqual(received["a"], received["b"])
        self.assertEqual(received["a"], [values.copy() for values in original.values() for _ in range(3)])
        self.assertEqual(len({id(values) for values in held}), 18)
        self.assertEqual(shapes, original)

    def test_direct_reference_scripts_are_bounded_and_file_workflows_are_explicit(self):
        with tempfile.TemporaryDirectory() as directory:
            for pack, supplied in (("AM-Check-In-1", "hello\none two\n"),
                                   ("AM-Check-In-3", "aba\n")):
                result = subprocess.run(
                    [sys.executable, "-B", str(ROOT / pack / "solution/main.py")],
                    input=supplied, cwd=directory, capture_output=True, text=True,
                    timeout=5, check=True
                )
                self.assertEqual(result.stderr, "")
            self.assertEqual((Path(directory) / "file.txt").read_text(), "a\nb\na\n")
            (Path(directory) / "input.txt").write_text("b\nA\n \n")
            result = subprocess.run(
                [sys.executable, "-B", str(ROOT / "AM-Check-In-3-Additional-Project/solution/main.py")],
                cwd=directory, capture_output=True, text=True, timeout=5, check=True
            )
            self.assertEqual(result.stderr, "")
            self.assertEqual((Path(directory) / "output.txt").read_text(), " \nA\nb\n")
        for pack in ("AM-Check-In-2", "AM-Check-In-2-Additional-Project"):
            result = subprocess.run(
                [sys.executable, "-B", str(ROOT / pack / "solution/main.py")],
                capture_output=True, text=True, timeout=5, check=True
            )
            self.assertEqual(result.stderr, "")
            if "Additional" in pack:
                self.assertIn("not Big-O proof", result.stdout)
                measurements = [line for line in result.stdout.splitlines() if line.endswith(" seconds")]
                self.assertEqual(len(measurements), 12)
                self.assertTrue(all(float(line.split()[-2]) >= 0 for line in measurements))


if __name__ == "__main__":
    unittest.main()
