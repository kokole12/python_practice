#!/usr/bin/python3
""" 4-main"""
nums = __import__('4-all').nums

if __name__ == "__main__":

    area1 = nums(3, 5)
    print('area = {}'.format(area1))

    print('---')

    area2 = nums(height=3, width=5)
    print('area = {}'.format(area2))
