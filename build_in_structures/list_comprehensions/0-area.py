#!/usr/bin/python3
from math import pi


def area(r):
    return pi * r**2

radii = [2, 4, 6]
print(list(map(area, radii)))
