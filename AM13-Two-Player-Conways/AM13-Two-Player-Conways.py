"""
Read the description of the two player version of Conway’s Game of Life found at the bottom of this page. In essence, you will need to create a starting file for each player and then load it into a playing grid. Let each player take turns selecting a place where they want to add a cell, and a place where they want to remove a cell. After updating those locations, go through a single step of Conway’s four rules as explained in the previous project. Let each player continue taking turns until a player loses all of their cells.
"""


def print_board(game):
	"""Prints the game board.

	:param game: The game board represented as a 2D list.
	"""
	
	# Print column indices
	print(" ", end=" ")
	for i in range(len(game[0])):
		print(i, end=" ")
	print()
	
	# Print each row with its index
	for i, row in enumerate(game):
		print(i, end=" ")
		for cell in row:
			print("O" if cell == 1 else "X" if cell == 2 else "-", end=" ")
		print()


def neighbors(grid, alive, i, j):
	"""Returns new cell state based on Conway's Game of Life rules.

	:param grid: The game board represented as a 2D list.
	:param alive: The current state of the cell.
	:param i: Row index of the cell.
	:param j: Column index of the cell.
	:return: New state of the cell.
	"""
	
	# Determine the states of the cell's neighbors
	neighbor_coords = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
	                   (i, j - 1), (i, j + 1),
	                   (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
	
	neighbors = [grid[x][y] for x, y in neighbor_coords if 0 <= x < len(grid) and 0 <= y < len(grid[0])]
	counts = {1: neighbors.count(1), 2: neighbors.count(2)}
	count_alive = sum(counts.values())
	
	# Apply Conway's rules
	if alive in [1, 2] and count_alive not in [2, 3] or alive == 0 and count_alive != 3:
		return 0
	return 2 if counts[2] > counts[1] else 1


def count_board(grid):
	"""Count the number of cells for each player.

	:param grid: The game board represented as a 2D list.
	:return: Tuple containing the counts for player 1 and player 2.
	"""
	
	cells = [cell for row in grid for cell in row]
	return cells.count(1), cells.count(2)


# Initialize board
grid = [[0] * 10 for _ in range(10)]

# Load player 1 coordinates
with open("player1.in") as f:
	for line in f:
		x, y = map(int, line.split())
		grid[x][y] = 1

# Load player 2 coordinates
with open("player2.in") as f:
	for line in f:
		x, y = map(int, line.split())
		grid[x][y] = 2

# Initialize game
print_board(grid)
input("Press Enter to start: ")

while True:
	# Create a new grid based on the current grid's state
	grid = [[neighbors(grid, grid[i][j], i, j) for j in range(len(grid[0]))] for i in range(len(grid))]
	
	print_board(grid)
	o_count, x_count = count_board(grid)
	print(f"Player O has {o_count} cells alive")
	print(f"Player X has {x_count} cells alive")
	
	if not (o_count and x_count):
		break
	
	# Take turns
	player = 1 if o_count > x_count else 2
	print(f"It's Player {player}'s Turn.")
	x_add = int(input("Please enter the row of the cell you wish to add: "))
	y_add = int(input("Please enter the column of the cell you wish to add: "))
	grid[x_add][y_add] = player
	x_del = int(input("Please enter the row of the cell you wish to delete: "))
	y_del = int(input("Please enter the column of the cell you wish to delete: "))
	grid[x_del][y_del] = 0

# Determine winner
o_count, x_count = count_board(grid)
if o_count > x_count:
	print("Player O has won the game")
elif x_count > o_count:
	print("Player X has won the game")
else:
	print("Both players are dead. It's a tie!")
