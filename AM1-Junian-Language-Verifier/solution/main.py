def verification_errors(word):
    """Return failed rules; letter comparisons and vowel counts ignore case."""
    normalized = word.lower()
    errors = []
    if len(word) % 2 != 0:
        errors.append("The word must have an even number of characters.")

    num_vowels = 0
    for letter in normalized:
        if letter in "aeiou":
            num_vowels += 1
    if num_vowels < 2:
        errors.append("The word must contain at least two vowels.")

    if normalized and normalized[0] == normalized[-1]:
        errors.append("The first and last letters must be different.")
    return errors


def run_verifier():
    word = input("Please type in a word for verification: ")
    errors = verification_errors(word)
    if errors:
        print("Your word is invalid.")
        for error in errors:
            print(error)
    else:
        print("Your word is valid.")


if __name__ == "__main__":
    run_verifier()
