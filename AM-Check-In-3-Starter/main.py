# BUBBLE SORT

# What is Bubble Sort?

# list1 = [4, 8, 2, 1, 10, 0]
# What does the list1 look like after 2 passes of Bubble Sort?
# Ans:

# Change the bubbleSort() function below to be more efficient.
def bubbleSort(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst) - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


# What is the time complexity of Bubble Sort?

# What is the best case for Bubble Sort? What is the worst case?


# MERGE SORT

# What is Merge Sort?

# What is the time complexity of Merge Sort?

# In Merge Sort, what must be true about the two lists that are being merged?

# The function merge() combines two sorted lists together. Finish the incomplete merge() function below
def merge(listA, listB):
    result = []
    while len(listA) > 0 and len(listB) > 0:
        # YOUR CODE HERE
        pass

    return


# Test your function here


# QUICKSORT

# What is Quicksort?

# What is the best case scenario for Quicksort? What is the worst case scenario?

# What is the time complexity of Quicksort in its best case? What's the time complexity of Quicksort in its worst case?

# The function partition() takes in a list and pivot is incomplete. Finish implementing the function below
def partition(lst, pivot):
    less = []
    eq = []
    great = []

    # YOUR CODE HERE

    return less, eq, great

# Test your function here


# FILE INPUT/OUTPUT

# Ask the user to input a word. Then, write the word letter by letter into an external file.

# Reading from the file that you just created, create a dictionary where the keys are the unique letters of your input and the values are how often those letters occur.

# What's the difference between read() and readlines()?
