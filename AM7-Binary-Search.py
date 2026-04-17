"""
Binary Search is an algorithm that looks for a target element in a sorted list. Write a function that takes in a sorted list and a number, and uses binary search to determine if that target number is in the list. The function returns True if the target value is in the list, and False otherwise.

If you want to split the list, use the same syntax that you used for substrings!
myList[i:] will grab the items starting at and including index i, all the way to the end of the list (the first index is inclusive).
myList[:i] will grab the items starting at index 0 all the way up to but not including i (the second index is exclusive).
"""


def binSearchIter(lst, item):
	low = 0
	high = len(lst) - 1
	
	while low <= high:
		mid = (high + low) // 2
		x = lst[mid]
		
		if x == item:
			return True
		elif x < item:  # Cannot be on left side
			low = mid + 1
		else:  # x > item, cannot be on right side
			high = mid - 1
	
	return False


def binSearchRecur(lst, item):
	high = len(lst) - 1
	
	if high < 0:  # The list is empty
		return False
	
	mid = high // 2
	
	if lst[mid] == item:
		return True
	elif lst[mid] < item:
		# We already know that item is not at mid, so we exclude mid
		return binSearchRecur(lst[mid + 1:], item)
	else:
		return binSearchRecur(lst[:mid], item)


l = [1, 4, 5, 6, 8, 9, 10]
print(binSearchIter(l, 4))
print(binSearchRecur(l, 4))
