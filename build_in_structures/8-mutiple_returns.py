#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        first_char = [0]
    else:
        return None
    return(len(sentence), first_char)
