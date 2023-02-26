#!/usr/bin/python3

ls = [3,5,6,7]

def even(num):
    for n in num:
        if n %2 == 0:
            print("{:d} is even".format(n))
        print("not even")


filter(even(ls), ls)

