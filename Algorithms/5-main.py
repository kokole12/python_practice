#!/usr/bin/python3
count_rotations_binary = __import__('5-algo').count_rotations_binary

if __name__ == '__main__':

    nums = [8, 9, 10, 1, 2, 3, 4, 6, 7]

    result = count_rotations_binary(nums)
    print(result)
