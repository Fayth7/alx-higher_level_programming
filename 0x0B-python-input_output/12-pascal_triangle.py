#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
