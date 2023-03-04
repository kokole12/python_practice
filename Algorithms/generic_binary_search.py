#!/usr/bin/python3
def binary_search(left, right, condition):
    while left <= right:
        mid = (left + right)//2
        if condition(mid) == 'found':
            return mid
        elif condition(mid) == 'left':
            left =  mid -1
        else:
            right = mid + 1
    return -1
