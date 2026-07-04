###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

# This is a helper function to handle the merging part of Merge Sort
def merge(list_a, list_b):
    result = []
    a_index = 0
    b_index = 0
    while a_index < len(list_a) and b_index < len(list_b):
        if list_a[a_index] < list_b[b_index]:
            result.append(list_a[a_index])
            a_index += 1
        else:
            result.append(list_b[b_index])
            b_index += 1

    while a_index < len(list_a):
        result.append(list_a[a_index])
        a_index += 1

    while b_index < len(list_b):
        result.append(list_b[b_index])
        b_index += 1

    return result


# This function is to help build intuition for the splitting part of Merge Sort
def split(lst):
    n = len(lst)
    if n <= 1:
        print(lst)
    else:
        split(lst[: n // 2])
        split(lst[n // 2 :])


# Merge Sort that uses the helper function merge
def merge_sort(lst):
    n = len(lst)
    if n <= 1:  # An empty list (or a list containing one element) is a sorted list
        return lst

    first_half = merge_sort(lst[: n // 2])
    second_half = merge_sort(lst[n // 2 :])
    return merge(first_half, second_half)


# This is the integrated version that does not require a helper "merge" function
def merge_sort2(lst):
    n = len(lst)
    if n <= 1:
        return lst

    first_half = merge_sort2(lst[: n // 2])
    second_half = merge_sort2(lst[n // 2 :])

    result = []
    a_index = 0
    b_index = 0
    while a_index < len(first_half) and b_index < len(second_half):
        if first_half[a_index] < second_half[b_index]:
            result.append(first_half[a_index])
            a_index += 1
        else:
            result.append(second_half[b_index])
            b_index += 1

    while a_index < len(first_half):
        result.append(first_half[a_index])
        a_index += 1

    while b_index < len(second_half):
        result.append(second_half[b_index])
        b_index += 1

    return result
