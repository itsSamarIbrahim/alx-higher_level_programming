#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
    matrix (list of lists): The input matrix, where each inner list represents a row.
    div (int or float): The divisor to divide the matrix elements by.

    Returns:
    list of lists: A new matrix with each element divided by the divisor,
    rounded to 2 decimal places.

    Raises:
    TypeError: If the input matrix is not a valid matrix (list of lists)
    of integers/floats, or if the divisor is not a number.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    for row in matrix:
        if row_length is None:
            row_length = len(row)
        elif row_length != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(elem / div, 2) for elem in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
