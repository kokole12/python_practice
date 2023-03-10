#!/usr/bin/python3
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)



""" using for loop"""
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transpose.append(transposed_row)

print(transpose)


""" using for loop and list comprehension combined"""

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)
