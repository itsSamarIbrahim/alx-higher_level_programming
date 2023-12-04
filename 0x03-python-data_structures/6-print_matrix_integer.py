#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for row in matrix:
        for column in row:
            if column != row[-1]:
                print("{:d}".format(column), end=" ")
            else:
                print("{:d}".format(column), end="\n")
