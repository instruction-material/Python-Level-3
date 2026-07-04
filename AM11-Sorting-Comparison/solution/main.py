import time
from random import randint


# O(1) space complexity, since we just modify the original list
def selection_sort(lst):
    for i in range(len(lst)):
        min_item = lst[0]
        min_item_i = 0
        for j in range(i, len(lst)):
            if lst[j] < min_item:
                min_item = lst[j]
                min_item_i = j

        temp = lst[i]
        lst[i] = min_item
        lst[min_item_i] = temp
    return lst


# Space complexity of O(1), since we modify the input list in-place
def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while j != 0 and lst[j] < lst[j - 1]:
            temp = lst[j - 1]
            lst[j - 1] = lst[j]
            lst[j] = temp
            j -= 1

    return lst


def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


# This is the integrated version that does not require a helper "merge" function
def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst

    first_half = merge_sort(lst[:n // 2])
    second_half = merge_sort(lst[n // 2:])

    result = []
    while len(first_half) > 0 and len(second_half) > 0:
        if first_half[0] < second_half[0]:
            result.append(first_half.pop(0))
        else:
            result.append(second_half.pop(0))

    return result + first_half + second_half


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

    pivot_ind = randint(0, n - 1)
    # pivotInd = 0 is the initial "naive" choice
    pivot = lst[pivot_ind]

    less, eq, great = partition(lst, pivot)

    sorted_less = quicksort(less)
    sorted_great = quicksort(great)

    return sorted_less + eq + sorted_great


""" This is a timing test on completely random lists """
print("SORTING TIMING TESTS (RANDOM)")
for n in [100, 1000, 10000]:
    print("With", n, "items")

    if n < 10000:
        lst = [randint(-10000, 10000) for _ in range(n)]
        start = time.time()
        selection_sort(lst)
        end = time.time()
        print("Selection Sort:\t", round(end - start, 6), "seconds")

        lst = [randint(-10000, 10000) for _ in range(n)]
        start = time.time()
        insertion_sort(lst)
        end = time.time()
        print("Insertion Sort:\t", round(end - start, 6), "seconds")

        lst = [randint(-10000, 10000) for _ in range(n)]
        start = time.time()
        bubble_sort(lst)
        end = time.time()
        print("Bubble Sort:\t", round(end - start, 6), "seconds")
    else:
        print("Selection Sort:\t about 16 seconds")
        print("Insertion Sort:\t about 44 seconds")
        print("Bubble Sort:\t about 45 seconds")

    lst = [randint(-10000, 10000) for _ in range(n)]
    start = time.time()
    merge_sort(lst)
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
        selection_sort(lst)
        end = time.time()
        print("Selection Sort:\t", round(end - start, 6), "seconds")
    else:
        print("Selection Sort:\t about 16 seconds")

    lst = [randint(-10000, 10000) for _ in range(n)]
    lst.sort()
    start = time.time()
    insertion_sort(lst)
    end = time.time()
    print("Insertion Sort:\t", round(end - start, 6), "seconds")

    if n < 10000:
        lst = [randint(-10000, 10000) for _ in range(n)]
        lst.sort()
        start = time.time()
        bubble_sort(lst)
        end = time.time()
        print("Bubble Sort:\t", round(end - start, 6), "seconds")
    else:
        print("Bubble Sort:\t about 37 seconds")

    lst = [randint(-10000, 10000) for _ in range(n)]
    lst.sort()
    start = time.time()
    merge_sort(lst)
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
        selection_sort(lst)
        end = time.time()
        print("Selection Sort:\t", round(end - start, 6), "seconds")

        lst = [randint(-10000, 10000) for _ in range(n)]
        lst.sort()
        lst.reverse()
        start = time.time()
        insertion_sort(lst)
        end = time.time()
        print("Insertion Sort:\t", round(end - start, 6), "seconds")

        lst = [randint(-10000, 10000) for _ in range(n)]
        lst.sort()
        lst.reverse()
        start = time.time()
        bubble_sort(lst)
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
    merge_sort(lst)
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
