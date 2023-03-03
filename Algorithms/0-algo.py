#!/usr/bin/python3
from pprint import pprint
""" the brute force solution is 
    Bod can turn each card one by one until he finds the query
    steps
    1. define a variable called position
    2. initialize position to 0
    3. chech whether the index at position equals to query
    4. if yes return position and if not increament position by 1
    5. if query isnt found return -1
"""


def locate_card(cards, query):

    """ implementing the first solution"""
    position  = 0
    
    print('cards', cards)
    print('query', query)
    """ setting up a loop for repeatition"""
    while True:
    
        print('position', position)
        """check if element at the current position match query"""
        if cards[position] == query:

            """ Answer found return  and exit"""
            return position
        
        """ Increament the value for position"""
        position += 1

        """ check if we have reached the end of list cards"""
        if position == len(cards):
            """ query not found"""
            return -1
