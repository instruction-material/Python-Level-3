"""Check console references with deterministic, local input and output."""

import contextlib
import datetime
import io
import unittest
from unittest.mock import patch

from test_algorithm_packs import load_module


def interact(function, answers):
    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch("builtins.input", side_effect=answers):
        function()
    return output.getvalue()


class ConsoleReviewTests(unittest.TestCase):
    def test_mad_libs_collects_and_reuses_five_words(self):
        program = load_module("AM1-Mad-Libs", "solution")["run_mad_libs"]
        first = ["bright", "tiny", "noodles", "dance", "cheered"]
        second = ["quiet", "green", "apples", "skip", "laughed"]
        first_story = interact(program, first)
        second_story = interact(program, second)
        for word in first:
            self.assertIn(word, first_story)
        for word in second:
            self.assertIn(word, second_story)
        self.assertNotEqual(first_story, second_story)
        self.assertTrue(first_story.endswith("!\n"))

    def test_language_rules_are_case_insensitive_and_report_failures(self):
        module = load_module("AM1-Junian-Language-Verifier", "solution")
        errors = module["verification_errors"]
        for word in ("Lumo", "LUMO", "ae", "aE"):
            self.assertEqual(errors(word), [], word)
        for word in ("", "x", "odd", "bcdf", "Aa", "Aboa"):
            self.assertTrue(errors(word), word)
        all_errors = errors("x")
        self.assertEqual(len(all_errors), 3)
        self.assertIn("even", all_errors[0])
        self.assertIn("vowels", all_errors[1])
        self.assertIn("different", all_errors[2])
        self.assertIn("valid.", interact(module["run_verifier"], ["Lumo"]))
        rejected = interact(module["run_verifier"], ["x"])
        self.assertIn("invalid.", rejected)
        for error in all_errors:
            self.assertIn(error, rejected)

    def test_assistant_handles_blank_unknown_and_exact_exit_commands(self):
        program = load_module("AM1-Juni-Assistant", "solution")["run_assistant"]
        output = interact(program, ["", "12", "7"])
        self.assertEqual(output.count("Unknown command."), 2)
        self.assertEqual(output.count("Goodbye!"), 1)
        for command in ("quit", " EXIT "):
            self.assertIn("Goodbye!", interact(program, [command]))
        self.assertIn("Goodbye!", interact(program, EOFError))

    def test_assistant_keeps_name_state_and_formats_time_and_date(self):
        module = load_module("AM1-Juni-Assistant", "solution")
        fixed = datetime.datetime(2026, 1, 2, 3, 4)
        with patch.object(module["datetime"], "datetime") as clock:
            clock.now.return_value = fixed
            output = interact(
                module["run_assistant"], ["4", "3", "Learner", "4", "1", "2", "7"]
            )
        self.assertIn("No name is stored yet.", output)
        self.assertIn("The stored name is Learner", output)
        self.assertIn("03:04", output)
        self.assertIn("2026-01-02", output)

    def test_assistant_random_commands_use_their_own_lists(self):
        module = load_module("AM1-Juni-Assistant", "solution")
        program = module["run_assistant"]
        facts = ["test fact"]
        jokes = ["test joke", "second test joke"]
        with patch.dict(program.__globals__, {"fun_facts": facts, "jokes": jokes}), patch.object(
            module["random"], "choice", side_effect=lambda values: values[0]
        ) as choose:
            output = interact(program, ["5", "6", "7"])
        self.assertIn("test fact", output)
        self.assertIn("test joke", output)
        self.assertEqual(choose.call_args_list[0].args[0], facts)
        self.assertEqual(choose.call_args_list[1].args[0], jokes)


if __name__ == "__main__":
    unittest.main()
