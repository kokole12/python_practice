#!/usr/bin/python3
multiple_returns = __import__('8-mutiple_returns').multiple_returns

if __name__ =="__main__":
    sentence = "At school, I learnt C"

    length, first = multiple_returns(sentence)

    print('Length: {:d} - First letter: {}'.format(length, first))
