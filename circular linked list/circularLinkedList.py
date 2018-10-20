from node import Node
import time
class CLL:

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
        self.head.next = temp

        #increment the count element
        self.count += 1

        #if there is only one element in the list, the head and tail are the same
        if self.count == 1:
            self.tail = self.head

    def removeTheHeadItem(self):

        #you cant remove an item if the list is empty
        if self.count != 0:

            #just set the value of the head node to be equal to the value of its nextNode
            self.head = self.head.next
            self.tail.next = self.head
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
                    current = current.next
                
                #update the nextNode pointer of the second to last element to be null
                current.next = None

                #update the value of the tail pointer
                self.tail = current
            self.count -= 1

    def addToEnd(self, data):
        new = Node(data)

        if self.count == 0:
            self.head = new
            self.tail = self.head
            self.count += 1
        else:
            self.tail.next = new
            self.tail = new
            self.tail.next = self.head
            self.count +=1 
    
    def iter(self):
        curr = self.head
        while curr != None:
            if curr == self.head:
                print("head",curr.data)
            elif curr == self.tail:
                print("tail",curr.data)
            else:
                print(curr.data)
            curr = curr.next
            time.sleep(1)

    def seeHeadItem(self):
        return self.head.data
    
    def seeTailItem(self):
        return self.tail.data
        #print(self.tail.data)
    
    def size(self):
        return self.count