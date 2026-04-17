import random, time


# Creating Grid

def createGrid():
    grid = []
    for _ in range(30):
        cell = []
        for _ in range(60):
            cell.append("-")
        grid.append(cell)
    return grid


# Create basic grid
grid = createGrid()


# Printing Grid
def printGrid(grid):
    print("\033c")
    for row in grid:
        print(*row, sep="")
    time.sleep(0.5)


def findNeighbors(grid, row, col):
    liveCells = 0
    rowRetainer = colRetainer = 0
    column1 = -1
    column2 = 0
    column3 = -1
    changeRow = [row, row - 1, row + 1]
    # Checking for live cells in a single column
    while column1 < 3:
        column1 += 1
        try:
            if grid[changeRow[rowRetainer]][col - 1] == "O":
                liveCells += 1
        except IndexError:
            pass
        rowRetainer += 1
    rowRetainer = 1
    while column2 <= 2:
        column2 += 1
        try:
            if grid[changeRow[rowRetainer]][col] == "O":
                liveCells += 1
        except IndexError:
            pass
        rowRetainer += 1
    rowRetainer = 0
    while column3 < 3:
        column3 += 1
        try:
            if grid[changeRow[rowRetainer]][col + 1] == "O":
                liveCells += 1
        except IndexError:
            pass
        rowRetainer += 1
    # Changing to or keeping a live or dead cell
    if grid[row][col] == "O":
        if liveCells < 2 or liveCells >= 4:
            return "-"
        elif liveCells == 2 or liveCells == 3:
            return "O"
    else:
        if liveCells == 3:
            return "O"
        else:
            return "-"


# Creating Live Cell Locations
with open("repeat.in", "r") as f:
    z = f.readlines()
    # For every coordinate in z, we will split and get the row and column and set to "o"
    for i in range(len(z)):
        b = z[i]
        nums = b.split()
        r = int(nums[0])
        c = int(nums[1])
        grid[r][c] = "O"

    printGrid(grid)


# Preparing for Finding Neighbors
def findRow(x):
    for i in range(x, len(grid)):
        if "O" not in grid[i]:
            pass
        else:
            return (i - 1)


# Looping Finding Neighbors function
while True:
    firstRow = findRow(0)
    newGrid = [row[:] for row in grid]
    for i in range(firstRow, len(grid)):
        for j in range(60):
            newGrid[i][j] = findNeighbors(grid, i, j)
    grid = newGrid
    printGrid(grid)
