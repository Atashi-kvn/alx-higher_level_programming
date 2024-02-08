#!/usr/bin/python3
"""Matrix division"""


def matrix_divided(matrix, div):
    """dividing a matrix by a number
    Args:
        matrix: matrix to be divided
        div: number to divide the matrix by
    Returns:
        a new matrix with the result of the division
    Raises:
        TypeError: if matrix is not a matrix (list of lists)
                   of integers/floats
        TypeError: if each row of the matrix is not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    """divides a matrix by a number
    Args:
        matrix (list of lists): matrix to be divided
        div (int/float): number to divide the matrix by
    Returns:
        a new matrix with the result of the division
    Raises:
        TypeError: if matrix is not a matrix (list of lists)
                   of integers/floats
        TypeError: if each row of the matrix is not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    """divides a matrix by a number
    Args:
        matrix (list of lists): matrix to be divided all elements of a matrix"""
    if (matrix == [] or matrix == [[]] or type(matrix) is not list or
       not all(type(row) is list for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
