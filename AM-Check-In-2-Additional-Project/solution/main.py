import copy
import random
import time


# Algorithm Comparison

# Copy in the code for each of the sorting functions that you have previously written, and write some tests to determine how fast each algorithm runs in a given scenario. Some possible scenarios to consider testing would be when the list to be sorted is already completely random, when it is already sorted, when it is sorted and reversed, and how many elements are in each of these lists (eg. n = 100, n = 1000, n = 2000, etc.). Can you think of any other scenarios? 


# You can copy a list with this line of code: list2 = copy.deepcopy(list1)
# You can sort a list in reverse if you write list2.sort(reverse=True)

# Copy over your functions for insertion sort and selection sort here. 

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


def insertionSort2(lst):
    for i in range(len(lst)):
        j = i
        while j != 0 and lst[j] < lst[j - 1]:
            temp = lst[j - 1]
            lst[j - 1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst


# create a variable for n
n = 2000

# generate a list with n random numbers in it
nums = []
for i in range(n):
    nums.append(random.randint(1, n * 10))
# make 3 copies of the list with copy.deepcopy(list1)
nums2 = copy.deepcopy(nums)
nums3 = copy.deepcopy(nums)
nums4 = copy.deepcopy(nums)

# sort and reverse two copies of the list with list3.sort(reverse=True)
nums3.sort(reverse=True)
nums4.sort(reverse=True)

# Find the times for all 4 tests

# selection sort random order
startSelect = time.time()
selectionSort2(nums)
stopSelect = time.time()

# selection sort on reversed list
startSelectReverse = time.time()
selectionSort2(nums3)
stopSelectReverse = time.time()

# insertion sort random order
startInsert = time.time()
insertionSort2(nums2)
stopInsert = time.time()

# insertion sort on reversed list
startInsertReverse = time.time()
insertionSort2(nums4)
stopInsertReverse = time.time()

# print results
print("Selection sort time for n=" + str(n) + ": " + str(round(stopSelect - startSelect, 5)))
print("Selection sort reversed time for n=" + str(n) + ": " + str(round(stopSelectReverse - startSelectReverse, 5)))

print("Insertion sort time for n=" + str(n) + ": " + str(round(stopInsert - startInsert, 5)))
print("Insertion sort reversed time for n=" + str(n) + ": " + str(round(stopInsertReverse - startInsertReverse, 5)))
