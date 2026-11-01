# N-Queen using Backtracking
# First Queen is placed by the user


# Function to print the board
def print_board(board, n):

    # Go through each row
    for i in range(n):

        # Go through each column
        for j in range(n):

            # Print 1 for Queen and 0 for empty
            print(board[i][j], end=" ")

        # Move to next row
        print()

    print()


# Function to check whether a position is safe
def is_safe(board, row, col, n):

    # Check the same column
    for i in range(n):

        # If Queen is present in the column
        if board[i][col] == 1:
            return False


    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:

        # If Queen is found
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1


    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:

        # If Queen is found
        if board[i][j] == 1:
            return False

        i -= 1
        j += 1


    # Position is safe
    return True


# Function to solve N-Queen
def solve(board, row, n, first_row):

    # If all rows are completed
    if row == n:

        # Print the solution
        print_board(board, n)

        return True


    # Skip the row where first Queen is already placed
    if row == first_row:

        # Move to next row
        return solve(board, row + 1, n, first_row)


    # Try every column
    for col in range(n):

        # Check whether position is safe
        if is_safe(board, row, col, n):

            # Place Queen
            board[row][col] = 1

            # Solve next row
            if solve(board, row + 1, n, first_row):
                return True

            # Remove Queen if solution fails
            board[row][col] = 0


    # No position found
    return False


# Main program

# Take number of Queens
n = int(input("Enter number of queens: "))

# Create empty board
board = [[0 for _ in range(n)] for _ in range(n)]


# Take first Queen's row
first_row = int(input("Enter row of first Queen (1 to N): ")) - 1

# Take first Queen's column
first_col = int(input("Enter column of first Queen (1 to N): ")) - 1


# Check whether position is valid
if first_row < 0 or first_row >= n or first_col < 0 or first_col >= n:

    # Invalid position
    print("Invalid position!")

else:

    # Place first Queen
    board[first_row][first_col] = 1

    # Display initial board
    print("\nInitial Board:")
    print_board(board, n)

    # Solve remaining Queens
    print("Final N-Queen Solution:")

    if not solve(board, 0, n, first_row):

        # If no solution exists
        print("No solution exists!")
    
'''
1. What is the N-Queens problem?  
Place N Queens on an N×N chessboard so that no two Queens attack each other.

2. Which technique is used in N-Queens?  
Backtracking.

11. Why do we use recursion?  
To place Queens row by row and go back when a solution fails.

20.What is the time complexity?  
Approximately O(N!).
x
21. What is the space complexity?  
O(N²) for the board and O(N) for recursion stack.

22. Why is the time complexity high?  
Because the algorithm tries many possible Queen positions using backtracking28. What is the main advantage of backtracking?  
It avoids continuing with an invalid partial solution.

29. What is the difference between brute force and backtracking?  
Brute force tries all possibilities, while backtracking rejects invalid possibilities early.

30. Give one real use of backtracking.  
N-Queens, Sudoku, maze solving, and graph coloring.Disadvantages of N-Queens using Backtracking

disadv
1. High time complexity – approximately O(N!).
2. Slow for large N because many possibilities are checked.
3. Uses recursion, so it requires extra stack memory.
4. Can take a long time when searching for all possible solutions.

A state space tree is a tree that represents all possible states/choices of a problem 
from the initial state to the final solution.
'''
