#!/usr/bin/python3
""" 1-main """

addAll = __import__('1-all').addAll

if __name__ == "__main__":

    rs = addAll(3, 5, 6, 8)
    print('the sum of args = {}'.format(rs))
