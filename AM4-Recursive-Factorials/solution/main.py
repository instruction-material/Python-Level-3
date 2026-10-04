def recursive_factorial(num):
    if num == 0:
        return 1
    return num * recursive_factorial(num - 1)


if __name__ == "__main__":
    print(recursive_factorial(5))
