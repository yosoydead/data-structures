from node import Node
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addToBeginning(self,data):
        new = Node(data)
        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            backup = self.head
            self.head = new
            self.head.next = backup
            self.count += 1
    
    def addToEnd(self,data):
        new = Node(data)
        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            self.tail.next = new
            self.tail = new
            self.count += 1

    def iter(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next