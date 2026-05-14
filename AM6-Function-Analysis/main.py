# O(n) - we loop through all of the whole numbers from 0 up to n,
# so this function has a linear runtime
def f1(n):
    for i in range(n):
        print(i)


# O(n) - technically this function does exactly half as many things
# as the previous function, but we drop constants and coefficients
def f2(n):
    for i in range(n // 2):
        print(i)


# O(n^2) - the outer loop does n/2 things, and the inner loop does
# n/4 things, so in all there are (n^2)/8 things being done, but 
# we always drop constants and coefficients, so we just say O(n^2)
def f3(n):
    k = 0
    for i in range(n // 2):
        for j in range(n // 4):
            k += 1
            print(k)


# O(n^2) - the inner loop runs 0 times, then 1 time, then 2 times,
# and so on up to n-1 times, meaning we are looping 1 + 2 + ... + n-1,
# which simplifies down mathematically to O(n^2)
def f4(n):
    k = 0
    for i in range(n):
        for j in range(i):
            k += 1
            print(k)


# O(n) - this recursive function starts at n and counts down to 0.
# Because we visit each of those numbers exactly once, this is linear
def f5(n):
    if n <= 0:
        return
    else:
        print(n)
        f5(n - 1)


# O(log(n)) - every time the function is called, the input is cut
# in half. Most commonly in CS, "log" has a hidden base of 2, which
# is the case here
def f6(n):
    if n <= 1:
        return
    else:
        print(n)
        f6(n // 2)


# O(n^3) - every loop repeats n times, and because they are nested,
# we count the number of iterations by multiplying the amount of 
# times that each loop runs
def f7(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)
    return


# O(n+m) - this function is dependent upon two different inputs,
# and each input corresponds to a linear portion of the function
def f8(n, m):
    for i in range(n):
        print(i)
    for i in range(m):
        print(i)


# O(n*m) - as mentioned previously, with nested loops, we multiply
# the number of iterations of both loops. This function is dependent
# upon n and m, so we multiply them to get the runtime
def f9(n, m):
    for i in range(m):
        for j in range(n):
            print(i, j)


# O(n) - initially this appears to be the same as the previous, but
# the function is exited after the inner loop iterates n times
def f10(n, m):
    for i in range(m):
        for j in range(n):
            print(i, j)
        return


""" Now the list problems: use the length of the list as N
    Note: all lists are of INTEGERS (this includes negative numbers and zero) """


# O(n) - we loop through each element of the list once, and the list
# has n elements
def f11(lst):
    for item in lst:
        print(item)


# O(n^2) - the function is comparing every element with every other
# element. In worst case scenario, every number in the list is unique,
# so we never return early. Even though not every use of this function
# will be O(n^2), we base the runtime off of the worst case scenario
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


# O(n) - like before, even though the possibility exists for the
# function to return before processing every single element, the
# worst case scenario would be that 0 is not in the list, so the
# runtime would be linear
def f13(lst):
    for item in lst:
        if item == 0:
            return True
    return False


# O(n) - this is the exact same thing as before, just with 1
# instead of 0
def f14(lst):
    for item in lst:
        if item == 1:
            return True
    return False
