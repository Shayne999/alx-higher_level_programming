#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(10):
        for j in range(len(matrix[i])):
            if j == 9:
                print(matrix[i][j], end="")
            else:
                print("{:d}".format(matrix[i][j]), end=", ")
