#!/usr/bin/python3
""" 3-all """


def areaAll(**kwargs):
    for k, v in kwargs.items():
        if k == "width":
            width = v
        if k == "height":
            height = v
    return width * height
