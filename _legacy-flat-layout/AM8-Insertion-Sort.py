"""
Write a function that takes in a list of numbers and returns a list that has been sorted using the Insertion Sort algorithm. The steps of Insertion Sort are:
Place the next number from the input list at the end of the output list
Swap that number with the previous one until the previous number is less than or equal to the one we inserted
Repeat until we have placed every number from the input list into the output list
"""

import random


# Space complexity of O(n), since we create a new list
def insertionSort1(lst):
	result = []
	for i in range(len(lst)):
		itemToInsert = lst[i]
		result.append(itemToInsert)
		indexToInsert = i
		
		while indexToInsert and itemToInsert < result[indexToInsert - 1]:
			result[indexToInsert] = result[indexToInsert - 1]
			result[indexToInsert - 1] = itemToInsert
			indexToInsert -= 1
	
	return result


# Space complexity of O(1), since we modify the input list in-place
def insertionSort2(lst):
	for i in range(len(lst)):
		j = i
		while j and lst[j] < lst[j - 1]:
			temp = lst[j - 1]
			lst[j - 1] = lst[j]
			lst[j] = temp
			j -= 1
	return lst


l = [random.randint(10, 99) for i in range(8)]
print(l, end='\n\n')
print(insertionSort1(l))
