def isPalindrome(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return (isPalindrome(str[1:-1]))


n = input("\n\nEnter the string you would like to check. \nWe will check if it is a palindrome. \n")
print(isPalindrome(n))


def isPalindrome(str): return True if len(str) <= 1 else False if str[0] != str[-1] else (isPalindrome(str[1:-1]))
