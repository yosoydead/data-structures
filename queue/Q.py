from node import Node

class myQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def enqueue(self, data):
        new = Node(data)
        if count == 0:
            self.first = new
            self.last = self.first
            self.count += 1
        else:
            self.last.next = new
            self.last = new
            self.count += 1
    
    def dequeue(self):
        if self.count != 0:

            if self.count == 1:
                backup = self.first
                self.first = None
                self.last = None
                self.count -= 1
                return backup
            else:
                backup = self.first
                self.first = self.first.next
                self.count -= 1
                return backup
        else:
            return "Queue is empty. Can't remove any items."
    
    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def iter(self):
        curr = self.first
        while curr != None:
            print(curr.data)
            curr = curr.next
    
    def checkFirstItem(self):
        return self.first