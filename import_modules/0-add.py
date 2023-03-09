#!/usr/bin/python3

if __name__ == "__main__":
    """ 
        importing the add_0 module

        args:
            a = 2
            b = 3
        
        Returns:
            The value of a + b
        
        add(a, b)
    """
    from add_0 import add
    a = 2
    b = 3

    result = add(a, b)

    print('{} + {} = {}'.format(a, b, result))
