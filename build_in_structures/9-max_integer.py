#!/usr/bin/python3


"""
    TO find the max value in the list
    0. the first element will be the max ie max = list[0]
    1. loop through the list
    2. compare the value of max and the new value in loop
    3. if the next values are not greater than the current max then its the max

    sample input = [1, 2, 4, 5, -1, 0 10, -6, -8]

"""
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max = my_list[0]

        for i in range(0, len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
