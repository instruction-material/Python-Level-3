"""Independent literal-character oracles, preserved sample bytes and real file I/O."""

import ast
import contextlib
import hashlib
import inspect
import io
from itertools import product
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "AM12-Crazy-Name-Tags-Printer"
NAMES = ("name_variations", "format_tags", "write_tags", "main", "write_separate_tags")
# Baseline 2473272796d28401c2b8a3f50b472070d9272e3a Git LF bytes, followed
# by the configured Mac CRLF checkout digest. No arbitrary normalization.
SAMPLES = {
    "output.txt": ("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",),
    "output1.txt": (
        "5f93e0bbde9607056d579a03d7c6bb736f2cea0fc93863a46e3a7a8452f4a7a2",
        "2d8d6daebd6f772066d54a54bd3c7e4e0e7220fa669fce6b01d659bdc63a0a5e"),
    "output2.txt": (
        "83a1b791127dfd0109ca90e1b1f38ac84ad1491c383f87bf539104be2eef361f",
        "038ae81edb4e92215c0116c344c8668c85a931e0e3e61f911a3d4d747393a22a"),
    "output3.txt": (
        "5ab2272896076d35b1af8de09e2b7664528588704c62875c0cc3a3a81ebeec07",
        "d17bf3dff36efc3f5acd7f0c312936f92324cef3fe82a5ce231497b94f5ce283"),
}


def load(role="solution"):
    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch(
        "builtins.input", side_effect=AssertionError("Import prompted")
    ), patch("builtins.open", side_effect=AssertionError("Import opened data")), patch.object(
        Path, "open", side_effect=AssertionError("Import opened a Path")
    ):
        module = runpy.run_path(str(PACK / role / "main.py"))
    if output.getvalue():
        raise AssertionError("Import printed")
    return module


def variations_oracle(name):
    characters = list(name)
    alternate = []
    for index, character in enumerate(characters):
        if index % 2 == 0:
            alternate.append(character)
    reverse = []
    pending = characters.copy()
    while pending:
        reverse.append(pending.pop())
    return (name, "".join(alternate), "".join(reverse))


def format_oracle(name, separate=False):
    outputs = []
    for variation in variations_oracle(name):
        lines = list(variation)
        if not separate:
            lines.append("")
        outputs.append("\n".join(lines) + "\n" if lines else "")
    return outputs if separate else "".join(outputs)


class NameTagTests(unittest.TestCase):
    def test_incomplete_starter_signatures_imports_and_initial_run(self):
        starter, reference = load("starter"), load()
        source = (PACK / "starter/main.py").read_text()
        definitions = {node.name: node for node in ast.parse(source).body
                       if isinstance(node, ast.FunctionDef)}
        self.assertEqual(set(definitions), set(NAMES))
        for name in NAMES:
            self.assertEqual(inspect.signature(starter[name]), inspect.signature(reference[name]))
            self.assertEqual(len(definitions[name].body), 2)
            self.assertIsInstance(definitions[name].body[0].value.value, str)
            self.assertIsInstance(definitions[name].body[1], ast.Raise)
            with self.assertRaises(NotImplementedError):
                starter[name]("Juni")
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, "-B", str(PACK / "starter/main.py")],
                                    cwd=directory, capture_output=True, text=True,
                                    timeout=5, check=True)
            self.assertIn("Implement the four core tasks", result.stdout)
            self.assertEqual(result.stderr, "")
            self.assertEqual(list(Path(directory).iterdir()), [])
        brief = (PACK / "starter/README.md").read_text()
        for contract in ("Four core tasks", "Optional separate-file", "UTF-8",
                         "three", "save/export", "reference", "cancelled", "rollback"):
            self.assertIn(contract, brief)

    def test_original_sample_assets_are_unchanged_and_not_imported_as_inputs(self):
        for name, digests in SAMPLES.items():
            data = (PACK / "solution" / name).read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            self.assertIn(digest, digests)
            if len(digests) == 2:
                self.assertEqual(b"\r\n" in data, digest == digests[1])
        self.assertEqual({file.name for file in (PACK / "starter").iterdir()},
                         {"main.py", "README.md"})

    def test_all_small_names_have_literal_orders_and_exact_section_format(self):
        module = load()
        for length in range(6):
            for characters in product("a B", repeat=length):
                name = "".join(characters)
                with self.subTest(name=name):
                    self.assertEqual(module["name_variations"](name), variations_oracle(name))
                    self.assertEqual(module["format_tags"](name), format_oracle(name))
        first = module["name_variations"]("Juni")
        self.assertIsInstance(first, tuple)
        self.assertIsNot(first, module["name_variations"]("Juni"))

    def test_case_spaces_tabs_and_unicode_codepoints_are_not_normalized(self):
        module = load()
        for name in ("", "X", "Juni", "quit", " A\tb ", "é😀a", "e\u0301B", "\0"):
            self.assertEqual(module["name_variations"](name), variations_oracle(name))
            self.assertEqual(module["format_tags"](name), format_oracle(name))
        self.assertEqual(module["format_tags"](""), "\n\n\n")
        self.assertEqual(module["format_tags"]("Juni"),
                         "J\nu\nn\ni\n\nJ\nn\n\ni\nn\nu\nJ\n\n")

    def test_invalid_names_never_open_or_truncate_existing_outputs(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "output.txt"
            target.write_bytes(b"keep")
            for name in (None, 1, True, b"Juni", [], "a\nb", "a\rb", "\ud800"):
                for function in ("name_variations", "format_tags"):
                    with self.assertRaises(ValueError):
                        module[function](name)
                with patch("builtins.open", side_effect=AssertionError("Invalid write opened")):
                    with self.assertRaises(ValueError):
                        module["write_tags"](name, target)
                self.assertEqual(target.read_bytes(), b"keep")

    def test_real_core_writes_overwrite_with_utf8_lf_and_return_none(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / " literal name.txt "
            for name in ("Juni", "é😀e\u0301 \t", "", "x"):
                target.write_bytes(b"old trailing contents")
                self.assertIsNone(module["write_tags"](name, target))
                self.assertEqual(target.read_bytes(), format_oracle(name).encode("utf-8"))

    def test_invalid_paths_fail_before_opening_or_prompting(self):
        module = load()
        class BytePath:
            def __fspath__(self):
                return b"output.txt"
        for path in (None, 0, [], b"x", "", "a\0b", "\ud800", BytePath()):
            with patch("builtins.open", side_effect=AssertionError("Invalid path opened")):
                with self.assertRaises(ValueError):
                    module["write_tags"]("Juni", path)
                with self.assertRaises(ValueError):
                    module["main"](path, input_fn=lambda _: self.fail("Invalid path prompted"))

    def test_missing_parent_and_directory_errors_propagate_without_creation(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaises(FileNotFoundError):
                module["write_tags"]("Juni", root / "missing" / "output.txt")
            with self.assertRaises(IsADirectoryError):
                module["write_tags"]("Juni", root)
            self.assertEqual(list(root.iterdir()), [])

    def test_context_manager_closes_even_after_write_failure(self):
        module = load()
        for optional in (False, True):
            calls = []
            class BrokenOutput:
                def __enter__(self):
                    calls.append("enter")
                    return self
                def write(self, text):
                    calls.append(text)
                    raise OSError("disk full")
                def __exit__(self, *args):
                    calls.append("close")
            with patch("builtins.open", return_value=BrokenOutput()) as opened:
                with self.assertRaises(OSError):
                    if optional:
                        module["write_separate_tags"]("Juni")
                    else:
                        module["write_tags"]("Juni")
            self.assertEqual(calls[-1], "close")
            self.assertEqual(opened.call_args.args, ("output1.txt" if optional else "output.txt", "w"))
            self.assertEqual(opened.call_args.kwargs, {"encoding": "utf-8", "newline": "\n"})

    def test_main_written_result_is_fresh_and_defaults_resolve_at_call_time(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "output.txt"
            with patch("builtins.input", return_value="quit") as read, patch("builtins.print") as report:
                first = module["main"](target)
                second = module["main"](target)
            self.assertEqual(read.call_count, 2)
            self.assertEqual(read.call_args.args, ("What is your name? ",))
            self.assertEqual(report.call_count, 2)
            self.assertIn("Wrote", report.call_args.args[0])
            self.assertEqual(first, {"status": "written", "path": str(target)})
            self.assertIsNot(first, second)
            self.assertEqual(target.read_bytes(), format_oracle("quit").encode())

    def test_main_cancellation_and_invalid_names_preserve_outputs(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "output.txt"
            for event, status in ((EOFError, "cancelled"), (KeyboardInterrupt, "cancelled"),
                                  ("a\nb", "invalid"), (None, "invalid")):
                target.write_bytes(b"preserve")
                def read(prompt):
                    self.assertEqual(prompt, "What is your name? ")
                    if isinstance(event, type):
                        raise event
                    return event
                messages = []
                with patch("builtins.open", side_effect=AssertionError("Invalid/cancelled opened")):
                    outcome = module["main"](target, read, messages.append)
                self.assertEqual(outcome, {"status": status, "path": str(target)})
                self.assertEqual(target.read_bytes(), b"preserve")
                self.assertEqual(len(messages), 1)
                self.assertNotIn("Wrote", messages[0])

    def test_main_failures_and_callback_configuration_are_honest(self):
        module = load()
        for input_fn, output_fn in ((0, print), (input, "print")):
            with patch("builtins.input", side_effect=AssertionError("Invalid callback prompted")):
                with self.assertRaises(ValueError):
                    module["main"](input_fn=input_fn, output_fn=output_fn)
        messages = []
        with patch("builtins.open", side_effect=PermissionError("denied")):
            outcome = module["main"]("output.txt", lambda _: "Juni", messages.append)
        self.assertEqual(outcome, {"status": "failed", "path": "output.txt"})
        self.assertNotIn("Wrote", messages[0])
        with self.assertRaises(RuntimeError):
            module["main"](input_fn=lambda _: (_ for _ in ()).throw(RuntimeError("callback")))

    def test_optional_separate_outputs_have_no_separators_and_empty_files(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            paths = [Path(directory) / f"output{index}.txt" for index in range(1, 4)]
            for name in ("Juni", "é😀 A", ""):
                self.assertIsNone(module["write_separate_tags"](name, paths))
                self.assertEqual([path.read_bytes() for path in paths],
                                 [text.encode("utf-8") for text in format_oracle(name, True)])

    def test_optional_validates_all_names_and_paths_before_any_open(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            paths = [Path(directory) / f"output{index}.txt" for index in range(3)]
            for path in paths:
                path.write_bytes(b"keep")
            for name, destinations in (("a\nb", paths), ("Juni", paths[:2]),
                                       ("Juni", "abc"), ("Juni", [*paths[:2], ""]),
                                       ("Juni", [paths[0], paths[1], paths[0]])):
                with patch("builtins.open", side_effect=AssertionError("Validation opened")):
                    with self.assertRaises(ValueError):
                        module["write_separate_tags"](name, destinations)
                self.assertEqual([path.read_bytes() for path in paths], [b"keep"] * 3)

    def test_optional_equivalent_symlink_and_hardlink_aliases_preserve_outputs(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first, other = root / "first", root / "other"
            first.write_bytes(b"first")
            other.write_bytes(b"other")
            symlink, hardlink = root / "symlink", root / "hardlink"
            symlink.symlink_to(first)
            os.link(first, hardlink)
            for alias in (root / "." / "first", symlink, hardlink):
                with patch("builtins.open", side_effect=AssertionError("Alias opened")):
                    with self.assertRaises(ValueError):
                        module["write_separate_tags"]("Juni", [first, other, alias])
                self.assertEqual(first.read_bytes(), b"first")
                self.assertEqual(other.read_bytes(), b"other")

    def test_later_optional_io_failure_does_not_claim_transactional_rollback(self):
        module = load()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first, last = root / "first", root / "last"
            last.write_bytes(b"preserve")
            with self.assertRaises(IsADirectoryError):
                module["write_separate_tags"]("Juni", [first, root, last])
            self.assertEqual(first.read_bytes(), b"J\nu\nn\ni\n")
            self.assertEqual(last.read_bytes(), b"preserve")

    def test_guarded_reference_runs_in_temporary_workspace_and_eof_writes_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "output.txt"
            for input_text in ("Juni\n", "\n"):
                result = subprocess.run([sys.executable, "-B", str(PACK / "solution/main.py")],
                                        cwd=directory, input=input_text, capture_output=True,
                                        text=True, timeout=5, check=True)
                self.assertIn("Wrote", result.stdout)
                self.assertEqual(result.stderr, "")
                self.assertEqual(target.read_bytes(), format_oracle(input_text[:-1]).encode())
            target.unlink()
            result = subprocess.run([sys.executable, "-B", str(PACK / "solution/main.py")],
                                    cwd=directory, input="", capture_output=True,
                                    text=True, timeout=5, check=True)
            self.assertIn("Cancelled", result.stdout)
            self.assertEqual(list(Path(directory).iterdir()), [])
