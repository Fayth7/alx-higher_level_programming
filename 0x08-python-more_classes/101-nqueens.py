#!/usr/bin/python3
"""
Solves the N-queens problem.
"""

import sys


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at position (row, col) on the board.

    Args:
        board (list): The current state of the board.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, solutions):
    """
    Recursively solves the N-queens problem.

    Args:
        board (list): The current state of the board.
        col (int): The column to place a queen.
        solutions (list): The list of valid solutions.

    Returns:
        None
    """
    if col == len(board):
        solutions.append([[i, j] for i, row in enumerate(board) for j, val in enumerate(row) if val == 1])
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[i][col] = 0


def print_solutions(n):
    """
    Prints all the solutions to the N-queens problem.

    Args:
        n (int): The size of the board.

    Returns:
        None
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_nqueens(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(n)
