"""ASCII file-sorting review. Read README.md and retain the supplied input.txt."""


def read_letters(path="input.txt"):
    """Read one ASCII character per record; reject malformed lines deliberately."""
    raise NotImplementedError("Implement read_letters before calling it.")


def sort_letters(letters):
    """Return a fresh ASCII-ordered list using an earlier sorting algorithm."""
    raise NotImplementedError("Implement sort_letters before calling it.")


def write_letters(letters, path="output.txt"):
    """Validate then write one ASCII character per line; retain duplicates."""
    raise NotImplementedError("Implement write_letters before calling it.")


def sort_file(input_path="input.txt", output_path="output.txt"):
    """Reject input/output aliases; validate before writing; retain the input."""
    raise NotImplementedError("Implement sort_file before calling it.")


if __name__ == "__main__":
    print("Implement the file/sort TODOs; then call sort_file() from this direct-run guard.")
