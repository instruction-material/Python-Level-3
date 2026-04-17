"""
Write and test the functions described in the comments of the starter code!
"""


# (1) Write a function that takes in a list of numbers and returns a list with every number doubled.
def double(numbers):
	result = []
	for number in numbers:
		result.append(number * 2)
	return result


print(double([1, 2, 3]))


# (2) Write a function that takes in a list of words and returns a list of only the words that start with the letter 'a.'
def startsWithA(words):
	result = []
	for word in words:
		if word[0] == 'a':
			result.append(word)
	return result


print(startsWithA(['apple', 'banana', 'ant', 'orange']))


# (3) Write a function that takes in a list of numbers and returns the number of even numbers in the list.
def numOfEvens(numbers):
	count = 0
	for number in numbers:
		if number % 2 == 0:
			count += 1
	return count


print(numOfEvens([2, 4, 6, 7]))


# (4) Write a function that takes in a list of numbers and returns the sum of the list.
def sumOfNumbers(numbers):
	sum = 0
	for number in numbers:
		sum += number
	return sum


print(sumOfNumbers([-1, 1, 2, 3]))


# (5) Write a function that takes in a list of distinct numbers and returns the index of the largest number in the list.
def indexOfLargestNumber(numbers):
	index = 0
	largestNum = numbers[0]
	for i in range(0, len(numbers)):
		if numbers[i] > largestNum:
			index = i
			largestNum = numbers[i]
	return index


print(indexOfLargestNumber([-4, -6, -3]))


# (6) For a given integer N, print all perfect squares less than or equal to N.
def allSquares(N):
	i = 0
	while True:
		perfectSquare = i * i
		if perfectSquare <= N:
			print(perfectSquare)
		else:
			break
		i += 1


allSquares(101)


# (7) Write a function that takes in an integer N and returns the greatest integer x for which 2^x is less than or equal to N.
def largestPowerOfTwo(N):
	i = 0
	while True:
		powerOfTwo = 2**i
		if (powerOfTwo > N):
			return i - 1
		i += 1


print(largestPowerOfTwo(65))


# (8) Write a function that takes in an integer N and returns the sum of 1! + 2! + ... + N!.
def factorialSum(N):
	sum = 0
	for i in range(1, N + 1):
		factorial = 1
		for j in range(1, i + 1):
			factorial *= j
		sum += factorial
	return sum


print(factorialSum(3))


# (9) Write a function that takes in a positive integer N and returns its largest divisor less than N.
def largestDivisor(N):
	for i in range(N - 1, 0, -1):
		if N % i == 0:
			return i


print(largestDivisor(24))


# (10) Write a function that takes in a list of integers (positive or negative) and returns the largest product that can be made with any two numbers from the list.
def largestProduct(numbers):
	largestNum = numbers[0] * numbers[1]
	for i in range(0, len(numbers)):
		for j in range(0, len(numbers)):
			if numbers[i] * numbers[j] > largestNum and i != j:
				largestNum = numbers[i] * numbers[j]
	return largestNum


print(largestProduct([0, 5, 9]))
print(largestProduct([-3, -8, 10]))


# (11) Write a function that takes in a list of integers (positive or negative) and return True if any pair of the numbers in the list sum to 0, Otherwise, return False.
def sumsToZero(numbers):
	for i in range(0, len(numbers)):
		for j in range(0, len(numbers)):
			if numbers[i] + numbers[j] == 0 and i != j:
				return True
	return False


print(sumsToZero([0, -1, 2]))
print(sumsToZero([-5, 8, 5]))


# (12) Write a function that takes in a list of integers and returns a list of the most commonly occurring integers in the list. For example, if the list is [3, 6, 2, 2, 6], the function should return [2,6].
def mostCommonNumbers(numbers):
	freq = {}
	for number in numbers:
		if number in freq:
			freq[number] += 1
		else:
			freq[number] = 1
	highestFreq = 0
	mostCommon = []
	for number in freq:
		if freq[number] > highestFreq:
			mostCommon = [number]
			highestFreq = freq[number]
		elif freq[number] == highestFreq:
			mostCommon.append(number)
	return mostCommon


print(mostCommonNumbers([6, 3, 2, 2]))
print(mostCommonNumbers([5, 4, 5, 4, 5, 4]))
print(mostCommonNumbers([1, 2, 3]))


# (13) Write a function that takes in a string and returns the string in reverse order.
def reverseString(str):
	reverseStr = ''
	for i in range(len(str) - 1, -1, -1):
		reverseStr += str[i]
	return reverseStr


print(reverseString("hello"))


# (14) Write a function that takes in a string and returns the number of vowels in the string.
def countVowels(str):
	count = 0
	for i in str:
		if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
			count += 1
	return count


print(countVowels('mooncake'))


# (15) Write a function that takes in a list of numbers and returns the number of numbers that appear exactly twice in the list.
def countPairs(numbers):
	freq = {}
	count = 0
	for number in numbers:
		if number in freq:
			freq[number] += 1
		else:
			freq[number] = 1
	for number in freq:
		if freq[number] == 2:
			count += 1
	return count


print(countPairs([1, 1, 2, 2, 3, 3, 3, 4]))


# (16) Write a function that takes in a list of distinct numbers and return the list with the smallest and largest numbers swapped.
def swapMinMax(numbers):
	minIndex = 0
	maxIndex = 0
	minNum = numbers[0]
	maxNum = numbers[0]
	for i in range(0, len(numbers)):
		number = numbers[i]
		if number < minNum:
			minIndex = i
			minNum = number
		elif number > maxNum:
			maxIndex = i
			maxNum = number
	numbers[minIndex] = maxNum
	numbers[maxIndex] = minNum
	return numbers


print(swapMinMax([1, 2, 3, 4]))
