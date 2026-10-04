"""Verify sorting values, mutation, stability and honest experiment boundaries."""

import ast
import contextlib
import inspect
import io
from itertools import product
from pathlib import Path
import random
import runpy
import subprocess
import sys
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PACKS = {
    "AM8-Selection-Sort": ("selection_sort1", "selection_sort2"),
    "AM8-Insertion-Sort": ("insertion_sort1", "insertion_sort2"),
    "AM9-Bubble-Sort": (
        "bubble_sort_in_place", "bubble_sort_improved", "bubble_sort_copy"
    ),
    "AM10-Merge-Sort": ("merge", "split", "merge_sort", "merge_sort2"),
    "AM11-Quicksort": ("partition", "quicksort", "shuffle", "shuffle2"),
    "AM11-Sorting-Comparison": (
        "selection_sort", "insertion_sort", "bubble_sort", "merge_sort",
        "partition", "quicksort", "make_workloads", "time_sort", "benchmark"
    ),
}
SORT_MODES = {
    "AM8-Selection-Sort": {"selection_sort1": "consume", "selection_sort2": "inplace"},
    "AM8-Insertion-Sort": {"insertion_sort1": "copy", "insertion_sort2": "inplace"},
    "AM9-Bubble-Sort": {
        "bubble_sort_in_place": "inplace", "bubble_sort_improved": "inplace",
        "bubble_sort_copy": "copy"
    },
    "AM10-Merge-Sort": {"merge_sort": "copy", "merge_sort2": "copy"},
    "AM11-Quicksort": {"quicksort": "copy"},
    "AM11-Sorting-Comparison": {
        "selection_sort": "inplace", "insertion_sort": "inplace",
        "bubble_sort": "inplace", "merge_sort": "copy", "quicksort": "copy"
    },
}


def load(project, role="solution"):
    stdout = io.StringIO()
    with contextlib.redirect_stdout(stdout), patch(
        "builtins.input", side_effect=AssertionError("Import requested input")
    ), patch("time.sleep", side_effect=AssertionError("Import slept")):
        module = runpy.run_path(str(ROOT / project / role / "main.py"))
    if stdout.getvalue():
        raise AssertionError("Import printed or ran an experiment")
    return module


class Record:
    """Compare only by key so labels reveal stability among equal keys."""

    def __init__(self, key, label):
        self.key, self.label = key, label

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __eq__(self, other):
        return self.key == other.key


class SortingPackTests(unittest.TestCase):
    def test_starters_are_import_safe_distinct_and_incomplete(self):
        for project, names in PACKS.items():
            source = (ROOT / project / "starter/main.py").read_text()
            self.assertNotEqual(source, (ROOT / project / "solution/main.py").read_text())
            starter, solution = load(project, "starter"), load(project)
            definitions = {n.name: n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)}
            for name in names:
                with self.subTest(project=project, function=name):
                    self.assertEqual(inspect.signature(starter[name]), inspect.signature(solution[name]))
                    body = definitions[name].body
                    self.assertEqual(len(body), 2)
                    self.assertIsInstance(body[0].value.value, str)
                    self.assertIsInstance(body[1], ast.Raise)
                    with self.assertRaises(NotImplementedError):
                        starter[name](*([1] * len(inspect.signature(starter[name]).parameters)))
            completed = subprocess.run(
                [sys.executable, "-B", str(ROOT / project / "starter/main.py")],
                capture_output=True, text=True, timeout=5, check=True
            )
            self.assertIn("Implement ", completed.stdout)
            self.assertEqual(completed.stderr, "")

    def test_all_sort_variants_exhaustive_small_inputs_and_mutation(self):
        cases = [list(values) for n in range(6) for values in product((-1, 0, 1), repeat=n)]
        cases += [[2, 1], [3, 2, 1], [-2, 3, 0], [1.5, -0.2, 1.5, 0], list(range(64)), list(range(64, -1, -1))]
        for project, modes in SORT_MODES.items():
            module = load(project)
            for name, mode in modes.items():
                for values in cases:
                    with self.subTest(project=project, function=name, values=values):
                        working = values.copy()
                        result = module[name](working)
                        self.assertEqual(result, sorted(values))
                        if mode == "inplace":
                            self.assertIs(result, working)
                        else:
                            self.assertIsNot(result, working)
                            self.assertEqual(working, [] if mode == "consume" else values)

    def test_stable_variants_preserve_tied_record_labels(self):
        values = [Record(2, "a"), Record(1, "b"), Record(2, "c"), Record(1, "d")]
        for project, modes in SORT_MODES.items():
            module = load(project)
            for name in modes:
                if name in ("selection_sort2", "selection_sort"):
                    continue  # Swapping selection sort intentionally makes no stability claim.
                with self.subTest(project=project, function=name):
                    result = module[name](values.copy())
                    self.assertEqual([r.label for r in result], ["b", "d", "a", "c"])

    def test_merge_and_split_contracts(self):
        module = load("AM10-Merge-Sort")
        for a in ([], [-2], [1, 1, 3], [0, 2, 5, 8]):
            for b in ([], [-3, 0, 3], [1, 1], [9]):
                left, right = a.copy(), b.copy()
                result = module["merge"](left, right)
                self.assertEqual(result, sorted(a + b))
                self.assertEqual((left, right), (a, b))
                self.assertIsNot(result, left)
                self.assertIsNot(result, right)
        for values, expected in (([], "[]\n"), ([2], "[2]\n"), ([3, 1, 2], "[3]\n[1]\n[2]\n")):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertIsNone(module["split"](values))
            self.assertEqual(output.getvalue(), expected)

    def test_partition_value_and_shuffle_contracts(self):
        for project in ("AM11-Quicksort", "AM11-Sorting-Comparison"):
            module = load(project)
            for values, pivot in (([], 7), ([3, 1, 2, 2, 4], 2), ([3, 1, 2], 8)):
                original = values.copy()
                groups = module["partition"](values, pivot)
                self.assertEqual(groups, (
                    [v for v in values if v < pivot], [v for v in values if v == pivot],
                    [v for v in values if v > pivot]
                ))
                self.assertEqual(values, original)
            self.assertEqual(module["quicksort"]([3, 1, 2, 2], random.Random(0)), [1, 2, 2, 3])
        module = load("AM11-Quicksort")
        for values in ([], [1], [2, 1, 2, 3]):
            original = values.copy()
            self.assertIsNone(module["shuffle"](values, 20))
            self.assertEqual(sorted(values), sorted(original))
            consumed = original.copy()
            result = module["shuffle2"](consumed)
            self.assertEqual(sorted(result), sorted(original))
            self.assertEqual(consumed, [])
            self.assertIsNot(result, consumed)
        for invalid in (-1, 1.5, True):
            with self.assertRaises(ValueError):
                module["shuffle"]([], invalid)

    def test_improved_bubble_stops_after_one_sorted_pass(self):
        class Counted(Record):
            count = 0

            def __gt__(self, other):
                Counted.count += 1
                return self.key > other.key

        module = load("AM9-Bubble-Sort")
        values = [Counted(i, str(i)) for i in range(10)]
        module["bubble_sort_improved"](values)
        self.assertEqual(Counted.count, 9)
        Counted.count = 0
        module["bubble_sort_in_place"](values)
        self.assertEqual(Counted.count, 45)

    def test_timing_excludes_preparation_and_validation_rejects_wrong_results(self):
        module = load("AM11-Sorting-Comparison")
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

        module["time_sort"].__globals__["perf_counter"] = clock
        self.assertEqual(module["time_sort"](sorter, Input([2, 1])), 2)
        self.assertEqual(events, ["oracle", "copy", "clock", "sort", "clock", "validation"])
        module = load("AM11-Sorting-Comparison")
        with self.assertRaises(AssertionError):
            module["time_sort"](lambda values: values, [2, 1])

    def test_default_experiment_runs_with_only_measured_labeled_results(self):
        completed = subprocess.run(
            [sys.executable, "-B", str(ROOT / "AM11-Sorting-Comparison/solution/main.py")],
            capture_output=True, text=True, timeout=5, check=True
        )
        self.assertIn("Measured medians: 3 runs", completed.stdout)
        self.assertIn("generation, copying, validation and printing excluded", completed.stdout)
        self.assertIn("not Big-O proof", completed.stdout)
        self.assertNotIn("about ", completed.stdout)
        measurements = [line for line in completed.stdout.splitlines() if line.endswith(" seconds")]
        self.assertEqual(len(measurements), 40)
        self.assertTrue(all(float(line.split()[-2]) >= 0 for line in measurements))
        self.assertEqual(completed.stderr, "")

    def test_benchmark_shared_data_fresh_copies_bounds_and_measured_medians(self):
        module = load("AM11-Sorting-Comparison")
        received = {"a": [], "b": []}
        held_inputs = []

        def sorter(name):
            def run(values):
                held_inputs.append(values)
                received[name].append(values.copy())
                values.sort()
                return values
            return run

        ticks = iter([tick for _ in range(8) for tick in (0, 2, 0, 4, 0, 6)])
        module["benchmark"].__globals__["perf_counter"] = lambda: next(ticks)
        rows = module["benchmark"]((12,), 3, 5, {name: sorter(name) for name in received})
        self.assertEqual(len(rows), 8)
        self.assertTrue(all(row["median_seconds"] == 4 and row["repeats"] == 3 for row in rows))
        self.assertEqual(received["a"], received["b"])
        self.assertEqual(len({id(v) for v in held_inputs}), len(held_inputs))
        for group in range(4):
            self.assertEqual(received["a"][group * 3:group * 3 + 3], [received["a"][group * 3]] * 3)
        self.assertEqual(module["make_workloads"](12, random.Random(5)), module["make_workloads"](12, random.Random(5)))
        for sizes, repeats in (([], 1), ([1] * 6, 1), ([-1], 1), ([2001], 1), ([True], 1), ([1.5], 1), ([1], 0), ([1], 11), ([1], True)):
            with self.assertRaises(ValueError):
                module["benchmark"](sizes, repeats)
        for size in (-1, 2001, True, 1.5):
            with self.assertRaises(ValueError):
                module["make_workloads"](size, random.Random(0))


if __name__ == "__main__":
    unittest.main()
