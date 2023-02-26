#!/usr/bin/python3
def max(list=[]):
    if len(list) == None:
        return None
    resulty = list[0]
    i = 1

    while i < len(list):
        if list[i] > resulty:
            resulty = list[i]
        i += 1
    return resulty