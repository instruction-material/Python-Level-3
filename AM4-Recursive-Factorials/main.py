def recursive_factorial(num):
    if num == 0:
        return 1
    return num * recursive_factorial(num - 1)


print(recursive_factorial(5))
