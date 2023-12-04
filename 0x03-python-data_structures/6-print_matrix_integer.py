#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for column in row:
            print("{}".format(column), end=" ")
        print()
