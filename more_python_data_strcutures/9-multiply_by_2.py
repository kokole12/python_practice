#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for key, val in a_dictionary.items():
        return {key: val * 2}

    # return {key: val * 2 for key, val in a_dictionary.items()}


    """ Using a for loop
    """
    
