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


# The AI is better than random now. It will check if it has a winning move and play it.
# It will also check if the opponent has a winning move and play to block.
def ai_player_move(board):
    # Check if AI has any moves that result in a win
    for i in range(3):
        for j in range(3):
            if test_win(board, i, j, "O"):
                return [i, j]

    # Checks if opponent has any moves that result in a win
    for i in range(3):
        for j in range(3):
            if test_win(board, i, j, "X"):
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
def test_win(board, i, j, player):
    # Create a new board and add the potential next move
    duplicate = []
    for a in range(3):
        line = []
        for b in range(3):
            line.append(board[a][b])
        duplicate.append(line)

    if duplicate[i][j] != " ":
        return False

    duplicate[i][j] = player
    return win(duplicate, player)


# Check if the board is full
def finished(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


# Set up the board
board = []
for i in range(3):
    line = []
    for j in range(3):
        line.append(" ")
    board.append(line)

tie = False
player = "X"
flip = random.randint(1, 2)
if flip == 1:
    print("The coin flip shows that the computer (O) goes first!")
    player = "O"
else:
    print("The coin flip shows that you (X) will go first!")

input("Press Enter to begin!")

while True:
    print_board(board)

    # User goes
    if player == "X":
        # While loop to make sure user puts in valid numbers
        while True:
            row = int(input("Pick a row to play: "))
            col = int(input("Pick a column to play: "))
            if (
                (-1 < row and row < 3)
                and (-1 < col and col < 3)
                and board[row][col] == " "
            ):
                board[row][col] = player
                break
            print("Not a valid move, try again")

    # Computer goes
    if player == "O":
        time.sleep(1)
        play = ai_player_move(board)
        board[play[0]][play[1]] = player

    # Check if someone has won
    if win(board, player):
        break
    # Check if all game spots are taken
    if finished(board):
        tie = True
        break

    # Changes turns
    if player == "X":
        player = "O"
    else:
        player = "X"

print_board(board)
if tie:
    print("Well, there was a tie!")
else:
    if player == "X":
        print("Wow! You won!")
    else:
        print("Well, the AI won.")
