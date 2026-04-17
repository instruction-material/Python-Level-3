"""
Using what you have learned about variables, strings, and input, create your own Mad Lib story. A Mad Lib consists of asking the user to enter words of different types (such as nouns, adjectives, verbs, etc.), and then using those words to fill in the story. If you have never heard of Mad Libs before, you can try one by clicking here. How would you collect the words in order to fill in the story? How would you put the user’s words with the words that don’t change?
"""

# Example mad lib: http://www.madtakes.com/libs/176.html
adjective = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
verb2 = input("Enter another verb, in past tense: ")

print(
	'The cafeteria at our school is very ' + adjective + '. For example, they serve ' + adjective2 + ' pizza. They also serve ' + noun + '. One time, I saw somebody ' + verb + ' across the cafeteria. Everybody ' + verb2 + '!')
