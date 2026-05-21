# Make a cascade function: cascade takes in a string, s, and prints out first the first char, then the first 2, then the first 3 … until all of s is printed
def cascade(s):
    if len(s) > 1:
        cascade(s[:-1])
    print(s)


word = "lemmings"
cascade(word)


# Now, make the inverse cascade: first “dog”, then “do”, then “d”
def inverse_cascade(s):
    print(s)
    if len(s) > 1:
        inverse_cascade(s[:-1])


inverse_cascade(word)
