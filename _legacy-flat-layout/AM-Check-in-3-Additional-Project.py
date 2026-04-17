"""
Each line of the input file contains a single letter. Read in all of the letters in the input file and store them all in a list. Using either Bubble Sort, Merge Sort, or Quicksort, sort the letters from smallest to largest ASCII order and output the results to a file. (You may use and modify the code that you previously wrote for any of those sorting algorithms).
"""

with open("AM-Check-in-3-Additional-Project-input.txt") as f:
	lines = f.readlines()
	lines = [line.strip() for line in lines]

# sort the list according to ASCII order
# this solution uses Bubble Sort; the student can also use Merge Sort or Quicksort instead 
for i in range(len(lines) - 1, 0, -1):
	for j in range(0, i):
		if ord(lines[j]) > ord(lines[j + 1]):
			temp = lines[j]
			lines[j] = lines[j + 1]
			lines[j + 1] = temp

o = open("AM-Check-in-3-Additional-Project-output.txt", "w+")

for i in lines:
	o.write(i + "\n")

o.close()
