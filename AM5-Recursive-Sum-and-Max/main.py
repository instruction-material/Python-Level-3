l = [1, 2, 3, 4, 5, 6]


def sum_recursion(l):
    if len(l) == 1:
        return l[0]

    return l[0] + sum_recursion(l[1:])


def max_recursion(l):
    if len(l) == 1:
        return l[0]

    if l[0] > l[-1]:
        return max_recursion(l[:-1])
    else:
        return max_recursion(l[1:])


print(sum_recursion(l))
print(max_recursion(l))
