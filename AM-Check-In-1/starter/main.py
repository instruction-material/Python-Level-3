# FUNCTIONS

# Ask the user for a word. Print out the middle letters of the word (not including the first and last)

# Ask the user to enter a sentence with at least two words. Print out the second word in the sentence.


# RECURSION

# What is a recursive function? What are the two key parts of any recursive function?

# Write a function that takes in a number of rows of a pyramid and returns the number of bowling pins needed to make a pyramid with that number of rows.

# Write a recursive function to calculate the nth Lucas number. The Lucas numbers are very similar to the Fibonacci numbers because each Lucas number is the sum of the previous two. The only difference is that the Lucas number sequence starts with 2 1 instead of 0 1. The first few Lucas numbers are:  2 1 3 4 7 11 ...


# What will be printed if we call strangeFunction(4)?
def strangeFunction(n):
    print(n)
    if n > 2:
        strangeFunction(n - 1)
        strangeFunction(n - 2)


# Once you have an answer, uncomment the next line to test if it is correct!
# strangeFunction(4)


# STACKS

# What is a stack? How is it different from a list?

# Create a stack called nums with the numbers from 1-5 stored in it.

# Add a random number to the top of the stack. Print the stack out.

# Remove the top element of the stack then print the stack out.

# Write a function that takes in a string of key presses and returns the word that the key presses produce. A "#" in the key presses represents hitting the backspace button. Here are a few examples:
# makeWord("hi#") -> "h"
# makeWord("ok##") -> ""
# makeWord("ti#ger") -> "tger"
# makeWord("t###") -> ""


# Callable exercises: see README.md for domains and self-checks.

def middle_letters(word):
    """Return the middle of a string; empty/short words return an empty string."""
    raise NotImplementedError("Implement middle_letters before calling it.")


def second_word(sentence):
    """Return the second whitespace-delimited word; fewer than two raises ValueError."""
    raise NotImplementedError("Implement second_word before calling it.")


def num_pins(rows):
    """Recursively return the pin total for a nonnegative integer number of rows."""
    raise NotImplementedError("Implement num_pins before calling it.")


def lucas(n):
    """Recursively return the one-based Lucas term; n must be a positive integer."""
    raise NotImplementedError("Implement lucas before calling it.")


def make_word(keystrokes):
    """Process # as backspace, ignoring it when the stack is empty."""
    raise NotImplementedError("Implement make_word before calling it.")


def main():
    """Collect words and demonstrate the original push/pop stack tasks."""
    raise NotImplementedError("Implement main before calling it.")


# Preserve the names used in the original prompt and reference.
makeWord = make_word
strange_function = strangeFunction


if __name__ == "__main__":
    print("Implement the TODO functions and main; then replace this reminder with main().")
