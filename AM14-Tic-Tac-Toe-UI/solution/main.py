import random
import time


def print_board(board):
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


# Simple AI algorithm - program just plays a spot randomly.
def random_player_move(board):
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board[row][column] == ' ':
            return [row, column]


# Check if the board is full
def finished(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


# Set up the board
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
    print("The coin flip shows that the computer (O) goes first!")
    player = 'O'
else:
    print("The coin flip shows that you (X) will go first!")

input("Press Enter to begin!")

while True:
    print_board(board)

    # User goes
    if player == 'X':
        # While loop to make sure user puts in valid numbers
        while True:
            row = int(input("Pick a row to play: "))
            col = int(input("Pick a column to play: "))
            if (-1 < row and row < 3) and (-1 < col and col < 3) and board[row][col] == " ":
                board[row][col] = player
                break
            print("Not a valid move, try again")

    # Computer goes
    if player == 'O':
        time.sleep(1)
        play = random_player_move(board)
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

print_board(board)
if tie:
    print("Well, there was a tie!")
else:
    if player == 'X':
        print("Wow! You won!")
    else:
        print("Well, the Random Player won.")
