"""
AM11 Project 1: Partition
Write a function that takes in a list and a pivot, and returns three lists: a list that contains everything less than the pivot, a list that contains everything equal to the pivot, and a list that contains everything greater than the pivot. A function can return multiple things! You can do this by separating each of the things that you would like to return with a comma, like so: return thing1, thing2, thing3. Alternatively, you could return a list that contains each of those three separate lists.

AM11 Project 2: Quicksort
Write a function that takes in a list and sorts it using the Quicksort algorithm.
"""

import random


# Helper function to partition the input list using the given index
def partition(lst, pivot):
	less = []  # Alternatively explain how to do multiple assignments, like so:
	eq = []  # less, eq, great = [[] for i in range(3)]
	great = []
	
	for num in lst:
		if num < pivot:
			less.append(num)
		elif num == pivot:
			eq.append(num)
		else:
			great.append(num)
	
	return less, eq, great


def quicksort(lst):
	n = len(lst)
	
	if n <= 1:
		return lst
	
	pivotInd = random.randint(0, n - 1)
	# pivotInd = 0 is the initial "naive" choice
	pivot = lst[pivotInd]
	
	less, eq, great = partition(lst, pivot)
	sortedLess = quicksort(less)
	sortedGreat = quicksort(great)
	
	return sortedLess + eq + sortedGreat


# One possible way to shuffle the items in a list prior to sorting it
def shuffle(lst, numSwaps):
	for i in range(numSwaps):
		a = random.randint(0, len(lst) - 1)
		b = random.randint(0, len(lst) - 1)
		temp = lst[a]
		lst[a] = lst[b]
		lst[b] = temp


# Another possible way to shuffle a list
def shuffle2(lst):
	result = []
	while len(lst) > 0:
		result.append(lst.pop(random.randint(0, len(lst) - 1)))
	return result


l = [random.randint(1, 100) for i in range(8)]
print(l)
print(quicksort(l))
