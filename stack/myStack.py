class Stk:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.count = 0

    def push(self, data):
        pass

    def pop(self):
        pass 
    
    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def peek(self):
        return self.top
