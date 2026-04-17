"""
Improve the strategy used by your computer player in the previous project by making it “think” rationally. Some things that your AI player should look out for are moves that would cause it to win, moves that would block the human player from immediately winning, and optimal board locations (the center is one of the most advantageous, followed by the corners).
"""

import random
import time


BOARD_SIZE = 3


def printBoard(board):
	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
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
	for row in range(BOARD_SIZE):
		for col in range(BOARD_SIZE):
			if testWin(board, row, col, "O"):
				return [row, col]
	
	# Checks if opponent has any moves that result in a win
	for row in range(BOARD_SIZE):
		for col in range(BOARD_SIZE):
			if testWin(board, row, col, "X"):
				return [row, col]
	
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
	# Alternatively, choose a random remaining corner (little impact on performance)
	if len(corners) > 0:
	  return corners[random.randint(0, len(corners) - 1)]
	"""
	
	# Plays a random move if can't find anything else
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
	for row in range(BOARD_SIZE):
		line = []
		for col in range(BOARD_SIZE):
			line.append(board[row][col])
		duplicate.append(line)
	
	if duplicate[testRow][testCol] != " ":
		return False
	
	duplicate[testRow][testCol] = player
	return win(duplicate, player)


# Check if the board is full
def finished(board):
	for i in range(BOARD_SIZE):
		for j in range(BOARD_SIZE):
			if board[i][j] == ' ':
				return False
	return True


# Set up the board
board = []  # board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
for _ in range(BOARD_SIZE):
	board.append([' ' for _ in range(BOARD_SIZE)])
"""
for _ in range(BOARD_SIZE):
    line = []
    for _ in range(BOARD_SIZE):
        line.append(' ')
    board.append(line)
"""

tie = False
player = 'X'
flip = random.randint(1, 2)
if flip == 1:
	print("The coin flip shows that the computer (O) goes first!")
	player = 'O'
else:
	print("The coin flip shows that you (X) will go first!")

input("Press Enter to begin!")

while True:
	printBoard(board)
	
	# User goes
	if player == 'X':
		# While loop to make sure user puts in valid numbers
		while True:
			row = int(input("Pick a row to play: "))
			col = int(input("Pick a column to play: "))
			if (-1 < row < BOARD_SIZE) and (-1 < col < BOARD_SIZE) and board[row][col] == " ":
				board[row][col] = player
				break
			print("Not a valid move, try again")
	
	# Computer goes
	elif player == 'O':
		time.sleep(1)
		play = AIPlayerMove(board)
		board[play[0]][play[1]] = player
	
	# Check if someone has won
	if win(board, player):
		break
	# Check if all game spots are taken
	if finished(board):
		tie = True
		break
	
	# Changes turns
	if player == 'X':
		player = 'O'
	else:
		player = 'X'

printBoard(board)
if tie:
	print("Well, there was a tie!")
else:
	if player == 'X':
		print("Wow! You won!")
	else:
		print("Well, the AI won.")
