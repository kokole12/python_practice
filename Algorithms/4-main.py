#!/usr/bin/python3
count_rotations_linear = __import__('4-algo').count_rotations_linear

if __name__ == '__main__':

    nums = [10, 9, 8, 1, 2, 3, 4, 5, 6, 7]

    result = count_rotations_linear(nums)
    print(result)
