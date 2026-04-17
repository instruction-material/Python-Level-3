"""
Improve your AI further by making it look for “forks”, which are moves that create two possible options for winning. The AI should play a move that will result in a fork when possible, as well as recognize when the human player could possibly be creating a fork.
"""

import random
import time


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
	
	# Check for a move that results in a fork
	for i in range(3):
		for j in range(3):
			if testFork(board, i, j, 'O'):
				return [i, j]
	
	# Check for a move that the opponent can play and result in a fork
	# If there are two forks however, choose to go on the offense
	loseForks = 0
	tempSet = [0, 0]
	for i in range(3):
		for j in range(3):
			if testFork(board, i, j, 'X'):
				loseForks += 1
				tempSet = [i, j]
	
	if loseForks == 1:
		return tempSet
	elif loseForks == 2:
		if board[0][1] == ' ':
			return [0, 1]
		if board[1][0] == ' ':
			return [1, 0]
		if board[1][2] == ' ':
			return [1, 2]
		if board[2][1] == ' ':
			return [2, 1]
	# return next(([i, j] for i, j in ((0, 1), (1, 0), (1, 2), (2, 1)) if board[i][j] == ' '), None)
	
	# If the center is open, play it
	if board[1][1] == " ":
		return [1, 1]
	
	# If there's an open corner, play it
	corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
	for corner in corners:
		if board[corner[0]][corner[1]] == " ":
			# corners.remove(corner)
			return corner
	
	# Plays a random move if can't find anything else
	while True:
		row = random.randint(0, 2)
		col = random.randint(0, 2)
		if board[row][col] == " ":
			break
	return [row, col]


# See if a win is possible if the input player selects the input position
def testWin(board, i, j, player):
	newBoard = duplicateBoard(board)
	if newBoard[i][j] != " ":
		return False
	newBoard[i][j] = player
	return win(newBoard, player)


# Create a deep copy of the board
def duplicateBoard(board):
	duplicate = []
	for row in range(3):
		line = []
		for col in range(3):
			line.append(board[row][col])
		duplicate.append(line)
	return duplicate


# Given a move, see if there are at least two winning moves generated from that play
def testFork(board, _row, _col, player):
	newBoard = duplicateBoard(board)
	if newBoard[_row][_col] != " ":
		return False
	
	newBoard[_row][_col] = player
	winningMoves = 0
	for row in range(3):
		for col in range(3):
			if newBoard[row][col] == " ":
				newBoard[row][col] = player
				if win(newBoard, player):
					winningMoves += 1
				newBoard[row][col] = " "
	
	if winningMoves >= 2:
		return True
	return False


# Check if the board is full
def finished(board):
	for row in range(3):
		for col in range(3):
			if board[row][col] == ' ':
				return False
	return True


"""
def finished(board):
    return not any(cell == ' ' for row in board for cell in row)
"""

# Set up the board
board = []
for i in range(3):
	line = []
	for j in range(3):
		line.append(' ')
	board.append(line)

"""
board = [[' ' for _ in range(3)] for _ in range(3)]
"""

player = 'X'
if random.randint(0, 1):
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
			if (-1 < row < 3) and (-1 < col < 3) and board[row][col] == " ":
				board[row][col] = player
				break
			print("Not a valid move, try again")
	
	# Computer goes
	elif player == 'O':
		time.sleep(1)
		play = AIPlayerMove(board)
		board[play[0]][play[1]] = player
	
	# Error state
	else:
		print("Error: Invalid player")
		break
	
	# Check if someone has won
	if win(board, player):
		printBoard(board)
		# print("Wow! You won!" if player == 'X' else "Well, the AI won.")
		if player == 'X':
			print("Wow! You won!")
		else:
			print("Well, the AI won.")
		break
	
	# Check if all game spots are taken
	if finished(board):
		printBoard(board)
		print("Well, there was a tie!")
		break
	
	# Changes turns
	player = 'O' if player == 'X' else 'X'
