"""
Using the AI player that you developed, write a program that makes the AI play 1,000 games against the random computer player. Print out the number of ties, the number of random computer player wins, and the number of AI wins.
"""

import random


def printBoard(board):
	for i in range(3):
		for j in range(3):
			if j == 2:
				print(" " + board[i][j], end="")
			else:
				print(" " + board[i][j] + " |", end="")
		if i != 2:
			print("\n-––+–––+–––")
	print("\n")


# Check if a player has won the game
def win(board, player):
	for i in range(3):
		# Horizontal wins
		if board[i][0] == player and board[i][1] == player and board[i][2] == player:
			return True
		
		# Vertical wins
		if board[0][i] == player and board[1][i] == player and board[2][i] == player:
			return True
	
	# Diagonal wins
	if board[0][0] == player and board[1][1] == player and board[2][2] == player or \
			board[0][2] == player and board[1][1] == player and board[2][0] == player:
		return True
	return False


"""
    # Horizontal, vertical, and diagonal wins
    return any(
            all(board[i][j] == player for j in range(3)) or
            all(board[j][i] == player for j in range(3))
            for i in range(3)
        ) or all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))
"""

"""
# Check if a player has won the game
def win(board, player):
    # Horizontal wins
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True

    # Vertical wins
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True

    # Diagonal wins
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False
"""


# The AI is better than random now. It will check if it has a winning move and play it. 
# It will also check if the opponent has a winning move and play to block.
def AIPlayerMove(board):
	# Check if AI has any moves that result in a win
	for i in range(3):
		for j in range(3):
			if testWin(board, i, j, "O"):
				return [i, j]
	
	# Checks if opponent has any moves that result in a win
	for i in range(3):
		for j in range(3):
			if testWin(board, i, j, "X"):
				return [i, j]
	
	# If the center is open, play it
	if board[1][1] == " ":
		return [1, 1]
	
	# If there's an open corner, use it
	corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
	for c in corners:
		if board[c[0]][c[1]] == " ":
			# corners.remove(c)
			return c
	"""
	# Alternatively, choose a random one of the remaining corners (little impact)
	if len(corners) > 0:
	  return corners[random.randint(0, len(corners) - 1)]
	"""
	
	# Plays a random move (on the edge) if can't find anything else
	while True:
		row = random.randint(0, 2)
		col = random.randint(0, 2)
		if board[row][col] == " ":
			break
	return [row, col]


# See if a win is possible if the input player selects the input position
def testWin(board, testRow, testCol, player):
	# Create a new board and add the potential next move
	duplicate = []
	for row in range(3):
		line = []
		for col in range(3):
			line.append(board[row][col])
		duplicate.append(line)
	
	if duplicate[testRow][testCol] != " ":
		return False
	
	duplicate[testRow][testCol] = player
	return win(duplicate, player)


def RandomPlayerMove(board):
	while True:
		row = random.randint(0, 2)
		col = random.randint(0, 2)
		if board[row][col] == " ":
			return [row, col]


# Check if the board is full
def finished(board):
	for row in range(3):
		for col in range(3):
			if board[row][col] == ' ':
				return False
	return True


ties = 0
randomPlay = 0
computer = 0

for q in range(1000):
	# Set up a blank board each time
	board = []
	for i in range(3):
		line = []
		for j in range(3):
			line.append(' ')
		board.append(line)
	
	tie = False
	player = 'X'
	flip = random.randint(1, 2)
	if flip == 1:
		player = 'O'
	
	while True:
		if player == 'X':
			play = RandomPlayerMove(board)
			board[play[0]][play[1]] = player
		
		elif player == 'O':
			play = AIPlayerMove(board)
			board[play[0]][play[1]] = player
		
		if win(board, player):
			break
		if finished(board):
			tie = True
			break
		
		if player == 'X':
			player = 'O'
		else:
			player = 'X'
	
	if tie:
		ties += 1
	else:
		if player == 'X':
			randomPlay += 1
		else:
			computer += 1

print("TIES: " + str(ties))
print("RANDOM WINS: " + str(randomPlay))
print("COMPUTER WINS: " + str(computer))
