def linear_search(l, v):
    for item in l:
        if item == v:
            return True
    return False


l = [1, 2, 3, 4, 5]
print(linear_search(l, 4))
print(linear_search(l, 6))
