# N-Queen using Backtracking
# First Queen is already placed

def print_board(board, n):
    # Print the N x N board
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()


def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # All Queens are placed
    if row == n:
        print_board(board, n)
        return True

    found = False

    # Try every column
    for col in range(n):

        # Check whether position is safe
        if is_safe(board, row, col, n):

            board[row][col] = 1       # Place Queen

            # Place Queen in next row
            if solve_n_queens(board, row + 1, n):
                found = True

            board[row][col] = 0       # Backtrack

    return found


# Main program
n = int(input("Enter number of queens: "))

# Create N x N matrix
board = [[0 for _ in range(n)] for _ in range(n)]

# First Queen is placed in first row
col = int(input("Enter column of first Queen (1 to N): ")) - 1
board[0][col] = 1

print("\nInitial Board:")
print_board(board, n)

print("Final N-Queen Solutions:")

# Start placing remaining Queens from second row
if not solve_n_queens(board, 1, n):
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
'''
