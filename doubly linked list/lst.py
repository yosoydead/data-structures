#this will be the wrapper class to create a doubly linked list
from node import Node

class DoublyLinkedList:
    #create an empty item with some properties
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None
