#!/usr/bin/python3
locate_card = __import__('1-algo').locate_card

if __name__ == '__main__':
    cards = [13, 11, 10, 7, 4, 3, 1, 0]
    query = 7
    output = 3

    result = locate_card(cards, query)
    print(result == output)
    print(result)
