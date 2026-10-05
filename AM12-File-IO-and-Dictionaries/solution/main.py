"""Alternating-line dictionary parsing with deliberate malformed-record policies."""


def parse_pairs(lines):
    """Convert alternating string records to pairs using the documented policies."""
    if not isinstance(lines, list) or not all(isinstance(line, str) for line in lines):
        raise ValueError("lines must be a list of string records")
    records = []
    for number, line in enumerate(lines, 1):
        if line.endswith("\r\n"):
            line = line[:-2]
        elif line.endswith(("\r", "\n")):
            line = line[:-1]
        if "\r" in line or "\n" in line:
            raise ValueError("line " + str(number) + " contains an extra record delimiter")
        records.append(line.strip())
    if len(records) % 2:
        raise ValueError("line " + str(len(records)) + " has a key without a value")
    result = {}
    for index in range(0, len(records), 2):
        key, value = records[index:index + 2]
        if not key:
            raise ValueError("line " + str(index + 1) + " must contain a nonblank key")
        result[key] = value
    return result


def load_pairs(path="input.txt"):
    """Read UTF-8 records with a context manager and return the parsed dictionary."""
    with open(path, encoding="utf-8") as source:
        return parse_pairs(source.readlines())


def main(path="input.txt"):
    """Print and return the loaded dictionary, without writing a data file."""
    result = load_pairs(path)
    print(result)
    return result


if __name__ == "__main__":
    main()
