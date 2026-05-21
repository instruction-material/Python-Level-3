def linearSearch(l, v):
    for item in l:
        if item == v:
            return True
    return False


l = [1, 2, 3, 4, 5]
print(linearSearch(l, 4))
print(linearSearch(l, 6))
