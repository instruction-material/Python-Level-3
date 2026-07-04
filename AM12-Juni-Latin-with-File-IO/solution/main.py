###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

f = open("input_no_punctuation.txt")
lines = f.readlines()
lines = [x.strip() for x in lines]
f.close()


def translate(word):
    new_word = ""

    for i in range(1, len(word)):
        new_word += word[i]

    new_word += word[0] + "ay"

    return new_word


l = []
o = open("output.txt", "w+")

for line in lines:
    l.append(line.split())

for line in l:
    a = ""
    for word in line:
        a += translate(word) + " "
    o.write(a + "\n")

o.close()

"""BONUS: Make sure it works for punctuation

f = open('input_punctuation.txt')
lines = f.readlines()

punctuation = ",.!?;"

for line in l:
  a = ""
  for word in line:
    if word[len(word) - 1] in punctuation:
      newWord = ""
      p = word[len(word - 1)]
      for i in range(len(word) - 1):
        newWord += word[i]
      a += translate(newWord) + p
    else:
      a += translate(word) + " "
    o.write(a + "\n")

o.close()
"""
