#!/usr/bin/python3
"""
    1. assign variables left and right to the list
    2. determine the middle element of the list
    3. if the middle element is not equal to the smallest element in the list
    4. search to the left and chech if the first element is less than the middle element
    5. else search to the right and check if the last element is greater
    6. the smallest elements position determines the number of rotations of the list 


    [3, 4, 5, 1, 2]
"""

def count_rotations_binary(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right)//2
        mid_number = nums[mid]

        if mid > 0 and mid_number < nums[mid]:
            return mid
        elif mid_number > nums[mid + 1]:
            left = mid - 1
        else:
            right = mid - 1
    return -1
