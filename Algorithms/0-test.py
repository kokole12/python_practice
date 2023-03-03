#!/usr/bin/python3
from pprint import pprint
""" the possible test cases for this problem
    1. query is the first element of the list
    2. query is the last element of the list
    3. query might occur somewhere in the middle of the list
    4. list cards might contain one element which is query
    5. list cards does not contain the query
    6. list cards is empty
    7. list cards contains repeating numbers
    8. query occurs in more  than one position in the list cards
"""
locate_card = __import__('0-algo').locate_card
tests = []
if __name__ == '__main__':
    
    test1 = {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7
        },
        'output': 3
    }


    tests.append(test1)

    """ Query in the middle of the cards"""
    tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
        },
        'output': 6
    })

    """ query occurs at the beginnig of the cards"""
    tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 13
        },
        'output': 0
    })

    """ Query occurs at the end of the cards"""
    tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 0
        },
        'output': 7
    })

    """ cards contain only one element"""
    tests.append({
        'input': {
            'cards': [7],
            'query': 7
        },
        'output': 0
    })

    """ cards do not contain query"""
    tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 2
        },
        'output': -1
    })

    """ cards list is empty"""
    tests.append({
        'input': {
            'cards': [],
            'query': 3
        },
        'output': -1
    })

    """ cards list contain repeating numbers"""
    tests.append({
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0],
            'query': 3
        },
        'output': 7
    })

    """ Qery occurs multiple times"""
    tests.append({
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0],
            'query': 6
        },
        'output': 2
    })

    test = tests[8]
    pprint(locate_card(**test['input']) == test['output'])
