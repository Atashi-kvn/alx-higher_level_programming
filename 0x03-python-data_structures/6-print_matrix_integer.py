#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for j in range(len(matrix[x])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[x][j]), end='')
        print()
