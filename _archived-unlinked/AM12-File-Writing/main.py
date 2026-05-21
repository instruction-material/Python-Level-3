f = open("numbers.txt", "w+")

for i in range(10):
    f.write("This is line %d\n" % (i + 1))

f.close()

"""
Alternatively, you can show your student this method for opening and writing to files

with open("numbers.txt", "w+") as f:
  for i in range(10):
    f.write("This is line %d" % (i+1))
"""
