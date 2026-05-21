import random


def bubbleSort(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst) - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


def bubblesortImproved(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


l = [random.randint(1, 100) for i in range(8)]
print(l)
print(bubblesortImproved(l))
'''
If the student is interested, you could explain this alternative swapping method.

lst[j], lst[j+1] = lst[j+1], lst[j]

Because the assignments are made simultaneously, 
there is no need to store any value in a temporary variable.
'''
