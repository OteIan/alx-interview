#!/usr/bin/python3
"""
Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix in place
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()
