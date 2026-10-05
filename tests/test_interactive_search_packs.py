"""Independent state, input, workload and timer checks for the AM7 search packs."""

import ast
import builtins
import contextlib
import inspect
import io
import itertools
import math
import random
import re
import subprocess
import sys
import time
import unittest
from unittest.mock import Mock, patch

from test_algorithm_packs import ROOT, load_module


REVERSE = "AM7-Reverse-Number-Guesser"
PLAYER = "AM7-Number-Guesser"
TIMING = "AM7-Runtime-Comparator"
CONTRACTS = {
    REVERSE: ("parse_feedback", "midpoint", "update_bounds", "play"),
    PLAYER: ("parse_guess", "guess_feedback", "play"),
    TIMING: (
        "linear_search", "bin_search_iter", "bin_search_recur",
        "make_workload", "compare_searches", "main",
    ),
}


def scripted(play, answers, **options):
    iterator = iter(answers)
    prompts, messages = [], []

    def input_fn(prompt):
        prompts.append(prompt)
        try:
            answer = next(iterator)
        except StopIteration:
            raise EOFError from None
        if isinstance(answer, BaseException):
            raise answer
        return answer

    result = play(input_fn=input_fn, output_fn=messages.append, **options)
    return result, prompts, messages


class InteractiveSearchPackTests(unittest.TestCase):
    def test_all_starter_tasks_are_incomplete_quiet_and_signature_matched(self):
        for project, names in CONTRACTS.items():
            with self.subTest(project=project):
                source = (ROOT / project / "starter/main.py").read_text()
                starter = load_module(project, "starter")
                solution = load_module(project, "solution")
                self.assertNotEqual(source, (ROOT / project / "solution/main.py").read_text())
                definitions = {
                    node.name: node for node in ast.parse(source).body
                    if isinstance(node, ast.FunctionDef)
                }
                self.assertEqual(set(definitions), set(names))
                for name in names:
                    self.assertEqual(inspect.signature(starter[name]), inspect.signature(solution[name]))
                    self.assertEqual(len(definitions[name].body), 2)
                    self.assertIsInstance(definitions[name].body[0].value, ast.Constant)
                    self.assertIsInstance(definitions[name].body[1], ast.Raise)
                    with self.assertRaises(NotImplementedError):
                        starter[name](*([1] * len(inspect.signature(starter[name]).parameters)))
                brief = (ROOT / project / "starter/README.md").read_text()
                for phrase in ("Python IDE", "ValueError", "solution", "save/export"):
                    self.assertIn(phrase.lower(), brief.lower())

    def test_starter_and_reference_imports_never_draw_random_values_or_time(self):
        with patch.object(random, "Random", side_effect=AssertionError("Import generated data.")), \
             patch.object(random, "randint", side_effect=AssertionError("Import drew a secret.")), \
             patch.object(time, "perf_counter", side_effect=AssertionError("Import ran a timer.")):
            for project in CONTRACTS:
                for role in ("starter", "solution"):
                    load_module(project, role)

    def test_direct_starters_remind_and_references_run_or_cancel_cleanly(self):
        for project in CONTRACTS:
            starter = subprocess.run(
                [sys.executable, "-B", "main.py"], cwd=ROOT / project / "starter",
                input="", capture_output=True, text=True, check=True, timeout=5,
            )
            self.assertIn("Implement ", starter.stdout)
            self.assertEqual(starter.stderr, "")
            reference = subprocess.run(
                [sys.executable, "-B", "main.py"], cwd=ROOT / project / "solution",
                input="quit\n", capture_output=True, text=True, check=True, timeout=5,
            )
            self.assertEqual(reference.stderr, "")
            if project == TIMING:
                self.assertIn("size=2000, queries=50", reference.stdout)
                self.assertIn("repeats=3", reference.stdout)
                self.assertIn("median_seconds=", reference.stdout)
                self.assertIn("not a proof of Big-O", reference.stdout)
            else:
                self.assertIn("Game cancelled.", reference.stdout)
                self.assertNotIn("You win", reference.stdout)
                self.assertNotIn("Confirmed by feedback:", reference.stdout)

    def test_reverse_feedback_normalization_and_strict_bound_updates(self):
        module = load_module(REVERSE, "solution")
        for token in ("yes", "above", "below", "quit"):
            self.assertEqual(module["parse_feedback"](" \t" + token.upper() + " \n"), token)
        for bad in ("", "correct", "YES?", "higher", None, True, 3, []):
            with self.assertRaises(ValueError):
                module["parse_feedback"](bad)
        for low in range(1, 9):
            for high in range(low, 9):
                self.assertEqual(module["midpoint"](low, high), (low + high) // 2)
                for guess in range(low, high + 1):
                    for feedback, wanted in (("above", (guess + 1, high)), ("below", (low, guess - 1))):
                        if wanted[0] > wanted[1]:
                            with self.assertRaises(ValueError):
                                module["update_bounds"](low, high, guess, feedback)
                        else:
                            result = module["update_bounds"](low, high, guess, feedback)
                            self.assertEqual(result, wanted)
                            self.assertLess(result[1] - result[0], high - low)
        for bounds in ((0, 100), (1, 101), (2, 1), (True, 2), (1, 2.0)):
            with self.assertRaises(ValueError):
                module["midpoint"](*bounds)
        for guess, feedback in ((0, "above"), (101, "below"), (True, "above"), (50, "yes"), (50, "quit")):
            with self.assertRaises(ValueError):
                module["update_bounds"](1, 100, guess, feedback)

    def test_reverse_truthful_feedback_identifies_every_secret_within_seven(self):
        play = load_module(REVERSE, "solution")["play"]
        for first, last in ((1, 100), (1, 8), (95, 100), (40, 40), (1, 2), (99, 100)):
            for secret in range(first, last + 1):
                low, high = first, last
                seen, messages = [], []

                def feedback(prompt):
                    nonlocal low, high
                    match = re.search(r": (\d+)\?", prompt)
                    self.assertIsNotNone(match)
                    guess = int(match[1])
                    self.assertEqual(guess, (low + high) // 2)
                    self.assertTrue(low <= secret <= high)
                    seen.append(guess)
                    if secret == guess:
                        return "yes"
                    previous_width = high - low
                    if secret > guess:
                        low = guess + 1
                        response = "above"
                    else:
                        high = guess - 1
                        response = "below"
                    self.assertLess(high - low, previous_width)
                    return response

                result = play(low=first, high=last, input_fn=feedback, output_fn=messages.append)
                self.assertEqual(result["number"], secret)
                self.assertIn(result["status"], ("confirmed", "inferred"))
                self.assertEqual(result["guesses"], seen)
                self.assertLessEqual(len(seen), 7)
                if result["status"] == "inferred":
                    self.assertEqual(result["bounds"], (secret, secret))
                    self.assertIn("inferred, not confirmed", messages[-1])
                    self.assertNotIn("Confirmed by feedback:", "\n".join(messages))
                else:
                    self.assertEqual(seen[-1], secret)

    def test_reverse_invalid_feedback_retries_the_same_unconsumed_guess(self):
        play = load_module(REVERSE, "solution")["play"]
        result, prompts, messages = scripted(play, [None, "", "YES?", "correct", " YeS "])
        self.assertEqual(result["status"], "confirmed")
        self.assertEqual(result["number"], 50)
        self.assertEqual(result["guesses"], [50])
        self.assertEqual(len(prompts), 5)
        self.assertEqual(len(set(prompts)), 1)
        self.assertEqual(sum(message.startswith("Invalid feedback") for message in messages), 4)

    def test_reverse_contradiction_exhaustion_and_inference_are_distinct(self):
        play = load_module(REVERSE, "solution")["play"]
        result, _, messages = scripted(play, ["below"], low=1, high=2)
        self.assertEqual(result, {"status": "contradiction", "number": None, "guesses": [1], "bounds": (1, 2)})
        self.assertIn("contradicts", messages[-1])
        result, _, messages = scripted(play, ["above"], max_guesses=1)
        self.assertEqual(result, {"status": "exhausted", "number": None, "guesses": [50], "bounds": (51, 100)})
        self.assertNotIn("Confirmed by feedback:", "\n".join(messages))
        result, prompts, _ = scripted(play, [], low=99, high=99)
        self.assertEqual(result["status"], "inferred")
        self.assertEqual(result["guesses"], [])
        self.assertEqual(prompts, [])
        result, _, _ = scripted(play, ["above"], low=1, high=2, max_guesses=1)
        self.assertEqual((result["status"], result["number"]), ("inferred", 2))

    def test_reverse_cancels_and_rejects_configuration_before_input(self):
        play = load_module(REVERSE, "solution")["play"]
        for answer in (" QuIt ", EOFError(), KeyboardInterrupt()):
            result, _, messages = scripted(play, ["above", answer])
            self.assertEqual(result["status"], "cancelled")
            self.assertIsNone(result["number"])
            self.assertEqual(result["guesses"], [50])
            self.assertEqual(messages[-1], "Game cancelled.")
        for options in ({"low": 0}, {"high": 101}, {"low": True}, {"max_guesses": 8}, {"max_guesses": False}, {"input_fn": 1}, {"output_fn": 1}):
            with self.assertRaises(ValueError):
                play(**options)

    def test_reverse_default_callbacks_resolve_at_call_time(self):
        play = load_module(REVERSE, "solution")["play"]
        output = io.StringIO()
        with patch("builtins.input", return_value="yes"), contextlib.redirect_stdout(output):
            result = play()
        self.assertEqual((result["status"], result["number"]), ("confirmed", 50))
        self.assertIn("Confirmed by feedback: 50", output.getvalue())

    def test_game_outcomes_own_their_history_and_do_not_reuse_global_state(self):
        for project, options, answers in (
            (REVERSE, {"low": 1, "high": 2}, ["yes"]),
            (PLAYER, {"secret": 50}, ["50"]),
        ):
            play = load_module(project, "solution")["play"]
            first, _, _ = scripted(play, answers, **options)
            expected = first["guesses"][:]
            first["guesses"].append(999)
            second, _, _ = scripted(play, answers, **options)
            self.assertIsNot(first, second)
            self.assertIsNot(first["guesses"], second["guesses"])
            self.assertEqual(second["guesses"], expected)

    def test_player_parses_only_the_documented_integer_text_and_quit(self):
        module = load_module(PLAYER, "solution")
        for text, wanted in (("1", 1), ("100", 100), (" +007 ", 7), (" QuIt ", None)):
            self.assertEqual(module["parse_guess"](text), wanted)
        for text in ("", "-1", "0", "101", "1.0", "1_0", "1 0", "７", None, True, 10, "9" * 5000):
            with self.assertRaises(ValueError):
                module["parse_guess"](text)
        for guess in range(1, 101):
            for secret in range(1, 101):
                wanted = "higher" if guess < secret else "lower" if guess > secret else "correct"
                self.assertEqual(module["guess_feedback"](guess, secret), wanted)
        for args in ((0, 50), (True, 50), (50, 101), (50, 50.0)):
            with self.assertRaises(ValueError):
                module["guess_feedback"](*args)

    def test_player_binary_strategy_wins_for_all_secrets_but_arbitrary_guesses_can_lose(self):
        play = load_module(PLAYER, "solution")["play"]
        for secret in range(1, 101):
            low, high = 1, 100
            guesses = []
            while low <= high:
                guess = (low + high) // 2
                guesses.append(str(guess))
                if guess == secret:
                    break
                if guess < secret:
                    low = guess + 1
                else:
                    high = guess - 1
            result, _, _ = scripted(play, guesses, secret=secret)
            self.assertEqual(result["status"], "won")
            self.assertEqual(result["secret"], secret)
            self.assertLessEqual(len(result["guesses"]), 7)
        result, _, messages = scripted(play, ["1"] * 7, secret=42)
        self.assertEqual(result["status"], "lost")
        self.assertEqual(result["guesses"], [1] * 7)
        self.assertNotIn("You win", "\n".join(messages))
        self.assertIn("secret was 42", messages[-1])

    def test_player_invalid_inputs_last_attempt_and_cancel_do_not_falsely_win(self):
        play = load_module(PLAYER, "solution")["play"]
        result, prompts, _ = scripted(play, ["", "0", "101", "1.5", "x", None, "42"], secret=42, max_guesses=1)
        self.assertEqual(result["status"], "won")
        self.assertEqual(result["guesses"], [42])
        self.assertEqual(len(prompts), 7)
        self.assertEqual(len(set(prompts)), 1)
        result, _, _ = scripted(play, ["1", "2", "3", "4", "5", "6", "42"], secret=42)
        self.assertEqual(result["status"], "won")
        self.assertEqual(len(result["guesses"]), 7)
        for answer in (" QuIt ", EOFError(), KeyboardInterrupt()):
            result, _, messages = scripted(play, ["1", answer], secret=42)
            self.assertEqual(result["status"], "cancelled")
            self.assertEqual(result["guesses"], [1])
            self.assertNotIn("42", "\n".join(messages))
            self.assertNotIn("You win", "\n".join(messages))

    def test_player_random_default_is_drawn_per_call_and_callbacks_resolve_at_call_time(self):
        module = load_module(PLAYER, "solution")
        with patch.object(module["random"], "randint", return_value=40) as draw:
            result, _, _ = scripted(module["play"], ["40"], low=30, high=45)
            self.assertEqual(result["status"], "won")
            draw.assert_called_once_with(30, 45)
            scripted(module["play"], ["40"], secret=40)
            self.assertEqual(draw.call_count, 1)
        output = io.StringIO()
        with patch("builtins.input", return_value="50"), contextlib.redirect_stdout(output):
            result = module["play"](secret=50)
        self.assertEqual(result["status"], "won")
        for options in ({"secret": True}, {"secret": 0}, {"secret": 101}, {"low": 51, "secret": 50}, {"high": 101}, {"max_guesses": 0}, {"max_guesses": 8}, {"max_guesses": True}, {"input_fn": 1}, {"output_fn": 1}):
            with self.assertRaises(ValueError):
                module["play"](**options)

    def test_searches_match_membership_on_all_364_small_lists_without_mutation(self):
        module = load_module(TIMING, "solution")
        for length in range(6):
            for sequence in itertools.product((-1, 0, 1), repeat=length):
                for name in ("linear_search", "bin_search_iter", "bin_search_recur"):
                    values = list(sequence) if name == "linear_search" else sorted(sequence)
                    snapshot = values[:]
                    for item in range(-2, 3):
                        self.assertIs(module[name](values, item), item in snapshot)
                        self.assertEqual(values, snapshot)
        class IndexedOnly:
            def __init__(self):
                self.reads = 0
            def __len__(self):
                return 1000000
            def __iter__(self):
                raise AssertionError("Binary search must not scan.")
            def __getitem__(self, index):
                if isinstance(index, slice):
                    raise AssertionError("Iterative search must not slice.")
                self.reads += 1
                return index
        for item in (-1, 0, 499999, 999999, 1000000):
            values = IndexedOnly()
            self.assertIs(module["bin_search_iter"](values, item), 0 <= item < 1000000)
            self.assertLessEqual(values.reads, 60)

    def test_workloads_are_seeded_fresh_bounded_and_do_not_change_global_rng(self):
        make = load_module(TIMING, "solution")["make_workload"]
        state = random.getstate()
        first = make(12, 7, 42)
        second = make(12, 7, 42)
        self.assertEqual(first, second)
        self.assertIsNot(first[0], second[0])
        self.assertIsNot(first[1], second[1])
        self.assertEqual(random.getstate(), state)
        self.assertEqual(tuple(map(len, first)), (12, 7))
        self.assertTrue(all(type(item) is int and 0 <= item <= 100000 for group in first for item in group))
        self.assertEqual(make(0, 0), ([], []))
        for options in ({"size": -1}, {"size": 5001}, {"size": True}, {"queries": 101}, {"queries": 2.0}, {"seed": False}, {"seed": "a"}):
            with self.assertRaises(ValueError):
                make(**options)

    def test_search_reports_use_exact_measured_medians_and_repeated_query_hits(self):
        compare = load_module(TIMING, "solution")["compare_searches"]
        clock = Mock(side_effect=[0, 1, 10, 13, 20, 22, 30, 35, 40, 44, 50, 56])
        nums, targets = [3, -1, 3, 0], [3, 2, 3]
        result = compare(nums, targets, repeats=3, clock=clock)
        self.assertEqual([row["median_seconds"] for row in result], [2, 5])
        self.assertEqual([row["algorithm"] for row in result], ["linear", "binary"])
        self.assertEqual([row["input_order"] for row in result], ["original", "sorted"])
        for row in result:
            self.assertEqual(set(row), {"algorithm", "size", "queries", "hits", "repeats", "input_order", "median_seconds"})
            self.assertEqual((row["size"], row["queries"], row["hits"], row["repeats"]), (4, 3, 2, 3))
        self.assertEqual(clock.call_count, 12)
        self.assertEqual(nums, [3, -1, 3, 0])
        self.assertEqual(targets, [3, 2, 3])
        self.assertIsNot(result[0], result[1])

    def test_shared_queries_warmups_copying_oracles_and_validation_stay_outside_timer(self):
        compare = load_module(TIMING, "solution")["compare_searches"]
        namespace = compare.__globals__
        nums, targets = [3, -1, 3, 0], [3, 2, -1]
        timed, ticks = False, 0
        batches, searches, checks = [], [], []
        original_check = namespace["_check_results"]

        def clock():
            nonlocal timed, ticks
            timed = not timed
            ticks += 1
            return ticks

        def search(name):
            def execute(values, item):
                self.assertIsNot(values, nums)
                count = sum(row[0] == name for row in searches)
                if count % len(targets) == 0:
                    batches.append(values)
                searches.append((name, item, timed, tuple(values)))
                return item in values
            return execute

        def checked(values, original, actual, expected):
            self.assertFalse(timed, "Result checking entered the timer.")
            checks.append(tuple(actual))
            return original_check(values, original, actual, expected)

        def prepare_sorted(values):
            self.assertFalse(timed, "Sorting entered the timer.")
            return builtins.sorted(values)

        def oracle(values):
            self.assertFalse(timed, "Oracle work entered the timer.")
            return builtins.set(values)

        with patch.dict(namespace, {"linear_search": search("linear"), "bin_search_iter": search("binary"), "bin_search_recur": Mock(side_effect=AssertionError("Optional recursion was benchmarked.")), "_check_results": checked, "sorted": prepare_sorted, "set": oracle}), \
             patch.object(random, "Random", side_effect=AssertionError("Comparison generated a workload.")), \
             patch("builtins.print", side_effect=AssertionError("Comparison printed a report.")):
            compare(nums, targets, repeats=2, clock=clock)
        self.assertEqual(ticks, 8)
        self.assertEqual(len(batches), 6)
        self.assertEqual(len({id(values) for values in batches}), 6)
        self.assertEqual(len(checks), 6)
        self.assertEqual([item for _, item, _, _ in searches], targets * 6)
        self.assertTrue(all(not row[2] for row in searches[:6]))
        self.assertTrue(all(row[2] for row in searches[6:]))
        self.assertEqual(nums, [3, -1, 3, 0])
        self.assertEqual(targets, [3, 2, -1])

    def test_bad_search_answers_or_mutation_stop_reports_before_or_after_timing(self):
        compare = load_module(TIMING, "solution")["compare_searches"]
        namespace = compare.__globals__
        for replacement in (lambda values, target: False, lambda values, target: 1):
            clock = Mock(return_value=0)
            with patch.dict(namespace, {"linear_search": replacement}), self.assertRaises(AssertionError):
                compare([1], [1], clock=clock)
            clock.assert_not_called()
        calls = 0
        def timed_wrong(values, target):
            nonlocal calls
            calls += 1
            return calls == 1
        clock = Mock(side_effect=[0, 1])
        with patch.dict(namespace, {"linear_search": timed_wrong}), self.assertRaises(AssertionError):
            compare([1], [1], repeats=1, clock=clock)
        self.assertEqual(clock.call_count, 2)
        def mutating(values, target):
            values.append(99)
            return target in values
        with patch.dict(namespace, {"linear_search": mutating}), self.assertRaises(AssertionError):
            compare([1], [1], clock=Mock(return_value=0))

    def test_comparison_domains_fail_before_timing_and_bad_clocks_never_report(self):
        compare = load_module(TIMING, "solution")["compare_searches"]
        for nums, targets, repeats in (((), [], 1), ([True], [], 1), ([1.0], [], 1), ([0] * 5001, [], 1), ([], (), 1), ([], [False], 1), ([], [0] * 101, 1), ([], [], 0), ([], [], 11), ([], [], True)):
            clock = Mock(return_value=0)
            with self.assertRaises(ValueError):
                compare(nums, targets, repeats, clock)
            clock.assert_not_called()
        with self.assertRaises(ValueError):
            compare([], [], clock=42)
        for readings in ((0, -1), (math.nan, 1), (0, math.inf), (False, 1), ("0", 1), (-1e308, 1e308), (-10**308, 10**308)):
            with self.assertRaises(ValueError):
                compare([1], [1], repeats=1, clock=Mock(side_effect=readings))

    def test_empty_batches_measure_overhead_and_main_prints_only_measured_rows(self):
        module = load_module(TIMING, "solution")
        rows = module["compare_searches"]([], [], repeats=1, clock=Mock(side_effect=[0, 1, 2, 4]))
        self.assertEqual([row["median_seconds"] for row in rows], [1, 2])
        self.assertTrue(all(row["hits"] == 0 and row["queries"] == 0 for row in rows))
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rows = module["main"](size=10, queries=3, repeats=2, seed=17)
        self.assertEqual([row["size"] for row in rows], [10, 10])
        self.assertEqual([row["repeats"] for row in rows], [2, 2])
        self.assertTrue(all(math.isfinite(row["median_seconds"]) and row["median_seconds"] >= 0 for row in rows))
        self.assertIn("seed=17", output.getvalue())
        self.assertIn("Hit position can differ", output.getvalue())


if __name__ == "__main__":
    unittest.main()
