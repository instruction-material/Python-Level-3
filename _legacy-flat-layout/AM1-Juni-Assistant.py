"""
Write a program that first prints a numbered list of instructions that the assistant can understand, and then prompts the user to specify which operation should be performed, and then finally performs the instruction designated by the entered number. Make the assistant continue to ask for commands until the user selects the “Quit” instruction (which you will need to include in your list of valid commands).
"""

import datetime
import random


print("Welcome to Juni Assistant!")

funFacts = ["The first oranges weren’t orange.",
            "There’s only one letter that doesn’t \nappear in any U.S. state name: Q.",
            "A cow-bison hybrid is called a 'beefalo'.", "Scotland has 421 words for 'snow'.",
            "Peanuts aren’t technically nuts."]
jokes = ["Today at the bank, an old lady asked me \nto help check her balance. \nSo I pushed her over.",
         "My dog used to chase people on a \nbike a lot. It got so bad, \nfinally I had to take his bike away.",
         "I'm so good at sleeping. \nI can do it with my eyes closed.",
         "Why is Peter Pan always flying? \nHe neverlands.",
         "My friend said to me: \n'What rhymes with orange' \nI said: 'No it doesn't"]

name = ""
keepGoing = True

while keepGoing:
	choice = input(
		"\nHow can I help you?\n 1. What time is it?\n 2. What is the date?\n 3. Remember my name\n 4. What is my name?\n 5. Fun fact\n 6. Tell me a joke.\n 7. Quit\n")
	
	currentDT = datetime.datetime.now()
	
	if choice[0] == "1":
		print(str(currentDT.hour) + ":" + str(currentDT.minute))
	elif choice[0] == "2":
		print(str(currentDT.month) + "/" + str(currentDT.day) + "/" + str(currentDT.year))
	elif choice[0] == "3":
		name = input("Please type in your name: ")
	elif choice[0] == "4":
		print("Your name is " + name)
	elif choice[0] == "5":
		print(funFacts[random.randint(0, len(funFacts) - 1)])
	elif choice[0] == "6":
		print(jokes[random.randint(0, len(funFacts) - 1)])
	elif choice[0] == "7":
		print("Goodbye!")
		keepGoing = False
	else:
		print("I'm sorry, I don't recognize that command.")
