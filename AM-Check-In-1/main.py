import random

# Functions

# Func-1: Ask the user for a word. Then print out the middle letters of the word (not including the first and last)
word = input("Enter a word: ")
print("The middle letters: " + word[1:-1])

# Func-2: Ask the user to enter a sentence with at least two words. Then print out the second word in the sentence. 
sentence = input("Enter a sentence with at least two words: ")
print("The second word of the sentence: " + sentence.split()[1])
print()


# RECURSION

# Recursion-2: Write a function that takes in a number of rows of a pyramid and returns the number of bowling pins needed to make a pyramid with that number of rows. 
def numPins(rows):
    if rows <= 1:
        return rows
    return rows + numPins(rows - 1)


print("The number of pins for 2 rows:", numPins(2))


# Recursion-3: Write a recursive function to calculate the nth Lucas number. The Lucas numbers are very similar to the Fibonacci numbers because each Lucas number is the sum of the previous two. The only difference is that the Lucas number sequence starts with 2 1 instead of 0 1. The first few Lucas numbers are:  2 1 3 4 7 11 ...
def Lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return Lucas(n - 1) + Lucas(n - 2)


print("The fourth Lucas number is:", Lucas(4))


# Recursion-4: What will be printed if we call strangeFunction(4)?
def strangeFunction(n):
    print(n)
    if n > 2:
        strangeFunction(n - 1)
        strangeFunction(n - 2)


# strangeFunction(4)
# print()


# STACKS

# Stacks-2: Create a stack called nums with the numbers from 1-5 stored in it.
nums = [1, 2, 3, 4, 5]

# Stacks-3: Add a random number to the top of the stack.
nums.append(random.randint(1, 10))
print("after adding a random number:")
print(nums)

# Stacks-4: Remove the top element of the stack then print the stack out. 
nums.pop()
print("after removing the top element:")
print(nums)
print()


# Stacks-5: Write a function that takes in a string of key presses and returns the word that the key presses produce. A "#" in the key presses represents hitting the backspace button. Here are a few examples:
# makeWord("hi#") -> "h"
# makeWord("ok##") -> ""
# makeWord("ti#ger") -> "tger"
# makeWord("t###") -> ""
def makeWord(keystrokes):
    stack = []
    # loop through the keystrokes
    for key in keystrokes:
        if key != "#":  # if the key is not a backspace, add it to the word
            stack.append(key)
        elif len(stack) > 0:  # if the key is a backspace and stack isn't empty, pop the last letter
            stack.pop()
    # turn the stack into a string
    word = ""
    for letter in stack:
        word += letter
    return word
    # alternative way to turn list into string in python
    # return "".join(stack)
# print("makeWord('ti#ger') ->", makeWord("ti#ger"))
