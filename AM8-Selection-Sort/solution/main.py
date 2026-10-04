import random


def selection_sort1(lst):
    """Return a sorted new list, consuming (emptying) the input list."""
    result = []
    for i in range(len(lst)):
        min_item = lst[0]
        for item in lst:
            if item < min_item:
                min_item = item
        result.append(min_item)
        lst.remove(min_item)
    return result


def selection_sort2(lst):
    """Sort in place and return the same list; swaps need not be stable."""
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


if __name__ == "__main__":
    values = [random.randint(1, 100) for _ in range(10)]
    print("original:", values)
    print("consuming sort:", selection_sort1(values))
    print("input after consuming sort:", values)
