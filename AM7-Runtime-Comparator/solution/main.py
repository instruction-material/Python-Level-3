import random
import time


def linear_search(list1, item):
    for i in range(len(list1)):
        if item == list1[i]:
            return True
    return False


def bin_search_iter(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (high + low) // 2
        x = lst[mid]

        if x == item:
            return True
        elif x < item:
            low = mid + 1
        else:
            high = mid - 1

    return False


def bin_search_recur(lst, item):
    high = len(lst) - 1

    if high < 0:  # The list is empty
        return False

    mid = high // 2

    if lst[mid] == item:
        return True
    elif lst[mid] < item:
        # We already know that item is not at mid, so we exclude mid
        return bin_search_recur(lst[mid + 1 :], item)
    else:
        return bin_search_recur(lst[:mid], item)


nums = []
for i in range(1000000):
    nums.append(random.randint(0, 100000))

print("Starting linear search...")
start_lin = time.time()  # Returns number of seconds since Jan 1 1970
for i in range(1000):
    item = random.randint(0, 100000)
    linear_search(nums, item)
end_lin = time.time()  # Time will have advanced a few seconds compared to earlier
print("Linear search ended.")

nums.sort()
print("Starting binary search...")
start_bin = time.time()
for i in range(1000):
    item = random.randint(0, 100000)
    bin_search_iter(nums, item)
end_bin = time.time()
print("Binary search ended.")

print("Linear search took " + str(round(end_lin - start_lin, 5)) + " seconds.")
print("Binary search took " + str(round(end_bin - start_bin, 5)) + " seconds.")
