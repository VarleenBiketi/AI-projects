#
# Sudoku solver
# CS 131 - Artificial Intelligence
#
# Varleen Biketi
# 3/27/2024

class SudokuSolver:
    def solve(self, board):
        # Solves the Sudoku puzzle using a Constraint Satisfaction Problems approach.
        if not self.is_valid_board(board):
            print("Invalid Sudoku board")
            return None

        print("Initial Sudoku puzzle:")
        self.print_board(board)

        if self.solve_sudoku(board):
            return board
        else:
            print("No solution exists")
            return None

    def is_valid_board(self, board):
        # Checks if the Sudoku board is valid.
        if len(board) != 9 or any(len(row) != 9 for row in board):
            return False
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0 and not self.is_valid_move(board, i, j, board[i][j]):
                    return False
        return True

    def is_valid_move(self, board, row, col, num):
        # Checks if a move is valid.
        for i in range(9):
            if board[row][i] == num and i != col:
                return False
            if board[i][col] == num and i != row:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num and (3 * (row // 3) + i // 3 != row or 3 * (col // 3) + i % 3 != col):
                return False
        return True

    def solve_sudoku(self, board):
        # Backtracking algorithm to solve the Sudoku puzzle.
        empty_cell = self.find_empty_cell(board)
        if not empty_cell:
            return True
        row, col = empty_cell

        for num in range(1, 10):
            if self.is_valid_move(board, row, col, num):
                board[row][col] = num
                print(f"\nStep {row * 9 + col + 1}: Placing {num} at ({row}, {col})")
                self.print_board(board)
                if self.solve_sudoku(board):
                    return True
                board[row][col] = 0
        return False

    def find_empty_cell(self, board):
        # Finds the next empty cell in the Sudoku grid.
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def print_board(self, board):
        # Prints the Sudoku board.
        for row in board:
            print(" ".join(str(num) if num != 0 else "_" for num in row))
        print()


# Input Sudoku puzzles
puzzle1 = [
    [6, 0, 8, 7, 0, 2, 1, 0, 0],
    [4, 0, 0, 0, 1, 0, 0, 0, 2],
    [0, 2, 5, 4, 0, 0, 0, 0, 0],
    [7, 0, 1, 0, 8, 0, 4, 0, 5],
    [0, 8, 0, 0, 0, 0, 0, 7, 0],
    [5, 0, 9, 0, 6, 0, 3, 0, 1],
    [0, 0, 0, 0, 0, 6, 7, 5, 0],
    [2, 0, 0, 0, 9, 0, 0, 0, 8],
    [0, 0, 6, 8, 0, 5, 2, 0, 3]
]

puzzle2 = [
    [0, 7, 0, 0, 4, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 6, 1, 0],
    [3, 9, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 4, 0, 0, 9],
    [0, 0, 3, 0, 0, 0, 7, 0, 0],
    [5, 0, 0, 1, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 7, 6],
    [0, 5, 4, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 1, 0, 0, 5, 0]
]

print("Sudoku Puzzle 1:")
SudokuSolver().print_board(puzzle1)
print("\nSudoku Puzzle 2:")
SudokuSolver().print_board(puzzle2)

# Ask user which puzzle to solve
choice = input("\nEnter the number of the Sudoku puzzle you wish to solve (1 or 2): ")

if choice == "1":
    print("\nSolving Sudoku Puzzle 1:")
    solution = SudokuSolver().solve(puzzle1)
elif choice == "2":
    print("\nSolving Sudoku Puzzle 2:")
    solution = SudokuSolver().solve(puzzle2)
else:
    print("Invalid choice! Please enter either '1' or '2'.")

# Print solution if found
if solution:
    print("\nSolution:")
    SudokuSolver().print_board(solution)
    print("Thank you!")

