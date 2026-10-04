def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


if __name__ == "__main__":
    text = input(
        "\n\nEnter the string to check as a literal palindrome: "
    )
    print(is_palindrome(text))
