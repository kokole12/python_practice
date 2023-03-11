#!/usr/bin/python3

print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

if __name__ == '__main__':

    a_dictionary = {'language': "C", 'Number': 13, 'track': "Low level", 'id': [1, 2, 3]}

    print_sorted_dictionary(a_dictionary)
