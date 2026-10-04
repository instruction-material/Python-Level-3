"""Analysis inputs are supplied code or worksheets, not unfinished algorithms."""

import ast
import contextlib
import io
import unittest

from test_algorithm_packs import ROOT, load_module


class AnalysisPackTests(unittest.TestCase):
    def test_function_analysis_supplies_original_code_without_answer_comments(self):
        project = "AM6-Function-Analysis"
        starter_text = (ROOT / project / "starter" / "main.py").read_text()
        reference_text = (ROOT / project / "solution" / "main.py").read_text()
        self.assertNotIn("# O(", starter_text)
        self.assertNotEqual(starter_text, reference_text)
        def definitions(source):
            return {
                node.name: ast.dump(node)
                for node in ast.parse(source).body
                if isinstance(node, ast.FunctionDef)
            }
        self.assertEqual(definitions(starter_text), definitions(reference_text))
        self.assertEqual(len(definitions(starter_text)), 14)
        load_module(project, "starter")
        load_module(project, "solution")

    def test_function_examples_have_checkable_operation_counts(self):
        module = load_module("AM6-Function-Analysis", "starter")
        cases = [
            ("f1", (4,), 4), ("f2", (4,), 2), ("f3", (8,), 8),
            ("f4", (4,), 6), ("f5", (4,), 4), ("f6", (8,), 3),
            ("f7", (3,), 27), ("f8", (3, 5), 8), ("f9", (3, 5), 15),
            ("f10", (3, 5), 3), ("f10", (3, 0), 0), ("f11", ([1, 2, 3],), 3),
        ]
        for name, args, expected in cases:
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                module[name](*args)
            self.assertEqual(len(output.getvalue().splitlines()), expected, name)
        self.assertIs(module["f12"]([1, 2, 3]), False)
        self.assertIs(module["f12"]([1, 2, 1]), True)
        self.assertIs(module["f13"]([-1, 0]), True)
        self.assertIs(module["f13"]([-1, 2]), False)
        self.assertIs(module["f14"]([-1, 1]), True)
        self.assertIs(module["f14"]([-1, 2]), False)

    def test_big_o_worksheet_has_ten_prompts_and_a_separate_reference(self):
        project = ROOT / "AM6-Big-O-Analysis"
        starter = (project / "starter" / "README.md").read_text()
        reference = (project / "solution" / "README.md").read_text()
        for number in range(1, 11):
            self.assertIn(f"### P{number}:", starter)
            self.assertIn(f"### P{number}:", reference)
        self.assertEqual(starter.count("Classification: ______"), 10)
        self.assertIn("mathematical worksheet", starter)
        self.assertNotIn("Classification: ______", reference)
        self.assertFalse((project / "starter" / "main.py").exists())


if __name__ == "__main__":
    unittest.main()
