"""
AM10 Project 1: Merge
Write a function that takes in two sorted lists and returns a single sorted list made up of the elements of each of the two input lists.

AM10 Project 2: Split
Write a function that prints the input list if it has 1 or fewer things in it; otherwise, split the list in half and recursively call the function with each half.

AM10 Project 3: Merge Sort
Referencing the two previous functions that you have written, write a function that takes in an unsorted list and performs Merge Sort by recursively splitting the input list, and then merging both of the sorted halves of that input list.
"""


# This is a helper function to handle the merging part of Merge Sort
def merge(listA, listB):
	result = []
	aIndex = 0
	bIndex = 0
	
	# Compare and add each element
	while aIndex < len(listA) and bIndex < len(listB):
		if listA[aIndex] < listB[bIndex]:
			result.append(listA[aIndex])
			aIndex += 1
		else:
			result.append(listB[bIndex])
			bIndex += 1
	
	# Add the remaining elements left in the list after the comparisons
	while aIndex < len(listA):
		result.append(listA[aIndex])
		aIndex += 1
	
	while bIndex < len(listB):
		result.append(listB[bIndex])
		bIndex += 1
	
	return result


# This function is to help build intuition for the splitting part of Merge Sort
def split(lst):
	n = len(lst)
	if n <= 1:
		print(lst)
	else:
		split(lst[:n // 2])
		split(lst[n // 2:])


# Merge Sort that uses the helper function merge
def mergeSort(lst):
	n = len(lst)
	if n <= 1:  # An empty list (or a list containing one element) is a sorted list
		return lst
	
	firstHalf = mergeSort(lst[:n // 2])
	secondHalf = mergeSort(lst[n // 2:])
	return merge(firstHalf, secondHalf)


# This is the integrated version that does not require a helper "merge" function
def mergeSort2(lst):
	n = len(lst)
	if n <= 1:
		return lst
	
	firstHalf = mergeSort2(lst[:n // 2])
	secondHalf = mergeSort2(lst[n // 2:])
	
	result = []
	aIndex = 0
	bIndex = 0
	while aIndex < len(firstHalf) and bIndex < len(secondHalf):
		if firstHalf[aIndex] < secondHalf[bIndex]:
			result.append(firstHalf[aIndex])
			aIndex += 1
		else:
			result.append(secondHalf[bIndex])
			bIndex += 1
	
	while aIndex < len(firstHalf):
		result.append(firstHalf[aIndex])
		aIndex += 1
	
	while bIndex < len(secondHalf):
		result.append(secondHalf[bIndex])
		bIndex += 1
	
	return result
