#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """Returns the perimeter of the
    island described in grid."""
    w = len(grid[0])
    h = len(grid)
    edges = 0
    span = 0

    for row in range(h):
        for square in range(w):
            if grid[row][square] == 1:
                span += 1
                if (square > 0 and grid[row][square - 1] == 1):
                    edges += 1
                if (row > 0 and grid[row - 1][square] == 1):
                    edges += 1

    return span * 4 - edges * 2
