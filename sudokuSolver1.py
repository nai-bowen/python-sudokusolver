# the grid to be solved
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def solve_sudoku(grid):
    # check if the grid is already solved
    if not find_empty_cell(grid):
        return True

    # try to fill the empty cells with valid numbers
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if is_valid_number(grid, i, j, n):
                        grid[i][j] = n
                        if solve_sudoku(grid):
                            return True
                        grid[i][j] = 0
                return False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid_number(grid, row, col, n):
    # check if the number already exists in the row
    if n in grid[row]:
        return False

    # check if the number already exists in the column
    for i in range(9):
        if grid[i][col] == n:
            return False

    # check if the number already exists in the 3x3 block
    block_row = row // 3
    block_col = col // 3
    for i in range(3):
        for j in range(3):
            if grid[block_row * 3 + i][block_col * 3 + j] == n:
                return False

    # the number is valid
    return True

# print the original grid
print("Original grid:")
for i in range(9):
    print(grid[i])

# solve the grid
solve_sudoku(grid)

# print the solved grid
print("Solved grid:")
for i in range(9):
    print(grid[i])
