#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """Returns the perimeter of the 
    island described in grid."""
    land = 0
    for row in grid:
        for square in row:
            if square == 1:
                land += 1

    return ((land * 2) + 2)
