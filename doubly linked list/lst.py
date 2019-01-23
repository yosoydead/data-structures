#this will be the wrapper class to create a doubly linked list
from node import Node

class DoublyLinkedList:
    #create an empty item with some properties
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    #start adding to the beginning
    def addToStart(self,data):
        #create a new node that holds the data to be added
        new = Node(data)

        #if the list is empty, it means the new node will be
        #the head and the tail at the same time
        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            #save the value of the current head
            tempHead = self.head
            #update the value of head to be the new node
            self.head = new

            #the new head should have its next poiter point to
            #the old head
            self.head.next = tempHead
            #the prev head needs to point to the new head
            tempHead.prev = self.head
            self.count += 1

    def addToLast(self,data):
        #create a new node to hold the data to be added
        new = Node(data)

        #if the list is empty, the head and tail need to point
        #to the same value
        if self.count == 0:
            self.head = new
            self.tail =self.head
            self.count += 1
        else:
            #need to bind the current tail.next pointer to the new value
            self.tail.next = new
            #make the new pointer prev to point to the tail
            new.prev = self.tail
            #update the tail to point to the new value
            self.tail = new
            self.count += 1

    def addAtCertainIndex(self, data, index):
        new = Node(data)
        if self.count == 0:
            self.addToStart(self,data)
        elif self.count == 1 or index > self.count:
            self.addToLast(self,data)
        else:
            current = self.head
            for i in range(0, index):
                current = current.next
            new.next = current.next
            current.next = new
            new.prev = current
            self.count += 1
    
    #method that gets a certain node at an index
    def get(self, index):
        #check if index in valid
        if index < 0 or index >= self.count:
            return None

        #check if index is <= to lists length
        #there is no point in iterating through the entire list if the item
        #is at the end of it

        #if it is, start iterating from the beginning
        if index <= self.count//2:
            counter = 0
            currentNode = self.head
            while counter != index:
                currentNode = currentNode.next
                counter+=1
            return currentNode
        #if not, iterate from the end of the list
        else:
            counter = self.count-1
            currentNode = self.tail
            while index != counter:
                currentNode = currentNode.prev
                counter-=1
            return currentNode

    
    def iterateFromStart(self):
        curr = self.head

        while curr != None:
            print(curr.data)
            curr = curr.next

    def iteratefromTail(self):
        curr = self.tail

        while curr != None:
            print(curr.data)
            curr = curr.prev

    def isEmpty(self):
        return self.count == 0

    def size(self):
        return self.count

    def firstItem(self):
        return self.head
    
    def lastItem(self):
        return self.tail

    def removeFirstItem(self):
        #cant remove an item if the list is empty 
        if self.count != 0:
            if self.count == 1:
                backup = self.head
                self.head = None
                self.tail = None
                self.count -= 1
                return backup.data
            else:
                backup = self.head
                self.head = self.head.next
                self.head.prev = None
                self.count -= 1
                return backup.data
        else:
            return "Can't remove an item if the list is empty."

    def removeLastItem(self):
        #cant remove an element is the list is empty
        if self.count != 0:
            if self.count == 1:
                backup = self.head
                self.head = None
                self.tail = None
                self.count -= 1
                return backup.data
            else:
                backup = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                self.count -= 1
                return backup.data
        else:
            return "Can't remove an item if the list is empty."

    def removeAtCertainIndex(self, index):
        pass

    