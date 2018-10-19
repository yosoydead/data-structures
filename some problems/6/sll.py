from node import Node
import random
class SLL:
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
            self.count += 1

    def populate(self, numbers):
        for i in range(0, numbers):
            n = random.randint(1,150)
            self.add(n)
    
    def iter(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next