#!/usr/bin/python3
binary_search = __import__('generic_binary_search').binary_search


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid] - 1 == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums)-1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid -1] == target:
                return "left"
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target) 