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
        pass
    
    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0