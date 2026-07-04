###########################
###   CODING STANDARD   ###
###########################
# Use named constants, descriptive names, and purpose comments before nontrivial scopes

d = {}

f = open("input.txt")
lines = f.readlines()
print(lines)
lines = [line.strip() for line in lines]
print(lines)
f.close()

keys = []
values = []
for i in range(len(lines)):
    if i % 2 == 1:
        values.append(lines[i])
    else:
        keys.append(lines[i])

for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)
