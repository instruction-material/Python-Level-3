"""Independent ranking/parser/translation oracles and original asset-byte checks."""

import ast
import contextlib
import copy
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
BASEBALL = "AM9-Baseball-Analytics"
DICTIONARY = "AM12-File-IO-and-Dictionaries"
LATIN = "AM12-Juni-Latin-with-File-IO"
PACKS = {
    BASEBALL: ("bubble_baseball", "print_list", "main"),
    DICTIONARY: ("parse_pairs", "load_pairs", "main"),
    LATIN: ("translate", "translate_punctuation", "read_lines", "translate_lines",
            "write_lines", "translate_file"),
}
ORIGINAL_PLAYERS = [
    ["B. Harper", 0.254, 27, 92], ["J. Soler", 0.256, 36, 91],
    ["C. Yelich", 0.329, 41, 89], ["C. Bellinger", 0.312, 42, 100],
    ["M. Trout", 0.299, 41, 99], ["F. Lindor", 0.296, 23, 56],
    ["M. Betts", 0.285, 21, 67], ["A. Rendon", 0.328, 29, 104],
    ["D. Lemahieu", 0.331, 22, 87], ["R. Acuna", 0.290, 36, 89],
]
ASSET_DIGESTS = {
    (DICTIONARY, "input.txt"): "68682cffe83e789d637dc16d247608e8911c2ea6608e0e51eda701e9a6d6f580",
    (LATIN, "input_no_punctuation.txt"): "12f8a11bb65655593bbeb41a8602e389bdea1f9544a3b33fbd33a5dc9a64c76f",
    (LATIN, "input_punctuation.txt"): "3a67645f67f58c84ef20db3540d8b6f6bcdbdd7be1d679eebf307b37422d3d2d",
}


def load(pack, role="solution"):
    output = io.StringIO()
    with contextlib.redirect_stdout(output), patch(
        "builtins.input", side_effect=AssertionError("Import requested input")
    ), patch("time.sleep", side_effect=AssertionError("Import slept")), patch(
        "builtins.open", side_effect=AssertionError("Import opened data")
    ), patch.object(Path, "open", side_effect=AssertionError("Import opened a Path")):
        module = runpy.run_path(str(ROOT / pack / role / "main.py"))
    if output.getvalue():
        raise AssertionError("Import printed or ran a demonstration")
    return module


def word_oracle(word):
    characters = list(word)
    if not characters:
        return ""
    characters.append(characters.pop(0))
    return "".join(characters) + "ay"


class RecordFilePackTests(unittest.TestCase):
    def test_starters_are_distinct_incomplete_quiet_and_signature_matched(self):
        for pack, names in PACKS.items():
            source = (ROOT / pack / "starter/main.py").read_text()
            starter, reference = load(pack, "starter"), load(pack)
            self.assertNotEqual(source, (ROOT / pack / "solution/main.py").read_text())
            definitions = {node.name: node for node in ast.parse(source).body
                           if isinstance(node, ast.FunctionDef)}
            for name in names:
                with self.subTest(pack=pack, function=name):
                    self.assertEqual(inspect.signature(starter[name]),
                                     inspect.signature(reference[name]))
                    body = definitions[name].body
                    self.assertEqual(len(body), 2)
                    self.assertIsInstance(body[0].value.value, str)
                    self.assertIsInstance(body[1], ast.Raise)
                    with self.assertRaises(NotImplementedError):
                        starter[name](*([1] * len(inspect.signature(starter[name]).parameters)))
            self.assertGreater(len((ROOT / pack / "starter/README.md").read_text()), 1000)
            with tempfile.TemporaryDirectory() as directory:
                result = subprocess.run(
                    [sys.executable, "-B", str(ROOT / pack / "starter/main.py")],
                    cwd=directory, capture_output=True, text=True, timeout=5, check=True
                )
                self.assertIn("Implement ", result.stdout)
                self.assertEqual(result.stderr, "")
                self.assertEqual(list(Path(directory).iterdir()), [])

    def test_original_asset_bytes_and_synthetic_player_records_are_preserved(self):
        for (pack, name), expected in ASSET_DIGESTS.items():
            for role in ("starter", "solution"):
                data = (ROOT / pack / role / name).read_bytes()
                self.assertEqual(hashlib.sha256(data).hexdigest(), expected)
                self.assertIn(b"\r\n", data)
                self.assertFalse(data.endswith(b"\n"))
        for role in ("starter", "solution"):
            module = load(BASEBALL, role)
            self.assertEqual(module["playerList"], ORIGINAL_PLAYERS)
            self.assertIs(module["playerList"], module["player_list"])
            for number in range(1, 11):
                self.assertIs(module["p" + str(number)], module["playerList"][number - 1])

    def test_rankings_all_small_inputs_stable_ties_fresh_result_and_no_mutation(self):
        rank = load(BASEBALL)["bubble_baseball"]
        cases = [values for n in range(6) for values in product((0, 1, 2), repeat=n)]
        for values in cases:
            records = [["player " + str(i), value / 2, value, 2 * value]
                       for i, value in enumerate(values)]
            original = copy.deepcopy(records)
            identities = [id(record) for record in records]
            for stat, field in (("Average", 1), ("Home Run", 2), ("RBI", 3)):
                expected = [record[0] for record in sorted(
                    records, key=lambda record: record[field], reverse=True
                )]
                with patch("builtins.sorted", side_effect=AssertionError("Used built-in sort")):
                    result = rank(records, stat)
                self.assertEqual(result, expected)
                self.assertIsNot(result, records)
                self.assertEqual(records, original)
                self.assertEqual([id(record) for record in records], identities)
                self.assertIsNot(rank(records, stat), result)
        module = load(BASEBALL)
        for stat, field in (("Average", 1), ("Home Run", 2), ("RBI", 3)):
            expected = [record[0] for record in sorted(
                ORIGINAL_PLAYERS, key=lambda record: record[field], reverse=True
            )]
            self.assertEqual(rank(module["playerList"], stat), expected)
        records = [("same", 0, 0, 0), ("same", 1, 1, 1)]
        self.assertEqual(rank(records, "Average"), ["same", "same"])
        tree = ast.parse((ROOT / BASEBALL / "solution/main.py").read_text())
        calls = [node.func for node in ast.walk(tree) if isinstance(node, ast.Call)]
        self.assertFalse(any(isinstance(node, ast.Attribute) and node.attr == "sort"
                             for node in calls))

    def test_ranking_rejects_unknown_keys_and_every_invalid_record_domain(self):
        rank = load(BASEBALL)["bubble_baseball"]
        for stat in ("average", "", None, 1, True, ["Average"]):
            with self.assertRaises(ValueError):
                rank([], stat)
        for players in (None, "players", (), {}):
            with self.assertRaises(ValueError):
                rank(players, "Average")
        malformed = [[], ["a", 0.5, 1], "a", None, ["a", 0.5, 1, 1, 1]]
        malformed += [[name, 0.5, 1, 1] for name in ("", " \t", None, 1)]
        malformed += [["a", avg, 1, 1] for avg in
                      (-0.1, 1.1, float("nan"), float("inf"), True, "0.5", None, 10 ** 400)]
        for field in (2, 3):
            for value in (-1, 1.0, True, float("nan"), None, "1"):
                record = ["a", 0.5, 1, 1]
                record[field] = value
                malformed.append(record)
        for bad in malformed:
            records = [["valid", 0.5, 1, 1], bad]
            before = copy.deepcopy(records)
            with self.subTest(record=bad), self.assertRaisesRegex(ValueError, "record 2"):
                rank(records, "Average")
            self.assertEqual(records, before)

    def test_leaderboard_display_and_guarded_demo_preserve_data(self):
        module = load(BASEBALL)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertIsNone(module["print_list"](["first", "second"]))
            self.assertIsNone(module["print_list"]([]))
        self.assertEqual(output.getvalue(), "\tfirst\n\tsecond\n")
        for invalid in (None, "name", ["valid", 1]):
            output = io.StringIO()
            with contextlib.redirect_stdout(output), self.assertRaises(ValueError):
                module["print_list"](invalid)
            self.assertEqual(output.getvalue(), "")
        before = copy.deepcopy(module["playerList"])
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertIsNone(module["main"]())
        self.assertEqual(module["playerList"], before)
        self.assertEqual(sum(line.startswith("\t") for line in output.getvalue().splitlines()), 30)
        result = subprocess.run(
            [sys.executable, "-B", str(ROOT / BASEBALL / "solution/main.py")],
            capture_output=True, text=True, check=True, timeout=5
        )
        for stat in ("Average", "Home Run", "RBI"):
            self.assertIn(stat + " Leaderboard:", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_dictionary_whitespace_empty_values_duplicate_keys_and_independent_oracle(self):
        parse = load(DICTIONARY)["parse_pairs"]
        for n in range(7):
            for keys in product(("a", "b"), repeat=n):
                values = [str(index) for index in range(n)]
                lines = [item for pair in zip(keys, values) for item in pair]
                before = lines.copy()
                result = parse(lines)
                self.assertEqual(result, dict(zip(keys, values)))
                self.assertEqual(lines, before)
                self.assertIsNot(result, parse(lines))
        self.assertEqual(parse([" key \r\n", "  two words \t\n", "empty", " \t"]),
                         {"key": "two words", "empty": ""})
        self.assertEqual(parse(["é", "🙂", "é\r", "new"]), {"é": "new"})

    def test_dictionary_rejects_malformed_records_with_actual_line_numbers(self):
        parse = load(DICTIONARY)["parse_pairs"]
        for lines, number in ((["one"], 1), (["key", "value", "last"], 3),
                              ([" \t", "value"], 1), (["a", "1", "", "2"], 3),
                              (["a\nb", "1"], 1), (["a", "1\r\n\n"], 2)):
            original = lines.copy()
            with self.assertRaisesRegex(ValueError, "line " + str(number)):
                parse(lines)
            self.assertEqual(lines, original)
        for lines in (None, "a\nb", ("a", "b"), ["a", 1]):
            with self.assertRaises(ValueError):
                parse(lines)

    def test_dictionary_file_loading_original_fixture_and_exact_bytes(self):
        module = load(DICTIONARY)
        expected = dict(zip(
            ("dessert", "sport", "technology", "food", "country", "state",
             "container", "person", "tool", "superhero"),
            ("cake", "soccer", "computer", "pizza", "france", "idaho",
             "basket", "bob", "hammer", "ironman")
        ))
        self.assertEqual(module["load_pairs"](ROOT / DICTIONARY / "starter/input.txt"), expected)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.txt"
            cases = [(b"", {}), (b"a\nb\nc\nd", {"a": "b", "c": "d"}),
                     (b"a\r\nb\r\na\r\nlast\r\n", {"a": "last"}),
                     (b"a\n\n", {"a": ""})]
            for data, result in cases:
                path.write_bytes(data)
                self.assertEqual(module["load_pairs"](path), result)
                self.assertEqual(path.read_bytes(), data)
            for data in (b"a\n", b" \r\nb", b"a\nb\nc"):
                path.write_bytes(data)
                with self.assertRaises(ValueError):
                    module["load_pairs"](path)
                self.assertEqual(path.read_bytes(), data)
            with self.assertRaises(FileNotFoundError):
                module["load_pairs"](Path(directory) / "missing")
            path.write_bytes(b"a\n\xff")
            with self.assertRaises(UnicodeDecodeError):
                module["load_pairs"](path)

    def test_dictionary_context_closes_on_success_and_error_without_output_writes(self):
        module = load(DICTIONARY)
        for data, valid in (("a\nb", True), ("a", False)):
            handle = io.StringIO(data)
            with patch("builtins.open", return_value=handle) as opened:
                if valid:
                    self.assertEqual(module["load_pairs"](), {"a": "b"})
                else:
                    with self.assertRaises(ValueError):
                        module["load_pairs"]()
            self.assertTrue(handle.closed)
            opened.assert_called_once_with("input.txt", encoding="utf-8")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.txt"
            path.write_bytes(b"a\nb")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(module["main"](path), {"a": "b"})
            self.assertEqual(output.getvalue(), "{'a': 'b'}\n")
            result = subprocess.run(
                [sys.executable, "-B", str(ROOT / DICTIONARY / "solution/main.py")],
                cwd=directory, capture_output=True, text=True, check=True, timeout=5
            )
            self.assertEqual(result.stdout, output.getvalue())
            self.assertEqual(result.stderr, "")
            self.assertEqual(sorted(p.name for p in Path(directory).iterdir()), ["input.txt"])

    def test_latin_core_character_rule_all_small_tokens_case_unicode_and_errors(self):
        translate = load(LATIN)["translate"]
        cases = ["".join(chars) for n in range(6) for chars in product("Aéb", repeat=n)]
        cases += ["wasn’t", "can't", "co-op", "🙂é", "x1", "hello!", "UnknownWord"]
        for word in cases:
            self.assertEqual(translate(word), word_oracle(word))
        self.assertEqual(translate("Cat"), "atCay")
        for word in (None, 1, False, "two words", "a\tb", "a\n", "\u2003"):
            with self.assertRaises(ValueError):
                translate(word)

    def test_optional_punctuation_clusters_only_tokens_and_internal_apostrophes(self):
        translate = load(LATIN)["translate_punctuation"]
        for prefix in ("", "(", "\"", "([“", "‘"):
            for suffix in ("", ".", "?!", "…”])", "’"):
                for word in ("Cat", "a", "wasn’t", "can't", "co-op", "é🙂"):
                    self.assertEqual(translate(prefix + word + suffix),
                                     prefix + word_oracle(word) + suffix)
        for word in ("", "...", "?!", "([“”])", "‘’…", "'\""):
            self.assertEqual(translate(word), word)
        for word in (None, False, "a b", "\t"):
            with self.assertRaises(ValueError):
                translate(word)

    def test_latin_line_shape_whitespace_case_and_optional_selection(self):
        module = load(LATIN)
        lines = ["  Cat\t dog  ", "", " \t ", "wasn’t good", "Hello!"]
        before = lines.copy()
        expected = ["atCay ogday", "", "", "asn’tway oodgay", "ello!Hay"]
        self.assertEqual(module["translate_lines"](lines), expected)
        self.assertEqual(module["translate_lines"](lines, True)[-1], "elloHay!")
        self.assertEqual(lines, before)
        self.assertIsNot(module["translate_lines"](lines), lines)
        self.assertEqual(module["translate_lines"]([]), [])
        for invalid in (None, "line", ("line",), [1], ["line\n"], ["line\r"]):
            with self.assertRaises(ValueError):
                module["translate_lines"](invalid)
        with self.assertRaisesRegex(ValueError, "line 2"):
            module["translate_lines"](["valid", "two\nlines"])
        for flag in (0, 1, None, "yes"):
            with self.assertRaises(ValueError):
                module["translate_lines"]([], flag)
        with patch.dict(module["translate_lines"].__globals__,
                        {"translate_punctuation": lambda word: "optional"}):
            self.assertEqual(module["translate_lines"](["Cat"], False), ["atCay"])
            self.assertEqual(module["translate_lines"](["Cat"], True), ["optional"])

    def test_latin_reads_physical_lines_and_writes_defined_lf_bytes(self):
        module = load(LATIN)
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / "input.txt", Path(directory) / "output.txt"
            for data, lines in ((b"", []), (b"Cat\r\n\r\ndog", ["Cat", "", "dog"]),
                                (b"Cat\n", ["Cat"]), (b"\n", [""]),
                                (b"  Cat\t dog\r\n", ["  Cat\t dog"])):
                source.write_bytes(data)
                self.assertEqual(module["read_lines"](source), lines)
                translated = module["translate_file"](source, target)
                expected = [" ".join(word_oracle(token) for token in line.split()) for line in lines]
                self.assertEqual(translated, expected)
                self.assertEqual(target.read_bytes(), "".join(line + "\n" for line in expected).encode())
                self.assertEqual(source.read_bytes(), data)
            self.assertIsNone(module["write_lines"](["é", "", "literal space "], target))
            self.assertEqual(target.read_bytes(), "é\n\nliteral space \n".encode())
            self.assertIsNone(module["write_lines"]([], target))
            self.assertEqual(target.read_bytes(), b"")

    def test_latin_invalid_data_and_missing_input_preserve_existing_output(self):
        module = load(LATIN)
        with tempfile.TemporaryDirectory() as directory:
            source, target = Path(directory) / "input.txt", Path(directory) / "output.txt"
            original = b"keep existing output\n"
            target.write_bytes(original)
            for invalid in (None, "line", [1], ["valid", "embedded\nrecord"], ["\r"]):
                with self.assertRaises(ValueError):
                    module["write_lines"](invalid, target)
                self.assertEqual(target.read_bytes(), original)
            with self.assertRaises(FileNotFoundError):
                module["translate_file"](source, target)
            self.assertEqual(target.read_bytes(), original)
            source.write_bytes(b"\xff")
            with self.assertRaises(UnicodeDecodeError):
                module["translate_file"](source, target)
            self.assertEqual(target.read_bytes(), original)
            self.assertEqual(source.read_bytes(), b"\xff")
            source.write_bytes(b"Cat")
            for flag in (0, 1, "yes", None):
                with self.assertRaises(ValueError):
                    module["translate_file"](source, target, flag)
                self.assertEqual(target.read_bytes(), original)
                self.assertEqual(source.read_bytes(), b"Cat")

    def test_latin_same_path_equivalent_path_symlink_and_hardlink_aliases_are_rejected(self):
        translate = load(LATIN)["translate_file"]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.txt"
            source.write_bytes(b"Cat\r\ndog")
            link, hardlink = root / "symbolic.txt", root / "hard.txt"
            link.symlink_to(source)
            os.link(source, hardlink)
            for target in (source, str(root) + "/./input.txt", link, hardlink):
                with self.assertRaises(ValueError):
                    translate(source, target)
                self.assertEqual(source.read_bytes(), b"Cat\r\ndog")
                self.assertEqual(Path(target).read_bytes(), source.read_bytes())

    def test_latin_context_managers_close_and_validate_before_opening_output(self):
        module = load(LATIN)
        source = io.StringIO("Cat\n\n")
        with patch("builtins.open", return_value=source):
            self.assertEqual(module["read_lines"](), ["Cat", ""])
        self.assertTrue(source.closed)
        target = io.StringIO()
        with patch("builtins.open", return_value=target) as opened:
            self.assertIsNone(module["write_lines"](["Cat"]))
        self.assertTrue(target.closed)
        opened.assert_called_once_with("output.txt", "w", encoding="utf-8", newline="\n")
        with patch("builtins.open", side_effect=AssertionError("Opened invalid output")):
            with self.assertRaises(ValueError):
                module["write_lines"](["invalid\n"])

    def test_latin_default_direct_run_and_original_files_use_separate_read_paths(self):
        module = load(LATIN)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            core = root / "input_no_punctuation.txt"
            core.write_bytes(b"Cat dog\r\n\r\nA")
            result = subprocess.run(
                [sys.executable, "-B", str(ROOT / LATIN / "solution/main.py")],
                cwd=directory, capture_output=True, text=True, check=True, timeout=5
            )
            self.assertIn("Wrote output.txt", result.stdout)
            self.assertEqual(result.stderr, "")
            self.assertEqual((root / "output.txt").read_bytes(), b"atCay ogday\n\nAay\n")
            self.assertEqual(core.read_bytes(), b"Cat dog\r\n\r\nA")
            punctuation = root / "input_punctuation.txt"
            punctuation.write_text("Different, wasn’t!", encoding="utf-8")
            translated = module["translate_file"](punctuation, root / "bonus.txt", True)
            self.assertEqual(translated, ["ifferentDay, asn’tway!"])
            self.assertEqual((root / "bonus.txt").read_bytes(), "ifferentDay, asn’tway!\n".encode())
            for name, flag in (("input_no_punctuation.txt", False), ("input_punctuation.txt", True)):
                original = ROOT / LATIN / "starter" / name
                lines = module["read_lines"](original)
                self.assertEqual(len(lines), 13)
                output = module["translate_file"](original, root / "checked.txt", flag)
                self.assertEqual(len(output), 13)
                self.assertEqual((root / "checked.txt").read_text().splitlines(), output)
                if flag:
                    self.assertIn("asn’tway", output[10])


if __name__ == "__main__":
    unittest.main()
