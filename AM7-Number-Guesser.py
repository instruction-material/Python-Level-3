"""
Write a program that selects a random integer from 1 to 100, and then allows the user to guess what the number is. If the user guesses the answer, the program terminates. If the guess is incorrect, the program prints whether the guess was too high or too low.
"""

import random


print("I'm thinking of a number between 1-100. \nYou get 7 guesses to get it right. Go!")

number = random.randint(1, 100)

numGuess = 7
while numGuess > 0:
	guess = int(input("You have " + str(numGuess) + " guesses left. Guess my number! "))
	
	if guess == number:
		print("You win! Congrats! " + str(number) + " was my number!")
		break
	elif guess > number:
		print("Nope! That guess was too high.")
	else:  # guess < number
		print("Nope! That guess was too low.")
	
	numGuess -= 1

if numGuess == 0:
	print("Sorry! You ran out of guesses.")
