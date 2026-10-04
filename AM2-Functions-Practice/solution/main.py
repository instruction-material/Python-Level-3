"""Iterative review references with explicit integer domains and quiet imports."""


def product(a, b, c):
    """Return the product of three numeric inputs."""
    return a * b * c


def average(x, y):
    """Return the arithmetic mean of two numeric inputs."""
    return (x + y) / 2


def count_letter(word, letter):
    """Count one exact character, case-sensitively; empty words return zero."""
    if not isinstance(word, str) or not isinstance(letter, str) or len(letter) != 1:
        raise ValueError("word must be a string and letter a single character")
    counter = 0
    for character in word:
        if character == letter:
            counter += 1
    return counter


def count_seven(number):
    """Count digit 7 in an integer's magnitude, without float conversion."""
    if type(number) is not int:
        raise ValueError("number must be an integer, not bool")
    number = abs(number)
    counter = 0
    while number > 0:
        if number % 10 == 7:
            counter += 1
        number //= 10
    return counter


def exponent(a, b):
    """Return a**b by repeated multiplication; b must be a nonnegative integer."""
    if type(b) is not int or b < 0:
        raise ValueError("b must be a nonnegative integer, not bool")
    answer = 1
    for _ in range(b):
        answer *= a
    return answer


def factorial(n):
    """Return n! iteratively, including 0! = 1."""
    if type(n) is not int or n < 0:
        raise ValueError("n must be a nonnegative integer, not bool")
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


def hailstone(n, max_steps=10000):
    """Count terms including n and final 1; raise if the transition cap is hit."""
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer, not bool")
    if type(max_steps) is not int or max_steps < 0:
        raise ValueError("max_steps must be a nonnegative integer, not bool")
    length = 1
    steps = 0
    while n != 1:
        if steps >= max_steps:
            raise RuntimeError("Hailstone transition cap reached before 1")
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
        length += 1
    return length


if __name__ == "__main__":
    print("product(2, 3, 5) =", product(2, 3, 5))
    print("average(2, 3) =", average(2, 3))
    print('count_letter("bookkeeper", "e") =', count_letter("bookkeeper", "e"))
    print("count_seven(177877) =", count_seven(177877))
    print("exponent(2, 10) =", exponent(2, 10))
    print("factorial(4) =", factorial(4))
    print("hailstone(10) =", hailstone(10))
