###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

import random


# Space complexity of O(n), since we create a new list
def insertion_sort1(lst):
    result = []
    for i in range(len(lst)):
        item_to_insert = lst[i]
        result.append(item_to_insert)
        index_to_insert = i

        while index_to_insert != 0 and item_to_insert < result[index_to_insert - 1]:
            result[index_to_insert] = result[index_to_insert - 1]
            result[index_to_insert - 1] = item_to_insert
            index_to_insert -= 1

    return result


# Space complexity of O(1), since we modify the input list in-place
def insertion_sort2(lst):
    for i in range(len(lst)):
        j = i
        while j != 0 and lst[j] < lst[j - 1]:
            temp = lst[j - 1]
            lst[j - 1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst


l = [random.randint(10, 99) for i in range(8)]
print(l, end="\n\n")
print(insertion_sort1(l))
