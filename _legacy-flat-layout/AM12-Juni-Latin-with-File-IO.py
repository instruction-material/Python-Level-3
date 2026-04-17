"""
To write a word in Juni Latin, move the very first letter to the end of the word and add "-ay". This may sound like Pig Latin, but Pig Latin is actually a bit more complicated! Read the sentences from input_no_punctuation.txt into the program, and run each word through your Juni Latin translate function to get a resulting sentence that is completely in Juni Latin. Think about what kind of input the function takes, and how you can prepare a string before passing it into the function. Write out the resulting translation to a file.
Bonus: can you make your program handle input that contains punctuation like input_punctuation.txt?
"""

with open('input_no_punctuation.txt') as f:
	lines = f.readlines()
	lines = [x.strip() for x in lines]


def translate(word):
	newWord = ""
	
	for i in range(1, len(word)):
		newWord += word[i]
	
	newWord += word[0] + 'ay'
	
	return newWord


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
