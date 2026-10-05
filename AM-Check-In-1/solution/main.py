"""Reference functions for the original strings, recursion and stack review."""

import random


def middle_letters(word):
    """Return a string without its first and last characters."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    return word[1:-1]


def second_word(sentence):
    """Return the second whitespace-delimited word of a valid sentence."""
    if not isinstance(sentence, str):
        raise ValueError("sentence must be a string")
    words = sentence.split()
    if len(words) < 2:
        raise ValueError("sentence must contain at least two words")
    return words[1]


def num_pins(rows):
    """Recursive row sum; practice with small nonnegative integers."""
    if isinstance(rows, bool) or not isinstance(rows, int) or rows < 0:
        raise ValueError("rows must be a nonnegative integer")
    if rows <= 1:
        return rows
    return rows + num_pins(rows - 1)


def lucas(n):
    """One-based naive recursive Lucas sequence beginning 2, 1."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def strange_function(n):
    print(n)
    if n > 2:
        strange_function(n - 1)
        strange_function(n - 2)


def make_word(keystrokes):
    """Return edited text; # on an empty stack does nothing."""
    if not isinstance(keystrokes, str):
        raise ValueError("keystrokes must be a string")
    stack = []
    for key in keystrokes:
        if key != "#":
            stack.append(key)
        elif stack:
            stack.pop()
    return "".join(stack)


makeWord = make_word
strangeFunction = strange_function


def main():
    word = input("Enter a word: ")
    print("The middle letters: " + middle_letters(word))
    sentence = input("Enter a sentence with at least two words: ")
    print("The second word of the sentence: " + second_word(sentence))
    print("The number of pins for 2 rows:", num_pins(2))
    print("The fourth Lucas number is:", lucas(4))
    nums = [1, 2, 3, 4, 5]
    nums.append(random.randint(1, 10))
    print("after adding a random number:")
    print(nums)
    nums.pop()
    print("after removing the top element:")
    print(nums)


if __name__ == "__main__":
    main()
