#!/usr/bin/python3

matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
    ]

new_matrix = [[x**2 for x in row]for row in matrix]
print(new_matrix)