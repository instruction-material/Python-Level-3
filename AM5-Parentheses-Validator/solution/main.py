# iterative way
def parentheses(brackets):
    dictionary = {"(": ")", "[": "]", "{": "}"}
    stack = []

    if len(brackets) == 0:
        return True

    for ch in brackets:
        if ch in dictionary:
            stack.append(ch)
        elif ch in dictionary.values():
            if len(stack) == 0:
                return False
            elif dictionary[stack.pop()] != ch:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print(parentheses("{()[]}"))
print(parentheses("{()[])"))


# recursive way
def rec_parentheses(brackets):
    if len(brackets) == 0:
        return True

    for i in range(len(brackets) - 1):
        check = brackets[i] + brackets[i + 1]
        if check == "()" or check == "{}" or check == "[]":
            new_bracks = brackets[:i] + brackets[i + 2 :]
            return rec_parentheses(new_bracks)

    return False


print(rec_parentheses("{()[]}"))
print(rec_parentheses("{(((())))[}]"))
