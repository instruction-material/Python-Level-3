import random

print("I'm thinking of a number between 1-100. \nYou get 7 guesses to get it right. Go!")

number = random.randint(1, 100)

num_guess = 7
while num_guess > 0:
    guess = int(input("You have " + str(num_guess) + " guesses left. Guess my number! "))

    if guess == number:
        print("You win! Congrats! " + str(number) + " was my number!")
        break
    elif guess > number:
        print("Nope! That guess was too high.")
    else:  # guess < number
        print("Nope! That guess was too low.")

    num_guess -= 1

if num_guess == 0:
    print("Sorry! You ran out of guesses.")
