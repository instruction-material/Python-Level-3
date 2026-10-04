def get_substrings(string):
    if len(string) == 0:
        return [string]
    substrings = [string]

    new_substrings = substrings

    result1 = get_substrings(string[1:])
    for substr in result1:
        new_substrings.append(substr)

    result2 = get_substrings(string[:-1])
    for substr in result2:
        new_substrings.append(substr)

    set_subs = set(new_substrings)  # convert to set to delete duplicates
    substrings = sorted(set_subs)  # a stable list of contiguous substrings
    return substrings


if __name__ == "__main__":
    print(get_substrings("abcde"))
