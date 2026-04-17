"""
Write a program that reads in a text file containing a coordinate pair of numbers on each line, and then fills in a two-dimensional grid with an “o” at each of the coordinate locations listed in the text file. After the initial grid has been set up, generate the next step according to the rules of Conway’s Game of Life. Once the next step has been generated, set the original grid equal to the new one. Be sure to print out the new grid once it has been created! Make this process repeat forever.
"""

# IMPORTANT: GIVE MORE SPACE FOR THE CONSOLE SO THE GAME CAN PROPERLY DISPLAY

import time


GRID_HEIGHT = 30
GRID_WIDTH = 60

# Building grid of size 30x60 but that can be changed
# (Pretty important to have the y-axis be 30 so that the animation covers the entire screen on repl)
grid = []
for row in range(GRID_HEIGHT):
	line = []
	for col in range(GRID_WIDTH):
		line.append(False)
	grid.append(line)

# Reading files of coordinates
f = open("repeat.in")
data = f.readlines()
f.close()

coords = []
for line in data:
	line = [int(coord) for coord in line.split()]
	coords.append(line)

# Setting file coordinates to be True/Alive, everything else initialized as False/Dead
for point in coords:
	grid[point[0]][point[1]] = True


# Function to print the board with O for Alive and - for Dead
def printBoard(game):
	for row in game:
		for boolean in row:
			if boolean:
				print("O", end="")
			else:
				print("-", end="")
		print("")


# Function to count neighbors Alive or Dead and return result based on Conway's rules.
def neighbors(grid, alive, row, col):
	countAlive = 0
	if col - 1 >= 0 and row - 1 >= 0 and grid[row - 1][col - 1]:
		countAlive += 1
	if row - 1 >= 0 and grid[row - 1][col]:
		countAlive += 1
	if col + 1 < len(grid[0]) and row - 1 >= 0 and grid[row - 1][col + 1]:
		countAlive += 1
	if col - 1 >= 0 and grid[row][col - 1]:
		countAlive += 1
	if col + 1 < len(grid[0]) and grid[row][col + 1]:
		countAlive += 1
	if col - 1 >= 0 and row + 1 < len(grid) and grid[row + 1][col - 1]:
		countAlive += 1
	if row + 1 < len(grid) and grid[row + 1][col]:
		countAlive += 1
	if col + 1 < len(grid[0]) and row + 1 < len(grid) and grid[row + 1][col + 1]:
		countAlive += 1
	
	# Rule 1: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
	if alive and countAlive < 2:
		return False
	
	# Rule 2: Any live cell with two or three live neighbours lives on to the next generation.
	elif alive and countAlive < 4:
		return True
	
	# Rule 3: Any live cell with more than three live neighbours dies, as if by overpopulation.
	elif alive:
		return False
	
	# Rule 4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
	if not alive and countAlive == 3:
		return True
	
	# Otherwise, return original
	return alive


input(
	"Welcome to Conway's Game of Life. We start with a 30x60 grid \nof cells, either alive or dead. Here are the rules:\n\t1) Any live cell with fewer than two live neighbors \n\t   dies, as if by underpopulation.\n\t2) Any live cell with two or three live neighbors \n\t   lives on to the next generation.\n\t3) Any live cell with more than three live neighbors \n\t   dies, as if by overpopulation.\n\t4) Any dead cell with exactly three live neighbors \n\t   becomes a live cell, as if by reproduction.\nPress Enter to continue:")
printBoard(grid)
input("Press Enter to start:")
while True:
	print("\033c")
	newGrid = []
	for _ in range(30):
		line = []
		for _ in range(60):
			line.append(False)
		newGrid.append(line)
	
	for row in range(GRID_HEIGHT):
		for col in range(GRID_WIDTH):
			newGrid[row][col] = neighbors(grid, grid[row][col], row, col)
	
	printBoard(newGrid)
	grid = newGrid
	
	# Pause for animation to take effect
	time.sleep(0.5)

"""
import time

# Building grid of size 30x60 using list comprehension
grid = [[False]*60 for _ in range(30)]

# Reading files of coordinates
with open("repeat.in") as f:
    coords = [list(map(int, line.split())) for line in f]

# Setting file coordinates to be True/Alive, everything else initialized as False/Dead
for x, y in coords:
    grid[x][y] = True

# Function to print the board with O for Alive and - for Dead
def printBoard(game):
    for line in game:
        print(''.join("O" if boolean else "-" for boolean in line))


# Function to count neighbors Alive or Dead and return result based on Conway's rules.
def neighbors(grid, row, col):
    countAlive = sum([grid[row+dx][col+dy] for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                    if 0 <= row+dx < len(grid) and 0 <= col+dy < len(grid[0])])
    alive = grid[row][col]
    return alive and 2 <= countAlive <= 3 or not alive and countAlive == 3

input(
    "Welcome to Conway's Game of Life. We start with a 30x60 grid \nof cells, either alive or dead. Here are the rules:\n\t1) Any live cell with fewer than two live neighbors \n\t   dies, as if by underpopulation.\n\t2) Any live cell with two or three live neighbors \n\t   lives on to the next generation.\n\t3) Any live cell with more than three live neighbors \n\t   dies, as if by overpopulation.\n\t4) Any dead cell with exactly three live neighbors \n\t   becomes a live cell, as if by reproduction.\nPress Enter to continue:")
printBoard(grid)
input("Press Enter to start:")
while True:
    print("\033c")
    newGrid = [[neighbors(grid, row, col) for col in range(60)] for row in range(30)]
    printBoard(newGrid)
    grid = newGrid
    time.sleep(0.5)
"""
