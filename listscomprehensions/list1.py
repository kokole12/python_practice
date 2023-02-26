#!/usr/bin/python3
scores = [3, 6, 9, 49]

newlist =  list(map(lambda x: x + x, scores))
print(newlist)