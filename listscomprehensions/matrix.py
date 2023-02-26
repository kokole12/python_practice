#!/usr/bin/python3
if __name__ == "__main__":
    from functools import reduce
    from operator import *
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
        ]

    newlist = [list(map(lambda x: x**2, row)) for row in matrix]
    sumMatrix = reduce(add, matrix)
    print(newlist)
    print(sumMatrix)