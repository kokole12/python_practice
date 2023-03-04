#!/usr/bin/python3
binary_search = __import__('generic_binary_search').binary_search


def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    return binary_search(0, len(cards)-1, condition)
