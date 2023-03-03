#!/usr/bin/python3
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insertAtbeginning(self, data):
        new_node =  Node(data, self.head)
        self.head = new_node

    """ Inserting at the end of the linked list""" 
    def insertAtEnd(self, data):
        """ Declaring the node"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        
        last_node.next = new_node

    def insertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)
    
    def get_length(self):
        count = 0
        last_node = self.head
        while last_node:
            count +=1
            last_node = last_node.next
        
        return count
    

    def remove_At(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("this is not a valid index")
        if index >= 0:
            self.head = self.head.next
            return  
        

    def print(self):
        if self.head is None:
            print("empty list")
            return
        
        current_node = self.head
        lls = ''
        while current_node:
            lls += str(current_node.data) + '-->'
            current_node = current_node.next
        print(lls)


if __name__ == "__main__":
    ll = Linkedlist()
    ll.insertAtbeginning(2)
    ll.insertAtbeginning(5)

    ll.insertAtEnd(4)
    ll.insertAtEnd(6)
    ll.insertAtEnd(10)

    ll.insertValues([1, 2, 9, 20])

    length = ll.get_length()
    print("the length = {}".format(length))
    ll.print()
