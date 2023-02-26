#!/usr/bin/python3
""" 4-all """


def nums(*args, **kwargs):
    area = 1
    if args and len(args) != 0:
        for arg in args:
            area *=arg
        return area
    elif kwargs and len(kwargs) != 0:
        for k, v in kwargs.items():
            if k == "width":
                width = v
            if k == "height":
                height = v
        return width *  height
