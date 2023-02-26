class Node:
    def __init__(self, data, next_node=None):
        self.data  = data
        self.next_node = next_node
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('Data must be integer')
        self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if (value is not None and not isinstance(value, None)):
            raise TypeError("Next node should be instance of node")
        self.__next_node = value

class SinglyLinkedlist:
    def __init__(self):
        """Initialises the singly linked list"""

        self.head = None

    def __str__(self):
        """makes the list printable"""
        printsll = ''
        location = self.head

        while location:
            printsll += str(location.data) + '\n'
            location = location.next_node
        return printsll[:-1]