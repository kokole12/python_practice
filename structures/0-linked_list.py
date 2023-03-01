#!/usr/bin/python3
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insertAtbeginning(self, data):
        node  = Node(data, self.head)
        self.head = node
    
    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)


    def print(self):
        if self.head is None:
            print("empty list")
            return
        
        itr = self.head
        lls = ''
        while itr:
            lls += str(itr.data) + '-->'
            itr = itr.next
        print(lls)


if __name__ == "__main__":
    ll = Linkedlist()
    ll.insertAtbeginning(2)
    ll.insertAtbeginning(5)

    ll.insertAtEnd(4)
    ll.insertAtEnd(6)
    ll.insertAtEnd(10)
    ll.print()
