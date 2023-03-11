#!/usr/bin/python3

def print_sorted_dictionary(a_dictinary):

    for key in sorted(a_dictinary.keys()):
        print('{}: {}'.format(key, a_dictinary[key]))

