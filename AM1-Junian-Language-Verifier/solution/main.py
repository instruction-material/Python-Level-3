word = input("Please type in a word for verification: ")

vowels = "aeiou"
num_vowels = 0

for letter in word:
    if letter in vowels:
        num_vowels += 1

if num_vowels < 2:
    print("Your word is invalid.")
elif len(word) % 2 != 0:
    print("Your word is invalid.")
elif word[0] == word[len(word) - 1]:  # Optionally, introduce word[-1]
    print("Your word is invalid.")
else:
    print("Your word is valid.")
