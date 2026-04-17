"""
Write a function that takes in a list of numbers and sorts that list using the Bubble Sort algorithm. The steps for Bubble Sort are:
Compare the element that you are at with the next element
If the current element is larger than the next one, swap them
Continue these comparisons until you have run through the list completely
Repeat this process for each element of the list
"""

import random


def bubbleSort(lst):
	for i in range(len(lst)):
		for j in range(len(lst) - 1):
			if lst[j] > lst[j + 1]:
				temp = lst[j]
				lst[j] = lst[j + 1]
				lst[j + 1] = temp
	return lst


def bubbleSortImproved(lst):
	for i in range(len(lst) - 1, 0, -1):
		for j in range(i):
			if lst[j] > lst[j + 1]:
				temp = lst[j]
				lst[j] = lst[j + 1]
				lst[j + 1] = temp
	return lst


l = [random.randint(1, 100) for i in range(8)]
print(l)
print(bubbleSort(l))
'''
If the student is interested, you could explain this alternative swapping method.

lst[j], lst[j+1] = lst[j+1], lst[j]

Because the assignments are made simultaneously, 
there is no need to store any value in a temporary variable.
'''

i = j = 0
newList = []
while i != len(listA) and j != len(listB):
	if listA[i] < listB[j]:
		newList.append(listA[i])
		i += 1
	else:
		newList.append(listB[j])
		j += 1

newList = []
while listA or listB:
	if listA[0] < listB[0]:
		newList.append(listA.pop(0))
	else:
		newList.append(listB.pop(0))
