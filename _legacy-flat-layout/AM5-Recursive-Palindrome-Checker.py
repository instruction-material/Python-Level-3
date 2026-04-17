"""
Write a recursive function that takes in a string and returns True if the string is a palindrome, and otherwise returns False. A palindrome is a word that reads the same when spelled forwards or backwards. For example, the word “racecar” is a palindrome, since it’s the same word spelled forwards or backwards.
"""


def isPalindrome(str):
	if len(str) <= 1:
		return True
	if str[0] != str[-1]:
		return False
	return isPalindrome(str[1:-1])


n = input("\n\nEnter the string you would like to check. \nWe will check if it is a palindrome. \n")
print(isPalindrome(n))
