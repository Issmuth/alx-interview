#!/usr/bin/python3
"""N queens problem"""
import sys

def validate_input(arguments):
    """Validate the input arguments"""
    if len(arguments) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not arguments[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(arguments[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    
    return n

def find_queen_positions(n, row=0, columns=[], diag1=[], diag2=[]):
    """Recursively find all possible positions for N queens"""
    if row < n:
        for col in range(n):
            if col not in columns and row + col not in diag1 and row - col not in diag2:
                yield from find_queen_positions(n, row + 1, columns + [col], diag1 + [row + col], diag2 + [row - col])
    else:
        yield columns

def solve_n_queens(n):
    """Solve the N queens problem and print solutions"""
    for solution in find_queen_positions(n):
        formatted_solution = [[i, col] for i, col in enumerate(solution)]
        print(formatted_solution)

if __name__ == "__main__":
    n = validate_input(sys.argv)
    solve_n_queens(n)