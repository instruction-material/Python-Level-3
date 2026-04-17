"""
First, create lists containing the following numbers:
The numbers 1 through 20
The first 20 even numbers
The first 10 square numbers (1, 4, 9, etc.)
Once you have created those lists, write the following functions:
A function that takes in two lists and returns the sum of both lists
A function that takes in a list and returns the minimum value in that list
A function that takes in a list and returns the maximum value in that list
A function that takes in a list of lists, and returns the sum of all those lists
A function that takes in a list of lists, and returns a new list made from “flattening” the lists (putting every element from each list into a single list)
A function that takes in a list of lists, and returns a new list containing the maximum value from each of the input lists. Can you find a way to use the function that you already made that returns the maximum of a list?
"""

# Create a list of the numbers 1 through 20 (without hard-coding the list)
nums = []
for i in range(20):
	nums.append(i + 1)
print(nums)

# Create a list of the first 10 even numbers (without hard-coding the list)
evens = []
for i in range(1, 21):
	if i % 2 == 0:
		evens.append(i)
print(evens)

# Create a list of the first 10 perfect squares (without hard-coding the list)
squares = []
for i in range(1, 11):
	squares.append(i * i)
print(squares)


# Write a function that takes in two lists and returns the sum of both lists
def sumLists(l1, l2):
	answer = 0
	for num in l1:
		answer += num
	for num in l2:
		answer += num
	return answer


a = [3, 5, 3, 2, -4, 1]
b = [4, 8, 9, -3, -5]
print(sumLists(a, b))


# Write a function that takes in a list and returns the minimum value in that list
def minimum(l):
	minNum = l[0]
	for num in l:
		if num < minNum:
			minNum = num
	return minNum


print(minimum(a))


# Write a function that takes in a list and returns the maximum value in that list
def maximum(l):
	maxNum = l[0]
	for num in l:
		if num > maxNum:
			maxNum = num
	return maxNum


print(maximum(a))


# Write a function that takes in a list of lists, and returns the sum of all those lists
def sumListOfLists(l):
	answer = 0
	for element in l:
		for num in element:
			answer += num
	return answer


l = [[1, 2, 3], [4, 5, 6], [], [7, 8, 9]]
print(sumListOfLists(l))


# Write a function that takes in a list of lists, and returns a new list made from “flattening” the lists (putting every element from each list into a single list)
def flattenList(l):
	newList = []
	for element in l:
		for num in element:
			newList.append(num)
	return newList


print(flattenList(l))


# Write a function that takes in a list of lists that returns a new list of all the individual maxes from each list. Can you find a way to use the function that you already made that returns the maximum of a list?
def maxList(l):
	mList = []
	for i in range(len(l)):
		if len(l[i]) > 0:
			mList.append(maximum(l[i]))
	return mList


print(maxList(l))
