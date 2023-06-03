def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list): The matrix represented as a list of lists.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with all elements divided by the divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
        TypeError: If the rows of the matrix have different sizes.

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

        >>> matrix_divided([[1, 2], [3, 4], [5, 6]], 0.5)
        [[2.0, 4.0], [6.0, 8.0], [10.0, 12.0]]
    """
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
