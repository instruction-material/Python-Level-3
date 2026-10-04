def sum_recursion(values):
    if not values:
        return 0
    if len(values) == 1:
        return values[0]

    return values[0] + sum_recursion(values[1:])


def max_recursion(values):
    if not values:
        raise ValueError("The maximum of an empty list is undefined.")
    if len(values) == 1:
        return values[0]

    if values[0] > values[-1]:
        return max_recursion(values[:-1])
    else:
        return max_recursion(values[1:])


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6]
    print(sum_recursion(values))
    print(max_recursion(values))
