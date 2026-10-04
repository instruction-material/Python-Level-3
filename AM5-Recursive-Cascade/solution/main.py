# Make a cascade function: cascade takes in a string, s, and prints out first the first char, then the first 2, then the first 3 … until all of s is printed
def cascade(s):
    if not s:
        return
    if len(s) > 1:
        cascade(s[:-1])
    print(s)


# Now, make the inverse cascade: first “dog”, then “do”, then “d”
def inverse_cascade(s):
    if not s:
        return
    print(s)
    if len(s) > 1:
        inverse_cascade(s[:-1])


if __name__ == "__main__":
    word = "lemmings"
    cascade(word)
    inverse_cascade(word)
