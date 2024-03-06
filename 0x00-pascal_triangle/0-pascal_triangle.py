#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """
    Implementation of pascal's triangle

    Return: list of lists of integers representing the Pascal's triangle of n
    """
    result = []

    if n <= 0:
        return result 
    
    for i in range(n):
        row = []
        for j in range(i+1):
            try:
                if i == 0 or j == 0:
                    row.append(1)
                else:
                    value = result[i-1][j-1] + result[i-1][j]
                    row.append(value)
            except IndexError:
                row.append(1)

        result.append(row)

    return result
