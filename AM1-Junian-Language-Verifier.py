"""
Write a program that takes in an input string from the user, and then outputs whether or not that input string is a valid word according to the Junian Language. A string is valid in Junian if:
It has an even amount of characters.
It contains at least 2 vowels.
The first letter is different from the last letter.
For example, "Juni" is valid in Junian.
"""

word = input("Please type in a word for verification: ")

vowels = "aeiou"
numVowels = 0

for letter in word:
	if letter in vowels:
		numVowels += 1

if numVowels < 2:
	print("Your word is invalid.")
elif len(word) % 2 != 0:
	print("Your word is invalid.")
elif word[0] == word[len(word) - 1]:  # Optionally, introduce word[-1]
	print("Your word is invalid.")
else:
	print("Your word is valid.")
