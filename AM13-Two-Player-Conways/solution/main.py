# Function to print the board with O for Player 1, X for Player 2, and - for Dead
def print_board(game):
    print(" ", end=" ")
    for i in range(len(game[0])):
        if i < 10:
            print(i, end=" ")
        else:
            print(i, end="")
    print()

    for x in range(len(game)):
        print(x, end=" ")
        for y in range(len(game[x])):
            # print(y, end ="")
            if game[x][y] == 1:
                print("O", end=" ")
            elif game[x][y] == 2:
                print("X", end=" ")
            else:
                print("-", end=" ")
        print()


# Function to count neighbors as O, X, or Dead and return result based on Conway's rules.
def neighbors(grid, alive, i, j):
    count_alive = 0
    xcount = 0
    ocount = 0

    # 1
    if j - 1 >= 0 and i - 1 >= 0 and grid[i - 1][j - 1] == 1:
        ocount += 1
        count_alive += 1
    elif j - 1 >= 0 and i - 1 >= 0 and grid[i - 1][j - 1] == 2:
        xcount += 1
        count_alive += 1

    # 2
    if i - 1 >= 0 and grid[i - 1][j] == 1:
        ocount += 1
        count_alive += 1
    elif i - 1 >= 0 and grid[i - 1][j] == 2:
        xcount += 1
        count_alive += 1

    # 3
    if j + 1 < len(grid[0]) and i - 1 >= 0 and grid[i - 1][j + 1] == 1:
        ocount += 1
        count_alive += 1
    elif j + 1 < len(grid[0]) and i - 1 >= 0 and grid[i - 1][j + 1] == 2:
        xcount += 1
        count_alive += 1

    # 4
    if j - 1 >= 0 and grid[i][j - 1] == 1:
        ocount += 1
        count_alive += 1
    elif j - 1 >= 0 and grid[i][j - 1] == 2:
        xcount += 1
        count_alive += 1

    # 5
    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
        ocount += 1
        count_alive += 1
    elif j + 1 < len(grid[0]) and grid[i][j + 1] == 2:
        xcount += 1
        count_alive += 1

    # 6
    if j - 1 >= 0 and i + 1 < len(grid) and grid[i + 1][j - 1] == 1:
        ocount += 1
        count_alive += 1
    elif j - 1 >= 0 and i + 1 < len(grid) and grid[i + 1][j - 1] == 2:
        xcount += 1
        count_alive += 1

    # 7
    if i + 1 < len(grid) and grid[i + 1][j] == 1:
        ocount += 1
        count_alive += 1
    elif i + 1 < len(grid) and grid[i + 1][j] == 2:
        xcount += 1
        count_alive += 1

    # 8
    if j + 1 < len(grid[0]) and i + 1 < len(grid) and grid[i + 1][j + 1] == 1:
        ocount += 1
        count_alive += 1
    if j + 1 < len(grid[0]) and i + 1 < len(grid) and grid[i + 1][j + 1] == 2:
        xcount += 1
        count_alive += 1

    # Rule 1: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    if (alive == 1 or alive == 2) and count_alive < 2:
        return 0

    # Rule 2: Any live cell with two or three live neighbours lives on to the next generation.
    elif (alive == 1 or alive == 2) and count_alive < 4:
        return alive

    # Rule 3: Any live cell with more than three live neighbours dies, as if by overpopulation.
    elif alive == 1 or alive == 2:
        return 0

    # Rule 4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    if alive == 0 and count_alive == 3:
        if xcount > ocount:
            return 2
        else:
            return 1

    # Otherwise, return original
    return alive


# Function to count the O's and X's of the grid
def count_board(grid):
    result = []
    xcounter = 0
    ocounter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                ocounter += 1
            if grid[i][j] == 2:
                xcounter += 1
    result = [ocounter, xcounter]
    return result


# Initializing board with everything dead
grid = []
for i in range(10):
    line = []
    for j in range(10):
        line.append(0)
    grid.append(line)

# Reading player1 coordinates file
f = open("player1.in")
data = f.readlines()
f.close()

start = []
for line in data:
    line = [int(x) for x in line.split()]
    start.append(line)

for point in start:
    grid[point[0]][point[1]] = 1

# Reading player2 coordinates file
f = open("player2.in")
data = f.readlines()
f.close()

start = []
for line in data:
    line = [int(x) for x in line.split()]
    start.append(line)

for point in start:
    grid[point[0]][point[1]] = 2

player_turn = True

input(
    "Welcome to Conway's 2-Player Game of Life. We start \nwith a 10x10 grid of cells, either alive or dead. \nHere are the rules:\n\t Each player starts with a square. Each turn they \nget to pick a position to grow a cell and pick a \nposition to kill an opponent cell. Each generation \npasses by following these rules:\n\t1) Any live cell with fewer than two live neighbors \n\t   dies, as if by underpopulation.\n\t2) Any live cell with two or three live neighbors \n\t   lives on to the next generation.\n\t3) Any live cell with more than three live neighbors \n\t   dies, as if by overpopulation.\n\t4) Any dead cell with exactly three live neighbors \n\t   becomes a live cell, as if by reproduction.\nPress Enter to continue:"
)
print_board(grid)
input("Press Enter to start: ")

while True:
    print()

    # Create blank grid
    new_grid = []
    for i in range(10):
        line = []
        for j in range(10):
            line.append(0)
        new_grid.append(line)

    # Iterate through one step of Conway's 4 rules
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i][j] = neighbors(grid, grid[i][j], i, j)
    print_board(new_grid)
    grid = new_grid

    score = count_board(grid)
    print("Player O has " + str(score[0]) + " cells alive")
    print("Player X has " + str(score[1]) + " cells alive")
    if score[0] == 0 or score[1] == 0:
        break

    # Player O's turn
    if player_turn:
        print("It's Player O's Turn.")
        row_add = int(
            input("Please enter the row of the cell you wish to add: ")
        )
        col_add = int(
            input("Please enter the column of the cell you wish to add: ")
        )
        row_del = int(
            input("Please enter the row of the cell you wish to delete: ")
        )
        col_del = int(
            input("Please enter the column of the cell you wish to delete: ")
        )
        grid[row_add][col_add] = 1
        grid[row_del][col_del] = 0
        player_turn = False
        print("Your new grid")
        print_board(grid)

    # Player X's turn
    else:
        print("It's Player X's Turn.")
        row_add = int(
            input("Please enter the row of the cell you wish to add: ")
        )
        col_add = int(
            input("Please enter the column of the cell you wish to add: ")
        )
        row_del = int(
            input("Please enter the row of the cell you wish to delete: ")
        )
        col_del = int(
            input("Please enter the column of the cell you wish to delete: ")
        )
        grid[row_add][col_add] = 2
        grid[row_del][col_del] = 0
        player_turn = True
        print("Your new grid")
        print_board(grid)

    score = count_board(grid)
    print("Player O has " + str(score[0]) + " cells alive")
    print("Player X has " + str(score[1]) + " cells alive")
    if score[0] == 0 or score[1] == 0:
        break

# Someone is at 0, but they could both conceivably be at 0.
if score[0] > score[1]:
    print("Player O has won the game")
elif score[1] > score[0]:
    print("Player X has won the game")
else:
    print("Both players are dead. It's a tie!")
