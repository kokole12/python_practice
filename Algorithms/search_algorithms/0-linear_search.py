#!/usr/bin/python3

def linear_search(nums, target):

    for i in range(0, len(nums)):
        if i == target:
            return i
    return None
