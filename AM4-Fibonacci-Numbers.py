"""
Write a recursive function that takes in an integer n and returns the nth Fibonacci number. The Fibonacci sequence is a special ordering of numbers that starts with 0 and 1, and then every next term is the sum of the two previous terms. For example, starting with 0 and 1, the next term would be 0 + 1 = 1; the following term would be 1 + 1 = 2, and then 1 + 2 = 3, then 2 + 3 = 5, and so on. The first 8 terms of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, and 13.
"""


# Recursive solution
def fibonacci(n):
	# Base cases
	if n <= 1:
		return 0
	if n == 2:
		return 1
	
	# Recursive calls
	return fibonacci(n - 2) + fibonacci(n - 1)


n = int(input("\n\nEnter n, where n will represent the nth Fibonacci number: "))
print(fibonacci(n))

# Iterative solution
a = 0
b = 1

for _ in range(1, n):
	c = a + b
	a = b
	b = c

print(a)
