#!/usr/bin/python3

""" problem is to find the number of rotations in a rotated sorted list
    the complexity has to be 0(logn)

    clear problem statement is:
    write a function that takes nums as an input and determines the position
    of the smallest element since each ration take the element to a position equal to 
    the number of rotations

    steps:
    1. define the function and initialise a variable called position=1
    2. check if the value at the position is less than the predicessor
    3. if true, return the position as number of rotations
    4. else the lise has not been rotated and return 0
"""
def count_rotations_linear(nums):
    
    position = 0

    while position < len(nums):

        if position > 0 and nums[position] < nums[position - 1]:
            return position
        
        position = position + 1

    return 0
