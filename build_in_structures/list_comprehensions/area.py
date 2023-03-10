#!/usr/bin/python3
import math
def area(r):
    return math.pi* r**2

radii = [2, 4, 6]

areas = []
for radius in radii:
    areas.append(area(radius))

print(areas)
