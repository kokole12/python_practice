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

    def insertAtPosition(self, data, index):
        if index == 0:
            self.insertAtBeginning(data)
        
        new_node = Node(data)
        current = self.head

        while index > 1:
            current = new_node.next
            index -= 1
        prev = current
        next = current.next

    def removeAt(self, data, index):
        if index < 0 and index >= self.length_list():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head == self.head.next
            return
        
        count = 0
        current_node = self.head
        while current_node:
            if count == index - 1:
                current_node.next = current_node.next.next
            current_node = current_node.next
        
        

    def __repr__(self):
        return '<Node: %s>' %self.data
    

    def length_list(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


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
    length = ll.length_list()
    print('The length of the list is {}'.format(length))
