"""The original Juni Latin character rule, with a separate punctuation extension."""

import os
from pathlib import Path
import string


EDGE_PUNCTUATION = string.punctuation + "“”‘’…"


def _token(word):
    if not isinstance(word, str) or any(character.isspace() for character in word):
        raise ValueError("word must be a whitespace-free string, or the empty string")


def _lines(lines):
    if not isinstance(lines, list) or not all(isinstance(line, str) for line in lines):
        raise ValueError("lines must be a list of strings")
    for number, line in enumerate(lines, 1):
        if "\r" in line or "\n" in line:
            raise ValueError("line " + str(number) + " must exclude its record delimiter")


def translate(word):
    """Move the first character of a nonempty token to its end, then add ay."""
    _token(word)
    if not word:
        return ""
    return word[1:] + word[0] + "ay"


def translate_punctuation(word):
    """Optionally preserve supported edge punctuation around the translated body."""
    _token(word)
    start, end = 0, len(word)
    while start < end and word[start] in EDGE_PUNCTUATION:
        start += 1
    while end > start and word[end - 1] in EDGE_PUNCTUATION:
        end -= 1
    if start == end:
        return word
    return word[:start] + translate(word[start:end]) + word[end:]


def read_lines(path="input_no_punctuation.txt"):
    """Read UTF-8 physical lines without their newline delimiters."""
    with open(path, encoding="utf-8") as source:
        return [line.removesuffix("\n") for line in source]


def translate_lines(lines, punctuation=False):
    """Translate tokens per line, intentionally normalizing whitespace within lines."""
    _lines(lines)
    if type(punctuation) is not bool:
        raise ValueError("punctuation must be a Boolean")
    translator = translate_punctuation if punctuation else translate
    return [" ".join(translator(word) for word in line.split()) for line in lines]


def write_lines(lines, path="output.txt"):
    """Validate all lines before writing UTF-8 output with LF record endings."""
    _lines(lines)
    with open(path, "w", encoding="utf-8", newline="\n") as output:
        for line in lines:
            output.write(line + "\n")


def translate_file(input_path="input_no_punctuation.txt", output_path="output.txt",
                   punctuation=False):
    """Protect source aliases, then read, translate, write and return output lines."""
    source, target = Path(input_path), Path(output_path)
    if source.resolve() == target.resolve():
        raise ValueError("input and output must be different files")
    if source.exists() and target.exists() and os.path.samefile(source, target):
        raise ValueError("input and output must be different files")
    translated = translate_lines(read_lines(source), punctuation)
    write_lines(translated, target)
    return translated


if __name__ == "__main__":
    translate_file()
    print("Wrote output.txt; input_no_punctuation.txt is unchanged.")
