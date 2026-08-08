#########################
# TIME COMPLEXITY
#########################

# What is Big-O analysis?

# Find the Big-O of each of these functions:
# 1. f(n) = n^2 + 1000n
# 2. f(n) = log(n) + sqrt(n)
# 3. f(n) = 1*2*3*4*...*n


# Look at the definition of weirdFunction. What is the best case scenario? What is the worst case scenario? What is the Big-O of weirdFunction?
def weirdFunction(nums):
    if len(nums) % 2 == 1:
        print("There are an odd amount of numbers")
    else:
        for i in range(len(nums)):
            print(i, nums[i])


# What is the time complexity of function1? Let n be the length of nums.
def function1(nums):
    for num in nums:
        for i in range(3):
            print(i, num)


# function1([12,45,23,67])


# What is the time complexity of function2?
def function2(n):
    print(n)
    if n > 2:
        function2(n // 2)


# function2(50)


#########################
# SEARCHING
#########################

# What do search algorithms do? What two search algorithms have we learned? When can we use each one?

# Write a function that takes in a sorted list of 0’s and 1’s and returns the index of the first 1. The function should be in O(logn) time.


#########################
# SELECTION SORT
#########################

# Selection-1: What is Selection Sort?

# list1 = [2, 5, 10, 3, 6, 1]
# What will list1 look after 2 passes of Selection Sort?
# Ans:


# The selectionSort() function below takes in a list and sorts the numbers from largest to smallest, but it's incomplete. Finish what's missing.
def selectionSort(lst):
    for i in range(len(lst)):
        maxItem = lst[i]
        maxItemI = i
        for j in range(i, len(lst)):
            # YOUR CODE HERE
            pass

    return lst


# What is the time complexity of Selection Sort?


#########################
# INSERTION SORT
#########################

# list2 = [3, 7, 2, 5, 10, 1]
# What will list2 look like after 3 passes of Insertion Sort?
# Ans:


# Finish the incomplete insertionSort() function below
def insertionSort(lst):
    for i in range(len(lst)):
        j = i
        # YOUR CODE HERE

    return lst


# What is the time complexity of Insertion Sort?

# What is the worst case scenario for Insertion Sort? What is the best case?
