# This is a helper function to handle the merging part of Merge Sort
def merge(listA, listB):
    result = []
    aIndex = 0
    bIndex = 0
    while aIndex < len(listA) and bIndex < len(listB):
        if listA[aIndex] < listB[bIndex]:
            result.append(listA[aIndex])
            aIndex += 1
        else:
            result.append(listB[bIndex])
            bIndex += 1

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
