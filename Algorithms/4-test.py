#!/usr/bin/python3
count_rotations_linear = __import__('4-algo').count_rotations_linear

if __name__ == '__main__':
    from pprint import pprint
    test = []
    """ a list of 10 items rotated 3 times"""
    test.append({
        'input':{
            'nums': [10, 9, 8, 1, 2, 3, 4, 5, 6, 7]
        },
        'output': 3
    })

    pprint(test)
