import random


# The pivot argument is a value, not an index.
def partition(lst, pivot):
    """Return less/equal/greater lists, preserving order within each group."""
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


def quicksort(lst, rng=None):
    """Return a sorted new list; optional rng makes pivot choices repeatable."""
    n = len(lst)

    if n <= 1:
        return lst.copy()

    generator = random if rng is None else rng
    pivot_ind = generator.randint(0, n - 1)
    # pivotInd = 0 is the initial "naive" choice
    pivot = lst[pivot_ind]

    less, eq, great = partition(lst, pivot)
    sorted_less = quicksort(less, generator)
    sorted_great = quicksort(great, generator)

    return sorted_less + eq + sorted_great


# One possible way to shuffle the items in a list prior to sorting it
def shuffle(lst, num_swaps):
    """Mutate by random swaps; return None. This is not a uniform shuffle."""
    if type(num_swaps) is not int or num_swaps < 0:
        raise ValueError("num_swaps must be a nonnegative integer")
    if len(lst) < 2:
        return
    for i in range(num_swaps):
        a = random.randint(0, len(lst) - 1)
        b = random.randint(0, len(lst) - 1)
        temp = lst[a]
        lst[a] = lst[b]
        lst[b] = temp


# Another possible way to shuffle a list
def shuffle2(lst):
    """Return a random permutation in a new list, consuming the input."""
    result = []
    while len(lst) > 0:
        result.append(lst.pop(random.randint(0, len(lst) - 1)))
    return result


if __name__ == "__main__":
    values = [random.randint(1, 100) for _ in range(8)]
    print("original:", values)
    print("sorted copy:", quicksort(values))
    print("original after sort:", values)
