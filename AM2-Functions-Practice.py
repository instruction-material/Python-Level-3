"""
Write a program that contains each of the following functions:
A function that takes in three numbers and returns the product of the numbers
A function that takes in two numbers and returns their average (the sum of the numbers divided by the amount of numbers)
A function that takes in a word and a letter, and returns how many times that letter occurs in the word
A function that takes in an integer and returns how many digits are 7
A function that takes in two numbers, a and b, and returns a to the power of b (remember that exponents just represent repeated multiplication)
"""


def product(a, b, c):
	return a * b * c


def average(x, y):
	return (x + y) / 2


def countLetter(word, letter):
	counter = 0
	for i in range(len(word)):
		if word[i] == letter:
			counter += 1
	return counter


# approach that is typically easier for students
def countSeven(number):
	number = str(number)
	counter = 0
	for i in range(len(number)):
		if number[i] == '7':
			counter += 1
	return counter


'''
Alternative (but recommended) approach
def countSeven(number): 
  counter = 0 
  while number > 0: 
    if number % 10 == 7: 
      counter += 1 
    number = int(number/10) 
  return counter
'''


def exponent(a, b):
	answer = 1
	for i in range(0, b):
		answer *= a
	return answer


def factorial(n):
	answer = 1
	for i in range(1, n + 1):
		answer *= i
	return answer


def hailstone(n):
	length = 1
	while n != 1:
		length += 1
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
	return length


print("product(2,3,5) =", product(2, 3, 5))
print("average(2,3) =", average(2, 3))
print("countLetter(\"bookkeeper\", \"e\") =", countLetter("bookkeeper", "e"))
print("countSeven(177877) =", countSeven(177877))
print("exponent(2, 10) =", exponent(2, 10))
print("factorial(4) =", factorial(4))
print("hailstone(10) =", hailstone(10))
