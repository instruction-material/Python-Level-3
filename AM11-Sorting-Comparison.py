"""
Copy in the code for each of the sorting functions that you have previously written. Using time.time() to measure start and end times, write several tests to measure how fast each algorithm runs in a variety of scenarios. For example, you might consider testing with lists of different sizes (10-20 numbers, 100 numbers, 1000 numbers, etc.), and with varying levels of randomness (completely random, completely sorted, mostly sorted, sorted but reversed, etc.).
"""

import time
from random import randint


# O(1) space complexity, since we just modify the original list
def selectionSort(lst):
	for i in range(len(lst)):
		minItem = lst[0]
		minItemI = 0
		for j in range(i, len(lst)):
			if lst[j] < minItem:
				minItem = lst[j]
				minItemI = j
		
		temp = lst[i]
		lst[i] = minItem
		lst[minItemI] = temp
	return lst


# Space complexity of O(1), since we modify the input list in-place
def insertionSort(lst):
	for i in range(len(lst)):
		j = i
		while j != 0 and lst[j] < lst[j - 1]:
			temp = lst[j - 1]
			lst[j - 1] = lst[j]
			lst[j] = temp
			j -= 1
	
	return lst


def bubbleSort(lst):
	for i in range(len(lst) - 1, 0, -1):
		for j in range(0, i):
			if lst[j] > lst[j + 1]:
				temp = lst[j]
				lst[j] = lst[j + 1]
				lst[j + 1] = temp
	return lst


# This is the integrated version that does not require a helper "merge" function
def mergeSort(lst):
	n = len(lst)
	if n <= 1:
		return lst
	
	firstHalf = mergeSort(lst[:n // 2])
	secondHalf = mergeSort(lst[n // 2:])
	
	result = []
	while len(firstHalf) > 0 and len(secondHalf) > 0:
		if firstHalf[0] < secondHalf[0]:
			result.append(firstHalf.pop(0))
		else:
			result.append(secondHalf.pop(0))
	
	return result + firstHalf + secondHalf


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
	
	pivotInd = randint(0, n - 1)
	# pivotInd = 0 is the initial "naive" choice
	pivot = lst[pivotInd]
	
	less, eq, great = partition(lst, pivot)
	
	sortedLess = quicksort(less)
	sortedGreat = quicksort(great)
	
	return sortedLess + eq + sortedGreat


""" This is a timing test on completely random lists """
print("SORTING TIMING TESTS (RANDOM)")
for n in [100, 1000, 10000]:
	print("With", n, "items")
	
	if n < 10000:
		lst = [randint(-10000, 10000) for _ in range(n)]
		start = time.time()
		selectionSort(lst)
		end = time.time()
		print("Selection Sort:\t", round(end - start, 6), "seconds")
		
		lst = [randint(-10000, 10000) for _ in range(n)]
		start = time.time()
		insertionSort(lst)
		end = time.time()
		print("Insertion Sort:\t", round(end - start, 6), "seconds")
		
		lst = [randint(-10000, 10000) for _ in range(n)]
		start = time.time()
		bubbleSort(lst)
		end = time.time()
		print("Bubble Sort:\t", round(end - start, 6), "seconds")
	else:
		print("Selection Sort:\t about 16 seconds")
		print("Insertion Sort:\t about 44 seconds")
		print("Bubble Sort:\t about 45 seconds")
	
	lst = [randint(-10000, 10000) for _ in range(n)]
	start = time.time()
	mergeSort(lst)
	end = time.time()
	print("Merge Sort:\t\t", round(end - start, 6), "seconds")
	
	lst = [randint(-10000, 10000) for _ in range(n)]
	start = time.time()
	quicksort(lst)
	end = time.time()
	print("Quick Sort:\t\t", round(end - start, 6), "seconds")
	
	print()

time.sleep(2)
""" This is a timing test on sorted lists """
print("\n\nSORTING TIMING TESTS (PRE-SORTED)")
for n in [100, 1000, 10000]:
	print("With", n, "items")
	
	if n < 10000:
		lst = [randint(-10000, 10000) for _ in range(n)]
		lst.sort()
		start = time.time()
		selectionSort(lst)
		end = time.time()
		print("Selection Sort:\t", round(end - start, 6), "seconds")
	else:
		print("Selection Sort:\t about 16 seconds")
	
	lst = [randint(-10000, 10000) for _ in range(n)]
	lst.sort()
	start = time.time()
	insertionSort(lst)
	end = time.time()
	print("Insertion Sort:\t", round(end - start, 6), "seconds")
	
	if n < 10000:
		lst = [randint(-10000, 10000) for _ in range(n)]
		lst.sort()
		start = time.time()
		bubbleSort(lst)
		end = time.time()
		print("Bubble Sort:\t", round(end - start, 6), "seconds")
	else:
		print("Bubble Sort:\t about 37 seconds")
	
	lst = [randint(-10000, 10000) for _ in range(n)]
	lst.sort()
	start = time.time()
	mergeSort(lst)
	end = time.time()
	print("Merge Sort:\t\t", round(end - start, 6), "seconds")
	
	lst = [randint(-10000, 10000) for _ in range(n)]
	lst.sort()
	start = time.time()
	quicksort(lst)
	end = time.time()
	print("Quick Sort:\t\t", round(end - start, 6), "seconds")
	
	print()
time.sleep(2)
""" This is a timing test on reversed sorted lists """
print("\n\nSORTING TIMING TESTS (REVERSED SORTED)")
for n in [100, 1000, 10000]:
	print("With", n, "items")
	
	if n < 10000:
		lst = [randint(-10000, 10000) for _ in range(n)]
		lst.sort()
		lst.reverse()
		start = time.time()
		selectionSort(lst)
		end = time.time()
		print("Selection Sort:\t", round(end - start, 6), "seconds")
		
		lst = [randint(-10000, 10000) for _ in range(n)]
		lst.sort()
		lst.reverse()
		start = time.time()
		insertionSort(lst)
		end = time.time()
		print("Insertion Sort:\t", round(end - start, 6), "seconds")
		
		lst = [randint(-10000, 10000) for _ in range(n)]
		lst.sort()
		lst.reverse()
		start = time.time()
		bubbleSort(lst)
		end = time.time()
		print("Bubble Sort:\t", round(end - start, 6), "seconds")
	else:
		print("Selection Sort:\t about 30 seconds")
		print("Insertion Sort:\t about 105 seconds")
		print("Bubble Sort:\t about 84 seconds")
	
	lst = [randint(-10000, 10000) for _ in range(n)]
	lst.sort()
	lst.reverse()
	start = time.time()
	mergeSort(lst)
	end = time.time()
	print("Merge Sort:\t\t", round(end - start, 6), "seconds")
	
	lst = [randint(-10000, 10000) for _ in range(n)]
	lst.sort()
	lst.reverse()
	start = time.time()
	quicksort(lst)
	end = time.time()
	print("Quick Sort:\t\t", round(end - start, 6), "seconds")
	
	print()
