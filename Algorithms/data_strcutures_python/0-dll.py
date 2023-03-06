#!/usr/bin/python3
class Node:
    
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Doubly_linked_list:
    def __init__(self):
        self.head = None
    

    def insetAtBeginning(self, data):
        node = Node(data, self.head)
        node.prev = None

        if self.head is not None:
            self.head.prev = node
        
        self.head= node

    def insertAtEnd(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            node.prev = None
            return
        
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        
        last_node.next = node
        node.prev =  last_node

    def print_dll(self):
        if self.head is None:
            print('empty list')
            return
        
        current_node  = self.head
        dlls = ''
        while current_node:
            dlls += str(current_node.data) + '-->'
            current_node = current_node.next
        
        print(dlls)



dlls = Doubly_linked_list()

dlls.insetAtBeginning(3)
dlls.insetAtBeginning(4)
dlls.insetAtBeginning(10)

dlls.insertAtEnd(20)
dlls.insertAtEnd(40)
dlls.print_dll()