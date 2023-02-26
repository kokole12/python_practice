#!/usr/bin/python3
import sys

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print("input: {}".format(line))

print('Exit')
