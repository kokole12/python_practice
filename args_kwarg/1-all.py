#!/usr/bin/python3
""" using *args argument"""


def addAll(*args):
    sum  = 0
    for arg in args:
        sum += arg
    return sum
