#!/usr/bin/python3

max_integer = __import__('9-max_integer').max_integer

if __name__ == "__main__":

    my_list  = [1, 2, 4, 5, -1, 0, 10, -6, -8]
    max_value = max_integer(my_list)
    print('{} is the max'.format(max_value))
