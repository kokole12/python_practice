#!/usr/bin/python3

"""
    The function is to print the squares of the elements in a matrix
    sample input:
        matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
"""
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x**2, row)) for row in matrix]