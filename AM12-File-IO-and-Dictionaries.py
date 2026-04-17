"""
Read each line from the given input file into a dictionary. Every other line, starting from the first line, is a key, with the subsequent line being its value (in other words, odd number lines contain a key, and the even number lines contain the corresponding value).
"""

with open("input.txt") as f:
	lines = f.readlines()
	lines = [line.strip() for line in lines]

d = {}

keys = []
values = []
for i in range(len(lines)):
	if i % 2:
		values.append(lines[i])
	else:
		keys.append(lines[i])

for i in range(len(keys)):
	d[keys[i]] = values[i]

print(d)
