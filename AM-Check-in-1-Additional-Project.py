"""
Write a recursive function that takes in a list of numbers and prints out the first number, then the sum of the first two numbers, then the sum of the first three numbers, and so on up to the sum of all of the numbers in the list.
Write another recursive function that takes in a list of numbers. If the list has n numbers, your function should print the sum of the first n numbers, then print the sum of the first n-1 numbers, then the sum of the first n-2 numbers, and so on until it prints just the first number.
Note: You are allowed to use the built-in sum() function in your code!
"""


# Write a recursive function that takes in a list of numbers and prints out the first number, then the sum of the first two numbers, then the sum of the first three numbers, and so on up to the sum of all of the numbers in the list.

def sumPrint(nums):
	if len(nums) == 1:
		print(nums[0])
	else:
		sumPrint(nums[:-1])
		print(sum(nums))


sumPrint([4, 5, 2])


# Then, write another function that takes in a list of numbers. It should print the sum of all of the numbers then print the sum of the first n-1 numbers then the sum of the first n-2 numbers and so on until it prints just the first number (Notice that this function prints the same thing as the first, just in reverse).

def sumPrintReverse(nums):
	if len(nums) == 1:
		print(nums[0])
	else:
		print(sum(nums))
		sumPrintReverse(nums[:-1])


sumPrintReverse([4, 5, 2])
