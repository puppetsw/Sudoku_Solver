"""
    File name: solver.py
    Author: Scott Whitney
    Date created: 12/10/21
    Date last modified: 12/10/21
    Python Version: 3.9.7

    Comments:
    My first attempt at a backtracking algorithm in python to 
    help solve a Sudoku grid.
"""


def issafe(grid: list[list[int]], row: int, col: int, num: int):
    """Check if it is safe to place a number in the grid.

    Args:
        grid (list[list[int]]): The Sudoku grid.
        row (int): Row number in grid.
        col (int): Column number in grid.
        num (int): Number to check placement of.

    Returns:
        bool: True if okay to place, otherwise False.
    """
    if usedinrow(grid, row, num):
        return False

    if usedincolumn(grid, col, num):
        return False

    if usedinbox(grid, row - row % 3, col - col % 3, num):
        return False

    return True


def usedinrow(grid: list[list[int]], row: int, num: int):
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False


def usedincolumn(grid: list[list[int]], col: int, num: int):
    for i in range(9):
        if grid[i][col] == num:
            return True
    return False


def usedinbox(grid: list[list[int]], row: int, col: int, num: int):
    for i in range(3):
        for j in range(3):
            if grid[i + row][j + col] == num:
                return True
    return False


def findnextemptycell(grid: list[list[int]], grid_loc: list[int]):
    """Finds the next empty cell in the Sudoku grid.

    Args:
        grid (list[list[int]]): The Sudoku grid.
        grid_loc (list[int]): The location of the grid cell, when found.

    Returns:
        bool: True if empty cell found, otherwise False.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                grid_loc[0] = row
                grid_loc[1] = col
                return True
    return False


def solve(grid: list[list[int]]):
    print('Attemping to solve...')

    emptycell = [0, 0]

    if not findnextemptycell(grid, emptycell):
        return True # no more empty cells, solved!

    row = emptycell[0]
    col = emptycell[1]

    # for numbers 1 to 9
    for num in range(1, 10):
        if issafe(grid, row, col, num):
            # try placement
            grid[row][col] = num

            if solve(grid):
                return True

            # placement wasn't safe, try again.
            grid[row][col] = 0

    return False


def printgrid(grid: list[list[int]]):
    """Prints the grid out on the screen.

    Args:
        grid (list[list[int]]): The Sudoku grid.
    """
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end='')
            print(',', end='')
        print()


def main():

    # 0 means unassigned cells
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    expected_grid = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
                     [5, 2, 9, 1, 3, 4, 7, 6, 8],
                     [4, 8, 7, 6, 2, 9, 5, 3, 1],
                     [2, 6, 3, 4, 1, 5, 9, 8, 7],
                     [9, 7, 4, 8, 6, 3, 1, 2, 5],
                     [8, 5, 1, 7, 9, 2, 6, 4, 3],
                     [1, 3, 8, 9, 4, 7, 2, 5, 6],
                     [6, 9, 2, 3, 5, 1, 8, 7, 4],
                     [7, 4, 5, 2, 8, 6, 3, 1, 9]]

    solve(grid)

    if (grid == expected_grid):
        print('Solved!')
        printgrid(grid)

    else:
        print('Solve failed!')


if __name__ == "__main__":
    main()
