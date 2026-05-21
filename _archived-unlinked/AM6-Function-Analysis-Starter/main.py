def f1(n):
    for i in range(n):
        print(i)


def f2(n):
    for i in range(n // 2):
        print(i)


def f3(n):
    k = 0
    for i in range(n // 2):
        for j in range(n // 4):
            k += 1
            print(k)


def f4(n):
    k = 0
    for i in range(n):
        for j in range(i):
            k += 1
            print(k)


def f5(n):
    if (n <= 0):
        return
    else:
        print(n)
        f5(n - 1)


def f6(n):
    if (n == 1):
        return
    else:
        print(n)
        f6(n // 2)


def f7(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
                return


def f8(n, m):
    for i in range(n):
        print(i)
    for i in range(m):
        print(i)


def f9(n, m):
    for i in range(m):
        for j in range(n):
            print(i, j)


def f10(n, m):
    for i in range(m):
        for j in range(n):
            print(i, j)
        return


""" Now the list problems: use the length of the list as N
    Note: all lists are of INTEGERS (this includes negative numbers and zero) """


def f11(lst):
    for item in lst:
        print(item)


def f12(lst):
    n = len(lst)
    for i in range(n):
        item1 = lst[i]
        for j in range(n):
            item2 = lst[j]
            if i == j:
                continue
            if item1 == item2:
                return True
    return False


def f13(lst):
    for item in lst:
        if item == 0:
            return True
    return False


def f14(lst):
    for item in lst:
        if item == 1:
            return True
    return False
