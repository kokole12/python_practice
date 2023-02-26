#!/usr/bin/python3
if __name__ == "__main__":
    from functools import reduce
    from operator import *
    scores = [2, 4, 6, 8]

    sum = reduce(lambda x, y: x + y, scores)
    sorted = reduce(lambda x, y: x if x >y else y, scores)
    opsum = reduce(add, scores)
    print(sum)
    print(sorted)
    print(opsum)