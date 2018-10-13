#this will be the wrapper class to create a doubly linked list
from node import Node

class DoublyLinkedList:
    #create an empty item with some properties
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    #start adding to the beginning
    def addToStart(self,data):
        #create a new node that holds the data to be added
        new = Node(data)

        #if the list is empty, it means the new node will be
        #the head and the tail at the same time
        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            #save the value of the current head
            tempHead = self.head
            #update the value of head to be the new node
            self.head = new

            #the new head should have its next poiter point to
            #the old head
            self.head.next = tempHead
            #the prev head needs to point to the new head
            tempHead.prev = self.head
            self.count += 1