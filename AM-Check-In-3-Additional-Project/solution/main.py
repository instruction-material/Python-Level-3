"""One-ASCII-character-per-record file sorting, with explicit failure policies."""

import os
from pathlib import Path


def _character(value):
    return (isinstance(value, str) and len(value) == 1
            and ord(value) < 128 and value not in "\r\n")


def _letters(letters):
    if not isinstance(letters, list) or not all(_character(c) for c in letters):
        raise ValueError("letters must be a list of single ASCII characters, excluding CR/LF")


def read_letters(path="input.txt"):
    result = []
    with open(path, encoding="utf-8") as source:
        for number, line in enumerate(source, 1):
            character = line.removesuffix("\n")
            if not _character(character):
                raise ValueError("line " + str(number) + " must contain one ASCII character")
            result.append(character)
    return result


def sort_letters(letters):
    _letters(letters)
    result = letters.copy()
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for j in range(end):
            if ord(result[j]) > ord(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def write_letters(letters, path="output.txt"):
    _letters(letters)
    with open(path, "w", encoding="utf-8", newline="\n") as output:
        for character in letters:
            output.write(character + "\n")


def sort_file(input_path="input.txt", output_path="output.txt"):
    source, target = Path(input_path), Path(output_path)
    if source.resolve() == target.resolve():
        raise ValueError("input and output must be different files")
    if source.exists() and target.exists() and os.path.samefile(source, target):
        raise ValueError("input and output must be different files")
    letters = sort_letters(read_letters(source))
    write_letters(letters, target)
    return letters


if __name__ == "__main__":
    sort_file()
    print("Wrote output.txt; input.txt is unchanged.")
