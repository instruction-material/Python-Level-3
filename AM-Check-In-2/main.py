#########################
# TIME COMPLEXITY
#########################

# Time-2: Find the big-O of each of these functions:
# 1. f(n) = n^2 + 1000n
# 2. f(n) = log(n) + sqrt(n)
# 3. f(n) = 1*2*3*4*...*n

# 1. O(n^2)
# 2. O(sqrt(n)) 
# 3. O(n!)

# Time-3: Look at the definition of weirdFunction. What is the best case scenario? What is the worst case scenario? What is the big-O of weirdFunction? 
def weirdFunction(nums):
    if len(nums) % 2 == 1:
        print("There are an odd amount of numbers")
    else:
        for i in range(len(nums)):
            print(i, nums[i])


# ANSWER: O(n)
# weirdFunction([4,5,6]) (odd length)
# weirdFunction([1,2,3,4,5,6]) (even length)
# print()

# Time-4: What is the time complexity of function1? Let n be the length of nums. 
def function1(nums):
    for num in nums:
        for i in range(3):
            print(i, num)


# ANSWER: O(n)
# function1([12,45,23,67])


# Time-5: What is the time complexity of function2?
def function2(n):
    print(n)
    if n > 2:
        function2(n // 2)


# ANSWER: O(log(n))
# function2(50)


#########################
# Linear Search
#########################

# Linear-2: The linearSearch() function takes in a list and a value, and returns true if the value is in the list and false otherwise, but it's incomplete. Fill in the missing code to create a working Linear Search function. Be sure to test the function after adding your code!


def linearSearch(l, v):
    for item in l:
        if item == v:
            return True
    return False


# Linear-3: What is the time complexity of Linear Search? Can you describe the best and worst case scenarios?
# Ans: O(n)


#########################
# Binary Search
#########################

# Binary-2: The binarySearch() function takes in a sorted list and a value, and returns true if the value is in the list and false otherwise, but it's incomplete. Fill in the missing code to create a working Binary Search function. Be sure to test the function after adding your code!


def binSearchIter(lst, item):
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


def binSearchRecur(lst, item):
    high = len(lst) - 1

    if high < 0:
        return False

    mid = high // 2

    if lst[mid] == item:
        return True
    elif lst[mid] < item:
        return binSearchRecur(lst[mid + 1:], item)
    else:
        return binSearchRecur(lst[:mid], item)


# Binary-3: What is the time complexity of Binary Search? Can you describe the best and worst case scenarios?
# Ans: O(log(n))


#########################
# SELECTION SORT
#########################

# What is Selection Sort? Can you describe how it works?

# list1 = [2, 5, 10, 3, 6, 1]
# What will list1 look after 2 passes of Selection Sort?
# Ans: list1 = [1, 2, 10, 3, 6, 5]

# The selectionSort() function below takes in a list and sorts the numbers from largest to smallest, but it's incomplete. Finish what's missing.
def selectionSort(lst):
    for i in range(len(lst)):
        maxItem = lst[i]
        maxItemI = i
        for j in range(i, len(lst)):
            # YOUR CODE HERE
            if lst[j] > maxItem:
                maxItem = lst[j]
                maxItemI = j

        temp = lst[i]
        lst[i] = maxItem
        lst[maxItemI] = temp
    return lst


# What is the time complexity of Selection Sort? Can you describe the best and worst case scenarios?
# Ans: O(n^2)


#########################
# INSERTION SORT
#########################

# What is Insertion Sort? Can you describe how it works?

# list2 = [3, 7, 2, 5, 10, 1]
# What will list2 look after 3 passes of Insertion Sort?
# Ans: list2 = [2, 3, 5, 7, 10, 1]

# Finish the incomplete insertionSort() function below
def insertionSort(lst):
    for i in range(len(lst)):
        j = i
        while j != 0 and lst[j] < lst[j - 1]:
            temp = lst[j - 1]
            lst[j - 1] = lst[j]
            lst[j] = temp
            j -= 1
    return lst

# What is the time complexity of Insertion Sort? Can you describe the best and worst case scenarios? 
# Ans: O(n^2)
# Best case - Array is already sorted
# Worst case - Array is backwards
