"""
Create a one-player Tic Tac Toe game. The program should first randomly select whether the human player or the computer player gets to go first. Every time that someone takes a turn, be sure to update the grid afterwards. Your game should be able to determine when somebody wins or when there is a tie. In this project, the computer player should simply choose a random location among the ones that are remaining.
"""

import random
import time


BOARD_SIZE = 3
TOP = 0
MID = 1
BOTTOM = 2
LEFT = 0
RIGHT = 2


def printBoard(board):
	for row in range(BOARD_SIZE):
		for col in range(BOARD_SIZE):
			if col == RIGHT:
				print(" " + board[row][col], end="")
			else:
				print(" " + board[row][col] + " |", end="")
		if row != RIGHT:
			print("\n-––+–––+–––")
	print("\n")


# Check if a player has won the game
def win(board, player):
	for i in range(BOARD_SIZE):
		# Horizontal wins
		if board[i][LEFT] == player and board[i][MID] == player and board[i][RIGHT] == player:
			return True
		
		# Vertical wins
		if board[TOP][i] == player and board[MID][i] == player and board[BOTTOM][i] == player:
			return True
	
	# Diagonal wins
	return board[TOP][LEFT] == player and board[MID][MID] == player and board[BOTTOM][RIGHT] == player or \
		board[TOP][RIGHT] == player and board[MID][MID] == player and board[BOTTOM][LEFT] == player


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


# Simple AI algorithm - program just plays a spot randomly.
def randomPlayerMove(board):
	while True:
		row = random.randint(TOP, BOTTOM)
		column = random.randint(LEFT, RIGHT)
		if board[row][column] == ' ':
			return [row, column]


# return random.choice([(row, column) for row in range(TOP, BOARD_SIZE) for column in range(LEFT, BOARD_SIZE) if board[row][column] == ' '])


# Check if the board is full
def finished(board):  # return all(cell != ' ' for row in board for cell in row)
	for row in range(BOARD_SIZE):
		for col in range(BOARD_SIZE):
			if board[row][col] == ' ':
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
			if (-1 < row < BOARD_SIZE) and (-1 < col < BOARD_SIZE) and board[row][col] == " ":
				board[row][col] = player
				break
			print("Not a valid move, try again")
	
	# Computer goes
	elif player == 'O':
		time.sleep(1)
		play = randomPlayerMove(board)
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
		print("Well, the Random Player won.")
