input = input("Please enter a paragraph: ")

words = input.split()
wordsSet = set()
for word in words:
    word = word.lower().replace(".", "")
    wordsSet.add(word)

letterCounter = {}
for word in wordsSet:
    length = len(word)
    if length in letterCounter:
        letterCounter[length] += 1
    else:
        letterCounter[length] = 1

for key in letterCounter:
    print("You entered %d %d-character words." % (letterCounter[key], key))
