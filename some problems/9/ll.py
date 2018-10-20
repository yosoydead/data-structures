from node import Node
import time
class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self,data):
        new = Node(data)

        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head
            self.count += 1

    def removeHead(self):
        backup = self.head

        if self.count != 0:
            if self.count == 1:
                self.head = None
                self.tail = None
                self.count -= 1
            else:
                self.head = self.head.next
                self.tail.next = self.head
                self.count -= 1
        return backup.data

    def iter(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next
            time.sleep(1)

    def concat(self):
        string = ""
        cur = self.head
        
        while cur != self.tail:
            string += str(cur.data)
            cur = cur.next
        
        string += str(cur.data)
        return string