from node import Node
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self,data):
        new = Node(data)
        if self.count > 5:
            #print("cant add anymore")
            return
        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            self.tail.next = new
            self.tail = new
            self.count += 1

    def concatinate(self):
        string = ""
        cur = self.head
        while cur != None:
            string += str(cur.data)
            cur = cur.next

        if string[0] == 0:
            return string[1:]
        else:
            return string