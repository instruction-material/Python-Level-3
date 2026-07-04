def is_palindrome(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return (is_palindrome(str[1:-1]))


n = input("\n\nEnter the string you would like to check. \nWe will check if it is a palindrome. \n")
print(is_palindrome(n))


def is_palindrome(str): return True if len(str) <= 1 else False if str[0] != str[-1] else (is_palindrome(str[1:-1]))
