#!/usr/bin/python3
def quadratic(a, b, c):
    return lambda x: a*x**2+b+c

f = quadratic(2, 3, -5)
print(f(2))
