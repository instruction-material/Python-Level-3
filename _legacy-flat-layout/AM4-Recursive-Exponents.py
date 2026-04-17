"""
Write a recursive function that takes in two numbers, called b (for base) and p (for power), and returns the value of b to the power of p (where p is a positive integer). If you are unfamiliar with exponents, when we say b to the power of p, we mean that we should have p amount of b’s multiplying each other. For example, 3 to the power of 4 would be 3 * 3 * 3 * 3.

Again, think about the base cases and what should happen to the original input when we make the recursive call.
"""


def exponent(base, power):
	if power == 0:
		return 1
	return base * exponent(base, power - 1)


print(exponent(3, 4))
