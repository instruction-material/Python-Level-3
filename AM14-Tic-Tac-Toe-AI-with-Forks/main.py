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

    # If the center is open, play it
    if board[1][1] == " ":
        return [1, 1]

    # If there's an open corner, play it
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
    for c in corners:
        if board[c[0]][c[1]] == " ":
            # corners.remove(c)
            return c

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
    for a in range(3):
        line = []
        for b in range(3):
            line.append(board[a][b])
        duplicate.append(line)
    return duplicate


# Given a move, see if there are at least two winning moves generated from that play
def testFork(board, i, j, player):
    newBoard = duplicateBoard(board)
    if newBoard[i][j] != " ":
        return False

    newBoard[i][j] = player
    winningMoves = 0
    for a in range(3):
        for b in range(3):
            if newBoard[a][b] == " ":
                newBoard[a][b] = player
                if win(newBoard, player):
                    winningMoves += 1
                newBoard[a][b] = " "

    if winningMoves >= 2:
        return True
    return False


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
    printBoard(board)

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
