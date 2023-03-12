#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0,0)):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        self.__position = position

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

    def my_print(self):
        if self.size == 0:
            print()
        
        str = '#'
        for x in range(self.__size):
            print(str * self.__size)
    

    @property
    def position(self):
        return self.position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive intgers")
        
        if len([i for i in value if isinstance(i, int) and i >= 0]) !=2:
            raise TypeError("position must be a tuple of 2 positive intgers")
        self.__position = value
