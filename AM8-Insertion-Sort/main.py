import random


# Space complexity of O(n), since we create a new list
def insertionSort1(lst):
    result = []
    for i in range(len(lst)):
        itemToInsert = lst[i]
        result.append(itemToInsert)
        indexToInsert = i

        while indexToInsert != 0 and itemToInsert < result[indexToInsert - 1]:
            result[indexToInsert] = result[indexToInsert - 1]
            result[indexToInsert - 1] = itemToInsert
            indexToInsert -= 1

    return result


# Space complexity of O(1), since we modify the input list in-place
def insertionSort2(lst):
    for i in range(len(lst)):
        j = i
        while j != 0 and lst[j] < lst[j - 1]:
            temp = lst[j - 1]
            lst[j - 1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst


l = [random.randint(10, 99) for i in range(8)]
print(l, end='\n\n')
print(insertionSort1(l))
