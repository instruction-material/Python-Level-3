"""Separate reference for literal name transformations and deliberate file writes."""

import os
from pathlib import Path


def name_variations(name):
    """Return literal, alternate-index and reversed names; validate the name."""
    if not isinstance(name, str) or "\r" in name or "\n" in name:
        raise ValueError("name must be a string without CR or LF")
    try:
        name.encode("utf-8")
    except UnicodeEncodeError as error:
        raise ValueError("name must be UTF-8 encodable") from error
    return (name, name[::2], name[::-1])


def format_tags(name):
    """Return the three sections, one LF per character and after each section."""
    return "".join(
        "".join(character + "\n" for character in variation) + "\n"
        for variation in name_variations(name)
    )


def _destination(path):
    try:
        value = os.fspath(path)
        if not isinstance(value, str) or not value or "\0" in value:
            raise ValueError("path must be a nonempty string or text PathLike without NUL")
        value.encode("utf-8")
    except (TypeError, UnicodeEncodeError) as error:
        raise ValueError("path must be UTF-8 encodable text") from error
    return value


def write_tags(name, path="output.txt"):
    """Validate before opening, then write the core UTF-8/LF file and return None."""
    text = format_tags(name)
    destination = _destination(path)
    with open(destination, "w", encoding="utf-8", newline="\n") as output:
        output.write(text)


def main(path="output.txt", input_fn=None, output_fn=None):
    """Prompt once, handle cancellation/errors, and return the documented outcome."""
    destination = _destination(path)
    read = input if input_fn is None else input_fn
    report = print if output_fn is None else output_fn
    if not callable(read) or not callable(report):
        raise ValueError("input_fn and output_fn must be callable or None")
    try:
        name = read("What is your name? ")
    except (EOFError, KeyboardInterrupt):
        report("Cancelled; no output was opened.")
        return {"status": "cancelled", "path": destination}
    try:
        write_tags(name, destination)
    except ValueError as error:
        report(f"Invalid name; no output was opened: {error}")
        status = "invalid"
    except OSError as error:
        report(f"Writing failed: {error}")
        status = "failed"
    else:
        report(f"Wrote name tags to {destination}.")
        status = "written"
    return {"status": status, "path": destination}


def write_separate_tags(name, paths=("output1.txt", "output2.txt", "output3.txt")):
    """Optional: validate three distinct destinations before writing separate tags."""
    variations = name_variations(name)
    if not isinstance(paths, (list, tuple)) or len(paths) != 3:
        raise ValueError("paths must be a list or tuple of three destinations")
    destinations = [_destination(path) for path in paths]
    for index, destination in enumerate(destinations):
        for other in destinations[:index]:
            if Path(destination).resolve() == Path(other).resolve() or (
                os.path.exists(destination) and os.path.exists(other)
                and os.path.samefile(destination, other)
            ):
                raise ValueError("separate tags require three distinct destinations")
    texts = ["".join(character + "\n" for character in part) for part in variations]
    for destination, text in zip(destinations, texts):
        with open(destination, "w", encoding="utf-8", newline="\n") as output:
            output.write(text)


if __name__ == "__main__":
    main()
