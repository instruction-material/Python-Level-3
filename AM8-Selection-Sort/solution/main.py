###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import random


# O(n) space complexity, since we create and return a new list
def selection_sort1(lst):
    result = []
    for i in range(len(lst)):
        min_item = lst[0]
        for item in lst:
            min_item = min(item, min_item)
        result.append(min_item)
        lst.remove(min_item)
    return result


# O(1) space complexity, since we just modify the original list
def selection_sort2(lst):
    for i in range(len(lst)):
        min_item = lst[i]
        min_item_i = i
        for j in range(i, len(lst)):
            if lst[j] < min_item:
                min_item = lst[j]
                min_item_i = j

        temp = lst[i]
        lst[i] = min_item
        lst[min_item_i] = temp
    return lst


l = [random.randint(1, 100) for i in range(10)]
print(l)
print(selection_sort1(l))
