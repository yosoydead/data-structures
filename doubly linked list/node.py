#the basic building block for a singly/doubly linked list
#the only difference is that a doubly linked list needs a new pointer for the previous value
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None