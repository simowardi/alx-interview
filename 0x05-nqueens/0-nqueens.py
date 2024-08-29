#!/usr/bin/python3
"""
Solves the N-queens puzzle
Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N-queens puzzle and return the solutions
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        """
        Recursive function to solve N-queens using backtracking
        """
        if col == n:
            # Found a solution, add it to the list
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return True

        for i in range(n):
            if is_safe(board, i, col, n):
                # Place the queen
                board[i][col] = 1
                # Recur to place rest of the queens
                solve(col + 1)
                # Backtrack
                board[i][col] = 0

    # Start solving from the first column
    solve(0)
    return solutions


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a valid integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the puzzle and print solutions
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)
