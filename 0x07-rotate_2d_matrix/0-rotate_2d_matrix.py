#!/usr/bin/python3
"""Matrix rotation."""


def rotate_2d_matrix(matrix):
    """Rotates an nxn matrix by 90 degrees."""

    """This first loop transposes the matrix"""
    for i in range(len(matrix)):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    """
    The second loop below reverses each row of the
    transposed matrix, achieving a 90 degree rotation.
    """
    for i in range(len(matrix)):
        matrix[i].reverse()
