#!/usr/bin/python3

'''Defines a pascal's Traingle function '''


def pascal_triangle(n):
    """ The pascals triangle with size n
    Returns a list of intagers from the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(1)
            triangle.append(tmp)
    return triangles
