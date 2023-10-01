# Backtracking Algorithm to solve Sudoku

# Size of Matrix
M = 9

# Function to print the Matrix


def printMatrix(matrix):
    for i in range(0, M):
        for j in range(0, M):
            print(matrix[i][j], end=' ')
        print("")

# Function to check if we can put a value in a particular position


def isSafe(matrix, row, col, num):

    # Check if we can put this number in this column
    for x in range(0, M):
        if (matrix[row][x] == num):
            return False

    # Check if we can put this number in this row
    for x in range(0, M):
        if (matrix[x][col] == num):
            return False

    # Check if we can put this number in this 3 x 3 matrix
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(0, 3):
        for j in range(0, 3):
            if (matrix[i + startRow][j + startCol] == num):
                return False

    return True

# Function to solve the Sudoku


def solveSudoku(matrix, row, col):

    # Check if we have reached the 8th row and 9th column (0 indexed matrix) then we are returning true to avoid further backtracking
    if (row == M - 1 and col == M):
        return True

    # Check if column value becomes 9 , we move to next row and column start from 0
    if col == M:
        row += 1
        col = 0

    # Check if the current position of the grid already contains value >0, we iterate for next column
    if matrix[row][col] > 0:
        return solveSudoku(matrix, row, col + 1)
    for num in range(1, M + 1, 1):

        # Check if it is safe to place the num (1-9)  in the given row ,col ->we move to next column
        if isSafe(matrix, row, col, num):

            # Assigning the num in the current (row,col) position of the grid and assuming our assigned num in the position is correct
            matrix[row][col] = num

            # Checking for next possibility with next column
            if solveSudoku(matrix, row, col + 1):
                return True

        # Removing the assigned num , since our assumption was wrong , and we go for next assumption with diff num value
        matrix[row][col] = 0
    return False


# Driver Code
if __name__ == "__main__":

    # Grid Matrix (# 0 means unassigned cells)
    matrix = [
        [6, 9, 0, 4, 0, 5, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 6, 0, 3],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [9, 0, 0, 0, 1, 3, 7, 5, 0],
        [0, 3, 0, 0, 0, 0, 1, 8, 0],
        [0, 6, 8, 5, 7, 0, 0, 0, 9],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [8, 0, 7, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 7, 0, 8, 0, 9, 1]
    ]

    if (solveSudoku(matrix, 0, 0)):
        printMatrix(matrix)
    else:
        print("No solution exists")
