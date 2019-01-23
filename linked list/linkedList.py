from node import Node

class MyLinkedList:

    #this is the constructor for the list
    #it has both a head and a tail pointer so the operations are done easier
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    #add the specified value to the start of the linked list
    def addAtTheStartOfTheList(self, valueToAdd):
        #first off, create a new node that holds the value you want to be stored
        newNode = Node(valueToAdd)

        #store the value of the head so it doesn't get lost down the road
        temp = self.head

        #now, update the value of the head with the created new node
        #it holds the value you want to store and a pointer to the next value which is null currently
        self.head = newNode

        #update the null pointer with the value of the previous head that is stored
        #in the temp variable
        self.head.nextNode = temp

        #increment the count element
        self.count += 1

        #if there is only one element in the list, the head and tail are the same
        if self.count == 1:
            self.tail = self.head

    def addAtTheEndOfTheList(self, valueToAdd):
        #create a node that holds the value to be stored
        newNode = Node(valueToAdd)

        #if the list is empty, it needs to have a value in the head
        #the list cannot start with a null value because it can't iterate over the other elements
        if self.count == 0:
            self.head = newNode
        else:
            #if there is an item in the head, chain the new node to the other nodes
            self.tail.nextNode = newNode
        
        self.tail = newNode
        self.count += 1
        
    #this method gets the value at the specified index
    def get(self, index):
        if index < 0 or index >= self.count:
            return None
        
        count = 0
        currentNode = self.head

        while count != index:
            count+=1
            currentNode = currentNode.nextNode
        
        return currentNode

    #this method will insert a new node at the specified index
    def insert(self, index, data):
        #if the index is less than 0 or > to the length of the list
        #return false because you can't add a node at an invalid index
        if index < 0 or index > self.count:
            return False

        #if the index is == to the length of the list, use the defined
        #insert at the end method
        if index == self.count:
            self.addAtTheEndOfTheList(data)
            return True
        
        #if index is 0, use the add to beginning method
        if index == 0:
            self.addAtTheStartOfTheList(data)
            return True
        
        #if anything above is true, use the get method to get the node
        #BEFORE the specified index because you want to add a new node
        #at the specified index in the params
        previousNode = self.get(index-1)

        #store the next node of the previousNode so you don't lose the chain
        #when updating previousNode.next = newNode
        temp = previousNode.nextNode

        #create the new node
        newNode = Node(data)

        #link the newNode with the previousNode
        previousNode.nextNode = newNode

        #link the rest of the list to the newNode
        newNode.nextNode = temp

        #update the length of the list
        self.count += 1

        #return true so you know something happened
        return True

    def iterateThroughTheList(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data)
            currentNode = currentNode.nextNode

    #this method removes a node at a specified index
    def removeAtIndex(self, index):
        #if the index is < or > the lists length, return false
        if index < 0 or index >= self.count:
            return False

        #if index is == to the list length -1, use the removeTail function
        if index == self.count-1:
            self.removeTheTailItem()
            return True
        
        #if index is == 0, use the removeHead function
        if index == 0:
            self.removeTheHeadItem()
            return True

        #if nothing from above is true

        #get the node at index-1
        prevNode = self.get(index-1)

        #store the removed node which should be the next node
        #of the stored prevNode
        removedNode = prevNode.nextNode

        #the next node of prevNode should be the next node of removedNode
        prevNode.nextNode = removedNode.nextNode

        #return that removed node
        return removedNode

    def removeTheHeadItem(self):

        #you cant remove an item if the list is empty
        if self.count != 0:

            #just set the value of the head node to be equal to the value of its nextNode
            self.head = self.head.nextNode
            self.count -= 1

            if self.count == 0:
                self.tail = None
    
    def removeTheTailItem(self):
        #you can remove an item if only there is an item to be removed xD
        if self.count != 0:

            #if the list has only one item, just remove the head and tail reference from the node
            if self.count == 1:
                self.head = None
                self.tail = None
            else:
                #in order to find the second to last item in the list, we need to iterate through all the list
                #we start at the head of the list
                current = self.head

                #while the value of the current node seen is not = to tail, move through the list
                #it stops as the second to last item because the nextNode value would be the value of the tail node
                while current.nextNode != self.tail:
                    current = current.nextNode
                
                #update the nextNode pointer of the second to last element to be null
                current.nextNode = None

                #update the value of the tail pointer
                self.tail = current
            self.count -= 1

    def seeHeadItem(self):
        return self.head.data
    
    def seeTailItem(self):
        return self.tail.data
        #print(self.tail.data)
    
    #this method will accept an index and a value as arguments
    #it will update the value of the item at a certain index to the value passed
    def set(self, index, value):
        #first, get the value at the specified index
        #use the already defined get method
        foundNode = self.get(index)

        #if the node is found, update its value
        #return true so you know something updated
        if foundNode:
            foundNode.data = value
            return True

        #if the node is not found, return false
        return False

    def size(self):
        return self.count
    

    