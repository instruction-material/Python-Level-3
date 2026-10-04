def linear_search(values, target):
    for item in values:
        if item == target:
            return True
    return False


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    print(linear_search(values, 4))
    print(linear_search(values, 6))
