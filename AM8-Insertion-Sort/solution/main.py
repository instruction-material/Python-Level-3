import random


def insertion_sort1(lst):
    """Return a stable sorted new list without changing the input."""
    result = []
    for i in range(len(lst)):
        item_to_insert = lst[i]
        result.append(item_to_insert)
        index_to_insert = i

        while (
            index_to_insert != 0
            and item_to_insert < result[index_to_insert - 1]
        ):
            result[index_to_insert] = result[index_to_insert - 1]
            result[index_to_insert - 1] = item_to_insert
            index_to_insert -= 1

    return result


def insertion_sort2(lst):
    """Sort stably in place and return the same list."""
    for i in range(len(lst)):
        j = i
        while j != 0 and lst[j] < lst[j - 1]:
            temp = lst[j - 1]
            lst[j - 1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst


if __name__ == "__main__":
    values = [random.randint(10, 99) for _ in range(8)]
    print("original:", values)
    print("sorted copy:", insertion_sort1(values))
    print("original after copy sort:", values)
