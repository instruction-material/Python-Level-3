"""Implement the core file pipeline first; punctuation is a separate extension."""


def translate(word):
    """Move the first character of a nonempty token to its end, then add ay."""
    raise NotImplementedError("Implement translate, including the empty token")


def translate_punctuation(word):
    """Optionally preserve supported edge punctuation around the translated body."""
    raise NotImplementedError("Implement the optional punctuation extension")


def read_lines(path="input_no_punctuation.txt"):
    """Read UTF-8 physical lines without their newline delimiters."""
    raise NotImplementedError("Implement read_lines")


def translate_lines(lines, punctuation=False):
    """Translate tokens per line, intentionally normalizing whitespace within lines."""
    raise NotImplementedError("Implement translate_lines")


def write_lines(lines, path="output.txt"):
    """Validate all lines before writing UTF-8 output with LF record endings."""
    raise NotImplementedError("Implement write_lines")


def translate_file(input_path="input_no_punctuation.txt", output_path="output.txt",
                   punctuation=False):
    """Protect source aliases, then read, translate, write and return output lines."""
    raise NotImplementedError("Implement translate_file after testing its stages")


if __name__ == "__main__":
    print("Implement the core TODO functions in main.py; read README.md before running tests.")
