#!/usr/bin/python3

def binary_search(first, last, condition):

    while first < last:
        mid = (first + last)//2
        if condition(mid) == 'found':
            return mid
        elif condition(mid) == 'left':
            return mid - 1
        else:
            return mid + 1
    return None


def search_number(list, target):
    def condition(mid):
        if list[mid] == target:
            if mid > 0 and list[mid -1] == target:
                return 'left'
            return 'found'
        elif list[mid] < target:
            return 'left'
        else:
            return 'right'
    
    result = binary_search(0, len(list)-1, condition)
    print(result)