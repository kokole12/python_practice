#!/usr/bin/python3
locate_card = __import__('0-algo').locate_card

if __name__ == '__main__':

    import time

    start_time = time.time()
    test = {
        'input': {
            'cards': list(range(10000000, 0, -1)),
            'query': 2
        },
        'output': 9999998
    }
    end_time = time.time()
    runtime = end_time - start_time
    print('runtime: {} seconds'.format(runtime))

