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
    """Stably merge sorted inputs into a fresh list without consuming either."""
    raise NotImplementedError("Implement merge before calling it.")

# Test your function here


# QUICKSORT

# What is Quicksort?

# What is the best case scenario for Quicksort? What is the worst case scenario?

# What is the time complexity of Quicksort in its best case? What's the time complexity of Quicksort in its worst case?


# The function partition() takes in a list and pivot is incomplete. Finish implementing the function below
def partition(lst, pivot):
    """Return ordered less/equal/greater groups; pivot is a value, not an index."""
    raise NotImplementedError("Implement partition before calling it.")

# Test your function here


# FILE INPUT/OUTPUT

# Ask the user to input a word. Then, write the word letter by letter into an external file.

# Reading from the file that you just created, create a dictionary where the keys are the unique letters of your input and the values are how often those letters occur.

# What's the difference between read() and readlines()?


# Keep bubbleSort above as supplied optimization/trace input, not the final answer.

def bubble_sort(lst):
    """Implement shrinking-range and no-swap early exit; sort in place."""
    raise NotImplementedError("Implement bubble_sort before calling it.")


def write_letters(word, path="file.txt"):
    """Write one Unicode character per line; reject CR/LF before overwriting."""
    raise NotImplementedError("Implement write_letters before calling it.")


def read_letter_counts(path="file.txt"):
    """Count exact one-character records; malformed lines raise ValueError."""
    raise NotImplementedError("Implement read_letter_counts before calling it.")


def main():
    """Collect a word, write letters and print the reloaded frequency dictionary."""
    raise NotImplementedError("Implement main before calling it.")


if __name__ == "__main__":
    print("Implement the TODOs; trace bubbleSort first and keep reference answers separate.")
