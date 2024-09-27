#!/usr/bin/python3
"""Pascal Triangle Representaion."""


def pascal_triangle(n):
    """Returns the pascal triangle."""
    triangle = [[1], [1, 1]]

    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return triangle

    for i in range(n - 2):
        row = []
        prev = triangle[-1]
        row.append(1)
        for i in range(len(prev)):
            if i + 1 < len(prev):
                row.append(prev[i] + prev[i + 1])
        row.append(1)
        triangle.append(row)

    return triangle
