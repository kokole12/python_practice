#!/usr/bin/python3

Square = __import__('2-square').Square

try:
    my_square = Square(2)
    print(type(my_square))
    print(my_square.__dict__)
    print(my_square.size)
except Exception as e:
    print(e)

try:
    my_square = Square("2")
    print(my_square.size)
except Exception as e:
    print(e)


try:
    my_square = Square(-2)
    print(my_square.size)
except Exception as e:
    print(e)
