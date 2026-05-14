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
