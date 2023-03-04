#!/usr/bin/python3
class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next


class Link_list:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data, self.head)

        self.head = node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        
        last_node.next = new_node
        
    def __repr__(self):
        return 'Node: %s' %self.data
    
    def print_list(self):
        if self.head is None:
            print('empty list')
            return
        
        current_node = self.head
        lls = ''
        while current_node:
            lls += str(current_node.data) + '-->'
            current_node = current_node.next
        print(lls)

if __name__ == '__main__':
    ll = Link_list()
    ll.insertAtBeginning(4)
    ll.insertAtBeginning(7)

    ll.insertAtEnd(5)
    ll.print_list()
