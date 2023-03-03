#!/usr/bin/env python3
""" Defining a helper function to help use test the first occurance"""
def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

"""
    Applying binary search to reduce on the search complexity of of the algorithm
    we use the following steps to tackle this
    1. find the middle Element on the list
    2. if it matches the queried value, return that as the answer
    3. if its less than the queries element, then search the first half
    4. if it is greater than the queried element then search the second half
    5. if no more elements remain, return -1
"""
def locate_card(cards, query):
    left = 0
    right = len(cards) -1

    while left <= right:
        mid = (left + right)//2

        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            right = mid - 1
        elif cards[mid] > query:
            left = mid + 1
    return -1

    # """ Using a for loop"""
    # for i in range(left, right + 1):
    #     mid = (left + right)//2

    #     cards[mid] = mid_number
    #     if mid_number == query:
    #         return mid
    #     elif mid_number < query:
    #         right = mid  + 1
    #     else:
    #         left = mid  + 1
    # return -1
