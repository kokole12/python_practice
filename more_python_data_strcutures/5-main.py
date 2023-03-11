#!/usr/bin/python3

len_keys = __import__('5-len_keys').len_keys

if __name__ == "__main__":

    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = len_keys(a_dictionary)
    print("The number of keys is  {}".format(nb_keys))
