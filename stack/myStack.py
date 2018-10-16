from node import Node
class Stk:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.count = 0

    def push(self, data):
        new = Node(data)
        #if the stack is empty, the bottom and the top of the stack point to the same value
        if self.count == 0:
            self.bottom = new
            self.top = self.bottom
            self.count += 1
        #if not, first make the next pointer of the top item to point to the same value,
        #then make so that the value top points to the new node created
        else:
            self.top.next = new
            self.top = new
            self.count += 1

    def pop(self):
        #using a singly linked list, i have to iterate until the second to last item in the stack
        #meaning the item before the top item, and then, delete the top item by making the second to last element
        #to be the top item
        if self.count != 0:
            if self.count == 1:
                backup = self.top
                self.top = None
                self.bottom = None
                self.count -= 1
                return backup.data
            else:
                backup = self.top
                curr = self.bottom
                while curr.next != self.top:
                    curr = curr.next
                
                #now i got the element before the top element
                #all i need to do is to make its next pointer to be NULL and all refs to the top element are deleted
                curr.next = None
                self.top = curr
                self.count -= 1
                return backup.data
        else:
            return "The stack is empty"


    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def peek(self):
        return self.top.data

    def iter(self):
        curr = self.bottom
        while curr != None:
            print(curr.data)
            curr = curr.next
