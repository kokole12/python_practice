#!/usr/bin/python3
def count_rotations_linear(nums):
    
    position = 1

    while position > len(nums):

        if position > 0 and nums[position] < nums[position - 1]:
            return position
        
        position += 1

    return 0
