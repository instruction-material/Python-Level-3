"""
Write a recursive function that takes in a number and returns the factorial of the number. In math, the factorial of a number n is written n!, and is defined to be n * (n - 1) * (n - 2) * … * 3 * 2 * 1. For example, if n = 5, then n! = 5 * 4 * 3 * 2 * 1.

What is the base case? (This would be the smallest possible input that we could expect.) How do we modify the input when we make the recursive call?
"""


def recursive_factorial(num):
	if num == 0:
		return 1
	return num * recursive_factorial(num - 1)


print(recursive_factorial(5))
