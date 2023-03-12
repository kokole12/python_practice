#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """ returns the value of size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """ sets the value for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
