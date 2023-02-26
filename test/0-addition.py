""" The fucntions for the operations
args:
	a -  first integer
	b -  second argument
Return:
	sum
	mul
"""

def add(a, b):
	return a + b

def mul(a, b):
	return a * b

import doctest
doctest.testfile('tests.txt')


