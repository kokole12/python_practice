#!/usr/bin/python3
squares = [x ** 2 for x in range(10)]

print(squares)


square = []

for i in range(10):
    i = i**2

    square.append(i)

print(square)


""" Using lambda"""

squared = list((map(lambda x: x**2, range(10))))
print(squared) 