input = input("Please enter a paragraph: ")

words = input.split()
wordsSet = set()
for word in words:
    word = word.lower().replace(".", "")
    wordsSet.add(word)

print("The unique words in your paragraph are: ")
print(wordsSet)
