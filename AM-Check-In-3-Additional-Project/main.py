f = open("input.txt")
lines = f.readlines()
lines = [line.strip() for line in lines]
f.close()

# sort the list according to ASCII order
# this solution uses Bubble Sort; the student can also use Merge Sort or Quicksort instead 
for i in range(len(lines)-1, 0, -1):
  for j in range(0, i):
    if ord(lines[j]) > ord(lines[j+1]):
      temp = lines[j]
      lines[j] = lines[j+1]
      lines[j+1] = temp


o = open("output.txt", "w+")

for i in lines:
  o.write(i + "\n")
    
o.close()
