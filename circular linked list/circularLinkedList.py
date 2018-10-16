from node import Node
import time
class CLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, data):
        new = Node(data)

        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head
            self.count +=1 
    
    def iter(self):
        curr = self.head
        while curr != None:
            if curr == self.head:
                print("head",curr.data)
            elif curr == self.tail:
                print("tail",curr.data)
            else:
                print(curr.data)
            curr = curr.next
            time.sleep(1)
