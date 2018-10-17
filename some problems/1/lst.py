from node import Node

class Lst():

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def addStudent(self):
        new = Node()

        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            self.tail.next = new
            self.tail = new
            self.count += 1
    
    def getHead(self):
        return self.head.elev.returnName()
    
    def getTail(self):
        return self.tail.elev.returnName
    
    def returnAddressOfHead(self):
        return self.head
    