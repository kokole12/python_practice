#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b and a < c:
        print("smallest")
    elif b > a and b < c:
        print(b)
    else:
        print(c)


import dis
dis.dis(magic_calculation)