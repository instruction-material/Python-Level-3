###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

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
    substrings = list(set_subs)  # convert back to list
    return substrings


print(get_substrings("abcde"))
