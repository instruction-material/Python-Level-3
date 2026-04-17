"""
Write a function that takes in a list of numbers and returns a list that has been sorted using the Selection Sort algorithm. The steps of Selection Sort are:
Loop through the input list
Remove the minimum element
Place the minimum element at the end of the output list
Continue until the input list is empty
"""

import random


# O(n) space complexity, since we create and return a new list
def selectionSort1(lst):
	result = []
	for i in range(len(lst)):
		minItem = lst[0]
		for item in lst:
			minItem = min(item, minItem)
		result.append(minItem)
		lst.remove(minItem)
	return result


# O(1) space complexity, since we just modify the original list
def selectionSort2(lst):
	for i in range(len(lst)):
		minItem = lst[i]
		minItemI = i
		for j in range(i, len(lst)):
			if lst[j] < minItem:
				minItem = lst[j]
				minItemI = j
		
		temp = lst[i]
		lst[i] = minItem
		lst[minItemI] = temp
	return lst


l = [random.randint(1, 100) for i in range(10)]
print(l)
print(selectionSort1(l))
