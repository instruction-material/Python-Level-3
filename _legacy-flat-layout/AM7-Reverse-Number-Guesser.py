"""
Write a program that tries to determine the random integer from 1 to 100 that the user mentally selected. The program should use Binary Search to determine which numbers it should guess. After the computer makes a guess, the user should say whether the correct number is above or below the computer’s guess.
"""

guess = 50
low = 1
high = 100
numGuess = 0

print("Think of a whole number between 1 and 100, and I'll try to guess it in 7 guesses!")

while True:
	guess = (low + high) // 2
	if numGuess == 6:
		print("Your number must be " + str(guess) + "!")
		break
	elif low == high:
		print("Well then " + str(low) + " must be your number!")
		break
	else:
		print("\nIs your number " + str(guess) + "?")
		print("If not, is it above or below " + str(guess) + "?")
		answer = input("(Type 'yes', 'above' or 'below') ")
	
	numGuess += 1
	if answer == "above":
		low = guess + 1
	elif answer == "below":
		high = guess - 1
	else:
		break

print("I knew I'd guess it!")
