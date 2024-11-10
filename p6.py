def print_solution(board):
    """Function to print the chessboard with queens."""
    for row in board:
        print(" ".join(row))
    print("\n")


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    n = len(board)

    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens(board, row):
    """Recursive function to solve the N-Queens problem."""
    n = len(board)
    if row >= n:  # All queens are placed
        print_solution(board)
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 'Q'  # Place queen

            # Recur to place the rest of the queens
            if solve_n_queens(board, row + 1):
                return True  # If successful, stop further processing

            board[row][col] = '.'  # Backtrack

    return False  # No place found in this row


def main():
    n = 8  # Size of the chessboard (8x8)
    board = [['.' for _ in range(n)] for _ in range(n)]  # Initialize the board

    # Get the position of the first queen from the user
    print("Enter the position of the first queen (row and column from 0 to 7):")
    row = int(input("Row (0-7): "))
    col = int(input("Column (0-7): "))

    # Validate the input
    if row < 0 or row >= n or col < 0 or col >= n:
        print("Invalid position. Please enter values between 0 and 7.")
        return

    board[row][col] = 'Q'  # Place the first queen

    # Solve the N-Queens problem starting from the next row
    if not solve_n_queens(board, row + 1):  # Start solving from row + 1
        print("No solution exists with the first queen placed at the specified position.")


if __name__ == "__main_3_":
    main()
