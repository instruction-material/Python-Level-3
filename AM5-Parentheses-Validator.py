"""
Write a function that takes in a string made up entirely of parentheses (), braces {}, and brackets [] (we’ll just call all of those things together “parentheses”), and returns True if the expression is valid, and False if it is not. An expression is valid if the parentheses are balanced; an example of an expression with balanced parentheses is “([]{})” as well as “((([])))”, while “([]{)}” is not balanced. In technical terms, each opening symbol has a corresponding closing symbol, and the pairs of parentheses are properly nested.
"""


# iterative way
def parentheses(brackets):
	dictionary = {"(": ")", "[": "]", "{": "}"}
	stack = []
	
	if len(brackets) == 0:
		return True
	
	for ch in brackets:
		if ch in dictionary:
			stack.append(ch)
		elif ch in dictionary.values():
			if len(stack) == 0:
				return False
			elif dictionary[stack.pop()] != ch:
				return False
	
	if len(stack) == 0:
		return True
	else:
		return False


print(parentheses("{()[]}"))
print(parentheses("{()[])"))


# recursive way
def recParentheses(brackets):
	if len(brackets) == 0:
		return True
	
	for i in range(len(brackets) - 1):
		check = brackets[i] + brackets[i + 1]
		if check == "()" or check == "{}" or check == "[]":
			newBracks = brackets[:i] + brackets[i + 2:]
			return recParentheses(newBracks)
	
	return False


print(recParentheses("{()[]}"))
print(recParentheses("{(((())))[}]"))
