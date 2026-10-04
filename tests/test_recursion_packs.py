"""Assignment-specific reference checks; not imported into learner starters."""

import contextlib
import io
from itertools import product
import unittest

from test_algorithm_packs import load_module


def printed(function, argument):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        result = function(argument)
    if result is not None:
        raise AssertionError("This exercise prints rather than returning a result.")
    return output.getvalue().splitlines()


def balanced_brackets(text):
    closing_to_opening = {")": "(", "]": "[", "}": "{"}
    stack = []
    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in closing_to_opening:
            if not stack or stack.pop() != closing_to_opening[character]:
                return False
        else:
            return False
    return not stack


class RecursionPackTests(unittest.TestCase):
    def test_cascade_orders_and_empty_input(self):
        module = load_module("AM5-Recursive-Cascade", "solution")
        for text in ("", "a", "dog", "abba", "あい"):
            expected = [text[:length] for length in range(1, len(text) + 1)]
            with self.subTest(text=text):
                self.assertEqual(printed(module["cascade"], text), expected)
                self.assertEqual(printed(module["inverse_cascade"], text), expected[::-1])

    def test_palindrome_is_literal_and_case_sensitive(self):
        palindrome = load_module("AM5-Recursive-Palindrome-Checker", "solution")[
            "is_palindrome"
        ]
        for text in ("", "a", "aa", "abba", "abc", "racecar", "Aa", "a a", "あいいあ"):
            with self.subTest(text=text):
                self.assertIs(palindrome(text), text == text[::-1])

    def test_bracket_algorithms_agree_on_valid_and_invalid_strings(self):
        module = load_module("AM5-Parentheses-Validator", "solution")
        texts = ["a", "(a)", "a()", "([])", "([)]", "(()", "())", " "]
        for length in range(5):
            texts.extend("".join(chars) for chars in product("()[]{}", repeat=length))
        for text in texts:
            expected = balanced_brackets(text)
            for name in ("parentheses", "rec_parentheses"):
                with self.subTest(text=text, function=name):
                    self.assertIs(module[name](text), expected)

    def test_recursive_sum_and_maximum_boundaries(self):
        module = load_module("AM5-Recursive-Sum-and-Max", "solution")
        lists = [[], [4], [0, 0], [1, 2, 3], [-8, -3, -5], [3, -4, 9, 9], [0.5, 1.25]]
        for values in lists:
            original = values[:]
            with self.subTest(values=values):
                self.assertEqual(module["sum_recursion"](values), sum(values))
                if values:
                    self.assertEqual(module["max_recursion"](values), max(values))
                else:
                    with self.assertRaises(ValueError):
                        module["max_recursion"](values)
                self.assertEqual(values, original)

    def test_substrings_are_contiguous_unique_and_stable(self):
        substrings = load_module("AM5-Substring-Generator", "solution")["get_substrings"]
        for text in ("", "a", "ab", "aba", "abc", "aaaa", "あいう"):
            expected = sorted(
                {text[start:end] for start in range(len(text) + 1) for end in range(start, len(text) + 1)}
            )
            with self.subTest(text=text):
                self.assertEqual(substrings(text), expected)
                self.assertEqual(substrings(text), expected)
        self.assertNotIn("ac", substrings("abc"))

    def test_running_sum_orders_and_empty_input(self):
        module = load_module("AM-Check-In-1-Additional-Project", "solution")
        for values in ([], [4], [4, 5, 2], [-1, -4, 8], [0, 0, 2], [0.5, 1.25]):
            expected = []
            running = 0
            for value in values:
                running += value
                expected.append(str(running))
            original = values[:]
            with self.subTest(values=values):
                self.assertEqual(printed(module["sum_print"], values), expected)
                self.assertEqual(printed(module["sum_print_reverse"], values), expected[::-1])
                self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
