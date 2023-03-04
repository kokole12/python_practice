#!/usr/bin/python3
count_rotations_linear = __import__('4-algo').count_rotations_linear

if __name__ == '__main__':
    from pprint import pprint
    tests = []
    """ a list of 10 items rotated 3 times"""
    tests.append({
        'input':{
            'nums': [10, 9, 8, 1, 2, 3, 4, 5, 6, 7]
        },
        'output': 3
    })


    """ A list of 8 rotated 5 times"""
    tests.append({
        'input':{
            'nums': [9, 8, 7, 6, 5, 1, 3, 4]
        }, 
        'output': 5
    })
    test = tests[1]
    print(count_rotations_linear(test['input']['nums'])== test['output'])
    pprint(tests)
