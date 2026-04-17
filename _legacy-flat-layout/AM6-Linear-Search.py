"""
Write a function that takes in a list and a target value, and looks for that value in the list. Return True if the value is in the list, and False if it is not. (Note: you should do this without using the in keyword.)
"""


def linearSearch(arr, val):
	for item in arr:
		if item == val:
			return True
	return False


nums = [1, 2, 3, 4, 5]
print(linearSearch(nums, 4))
print(linearSearch(nums, 6))
