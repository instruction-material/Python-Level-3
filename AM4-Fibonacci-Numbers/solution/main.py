# Recursive solution
def fibonacci(n):
    # Base cases
    if n <= 1:
        return 0
    if n == 2:
        return 1

    # Recursive calls
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    n = int(input("\n\nEnter a positive position n (position 1 is 0): "))
    if n < 1:
        raise ValueError("The Fibonacci position must be positive.")
    print(fibonacci(n))

    # Iterative solution
    a = 0
    b = 1

    for i in range(1, n):
        c = a + b
        a = b
        b = c

    print(a)
