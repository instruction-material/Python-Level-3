# IMPORTANT: GIVE MORE SPACE FOR THE CONSOLE SO THE GAME CAN PROPERLY DISPLAY

import time

# Building grid of size 30x60 but that can be changed
# (Pretty important to have the y-axis be 30 so that the animation covers the entire screen on repl)
grid = []
for i in range(30):
    line = []
    for j in range(60):
        line.append(False)
    grid.append(line)

# Reading files of coordinates
f = open("repeat.in")
data = f.readlines()
f.close()

coords = []
for line in data:
    line = [int(x) for x in line.split()]
    coords.append(line)

# Setting file coordinates to be True/Alive, everything else initialized as False/Dead
for point in coords:
    grid[point[0]][point[1]] = True


# Function to print the board with O for Alive and - for Dead
def print_board(game):
    for line in game:
        for boolean in line:
            if boolean:
                print("O", end="")
            else:
                print("-", end="")
        print("")


# Function to count neighbors Alive or Dead and return result based on Conway's rules.
def neighbors(grid, alive, i, j):
    count_alive = 0
    if j - 1 >= 0 and i - 1 >= 0 and grid[i - 1][j - 1]:
        count_alive += 1
    if i - 1 >= 0 and grid[i - 1][j]:
        count_alive += 1
    if j + 1 < len(grid[0]) and i - 1 >= 0 and grid[i - 1][j + 1]:
        count_alive += 1
    if j - 1 >= 0 and grid[i][j - 1]:
        count_alive += 1
    if j + 1 < len(grid[0]) and grid[i][j + 1]:
        count_alive += 1
    if j - 1 >= 0 and i + 1 < len(grid) and grid[i + 1][j - 1]:
        count_alive += 1
    if i + 1 < len(grid) and grid[i + 1][j]:
        count_alive += 1
    if j + 1 < len(grid[0]) and i + 1 < len(grid) and grid[i + 1][j + 1]:
        count_alive += 1

    # Rule 1: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    if alive and count_alive < 2:
        return False

    # Rule 2: Any live cell with two or three live neighbours lives on to the next generation.
    elif alive and count_alive < 4:
        return True

    # Rule 3: Any live cell with more than three live neighbours dies, as if by overpopulation.
    elif alive:
        return False

    # Rule 4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    if not alive and count_alive == 3:
        return True

    # Otherwise, return original
    return alive


input(
    "Welcome to Conway's Game of Life. We start with a 30x60 grid \nof cells, either alive or dead. Here are the rules:\n\t1) Any live cell with fewer than two live neighbors \n\t   dies, as if by underpopulation.\n\t2) Any live cell with two or three live neighbors \n\t   lives on to the next generation.\n\t3) Any live cell with more than three live neighbors \n\t   dies, as if by overpopulation.\n\t4) Any dead cell with exactly three live neighbors \n\t   becomes a live cell, as if by reproduction.\nPress Enter to continue:"
)
print_board(grid)
input("Press Enter to start:")
while True:
    print("\033c")
    new_grid = []
    for i in range(30):
        line = []
        for j in range(60):
            line.append(False)
        new_grid.append(line)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i][j] = neighbors(grid, grid[i][j], i, j)

    print_board(new_grid)
    grid = new_grid

    # Pause for animation to take effect
    time.sleep(0.5)
