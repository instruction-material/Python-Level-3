###########################

# BUBBLE SORT

###########################

# What is Bubble Sort? Can you describe how it works?

# list1 = [4, 8, 2, 1, 10, 0]
# What does the list1 look like after 2 passes of Bubble Sort?
# list1 = [2, 1, 4, 0, 8, 10]

# Change the bubbleSort() function below to be more efficient (so that there's an early cutoff).
def bubbleSort(lst):
	for i in range(len(lst) - 1):
		for j in range(len(lst) - i - 1):
			if lst[j] > lst[j + 1]:
				temp = lst[j]
				lst[j] = lst[j + 1]
				lst[j + 1] = temp
	return lst


# What is the time complexity of Bubble Sort? Can you describe the best and worst case scenarios
# Ans: O(n^2)
# Ans: Best case - already in order
# Worst case - reverse order


###########################

# MERGE SORT

###########################

# What is Merge Sort? Can you describe how it works?

# The function merge() combines two sorted lists together. Finish the incomplete merge() function below
def merge(listA, listB):
	result = []
	while len(listA) > 0 and len(listB) > 0:
		# YOUR CODE HERE
		if listA[0] < listB[0]:
			result.append(listA.pop(0))
		else:
			result.append(listB.pop(0))
	
	return result + listA + listB


# What is the time complexity of Merge Sort? Can you describe the best and worst case scenarios?
# Ans: O(nlog(n)


###########################

# QUICKSORT

###########################

# What is Quicksort? Can you describe how it works?

# The function partition() takes in a list and pivot is incomplete. Finish implementing the function below
def partition(lst, pivot):
	less = []
	eq = []
	great = []
	
	# YOUR CODE HERE
	for num in lst:
		if num < pivot:
			less.append(num)
		elif num == pivot:
			eq.append(num)
		else:
			great.append(num)
	
	return less, eq, great


# What is the time complexity of Quicksort, can you describe best and worst case scenarios?
# Ans: O(nlog(n)) best case and O(n^2) worst case
# Ans: Best case - pick good pivot every time so that less partition and greater partition are roughly equal
# Worst case - pick bad pivot so every time all the other elements end up on one side
###########################

# FILE INPUT/OUTPUT

###########################

# Ask the user to input a word. Then, write the word letter by letter into an external file.
word = input("Please enter a word: ")

o = open("AM-Check-in-3.txt", "w+")

for i in word:
	o.write(i + "\n")

o.close()

# Reading from the file that you just created, create a dictionary where the keys are the unique letters of your input and the values are how often those letters occur. 

d = {}

f = open("AM-Check-in-3.txt")
lines = f.readlines()
lines = [line.strip() for line in lines]
f.close()

for letter in lines:
	if letter in d:
		d[letter] += 1
	else:
		d[letter] = 1
print(d)

# What's the difference between read() and readlines()?
# Ans: read() grabs the entire contents of a file and stores it into a string. readlines() combines read() and split() functions into one by automatically storing the words in a list
