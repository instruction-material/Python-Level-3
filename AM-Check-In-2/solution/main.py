"""Reference algorithms; mathematical classifications and traces are in README.md."""


def weird_function(nums):
    if len(nums) % 2 == 1:
        print("There are an odd amount of numbers")
    else:
        for i in range(len(nums)):
            print(i, nums[i])


def function1(nums):
    for num in nums:
        for i in range(3):
            print(i, num)


def function2(n):
    print(n)
    if n > 2:
        function2(n // 2)


def linear_search(l, v):
    for item in l:
        if item == v:
            return True
    return False


def bin_search_iter(lst, item):
    """Already ascending input; no input scan or mutation."""
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == item:
            return True
        if lst[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return False


def bin_search_recur(lst, item):
    """Bounds-only recursion avoids the old recursive slice copying."""
    def search(low, high):
        if low > high:
            return False
        mid = (low + high) // 2
        if lst[mid] == item:
            return True
        if lst[mid] < item:
            return search(mid + 1, high)
        return search(low, mid - 1)
    return search(0, len(lst) - 1)


def first_one_index(numbers):
    """Sorted binary input is a precondition, not an O(n) validation scan."""
    low, high = 0, len(numbers)
    while low < high:
        mid = (low + high) // 2
        if numbers[mid] == 0:
            low = mid + 1
        else:
            high = mid
    if low < len(numbers) and numbers[low] == 1:
        return low
    return -1


def selection_sort(lst):
    """Descending, in-place selection; no stability promise."""
    for i in range(len(lst)):
        max_item = lst[i]
        max_item_i = i
        for j in range(i, len(lst)):
            if lst[j] > max_item:
                max_item = lst[j]
                max_item_i = j
        lst[i], lst[max_item_i] = lst[max_item_i], lst[i]
    return lst


def insertion_sort(lst):
    """Ascending, stable in-place insertion; passes begin at index one."""
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
    return lst


selectionSort = selection_sort
insertionSort = insertion_sort
weirdFunction = weird_function


if __name__ == "__main__":
    print("First one:", first_one_index([0, 0, 0, 1, 1]))
    print("Descending selection:", selection_sort([2, 5, 10, 3, 6, 1]))
    print("Ascending insertion:", insertion_sort([3, 7, 2, 5, 10, 1]))
