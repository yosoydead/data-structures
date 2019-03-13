from node import Node

class PriorityQueue:
    def __init__(self):
        #this is the array that will store nodes
        self.values = []

    #enqueue method which takes a value and a priority
    def enqueue(self, value, priority):
        #create a new node with the two parameters
        newNode = Node(value, priority)

        #add the new node to the values array
        self.values.append(newNode)

        #use the helper
        self.bubbleUp()

    def dequeue(self):
        #the first element should have the highest priority
        mn = self.values[0]

        #remove the last element
        end = self.values.pop()

        if len(self.values) > 0:
            #now, the last element becomes the first element, but i need to check
            #if it is in the right spot
            self.values[0] = end
            self.sinkDown()

        #return the element with the highest priority
        return mn.value
    #helper method that moves elements to their correct spot based 
    #on their priority
    def bubbleUp(self):
        #get the last index
        index = len(self.values)-1

        #grab the element at the last index
        element = self.values[index]

        while index > 0:
            #get the parent index of the last element
            parentIndex = (index-1)//2

            #get the parent element of the last element
            parent = self.values[parentIndex]

            #if the elements priority is >= to the parents priority, break the loop
            if element.priority >= parent.priority:
                break
            
            #swap the element with its parent if the loop is not stopped
            self.values[parentIndex] = element
            self.values[index] = parent
            index = parentIndex

    def sinkDown(self):
        #your parent index starts at 0 (the root)
        index = 0
        length = len(self.values)
        element = self.values[0]

        #loop
        while True:
            leftChild = None
            rightChild = None
            swap = None

            #find the index of the left child: 2*index+1 (make sure its not out of bounds)
            left = 2*index+1
            if left < length:
                leftChild = self.values[left]
                if leftChild.priority < element.priority:
                    swap = left

            #find the index of the right child: 2*index+2 (make sure its not out of bounds)
            right = 2*index+2
            if right < length:
                rightChild = self.values[right]
                # If both left and right children are larger, swap with the largest child
                if (swap == None and rightChild.priority < element.priority) or (swap != None and rightChild.priority < leftChild.priority):
                    swap = right

            #keep looping and swapping until neither child is larger than the element
            #if no swaps happen, break the loop
            if swap == None:
                break
                
            self.values[index]= self.values[swap]
            self.values[swap] = element

            #update index 
            index = swap
    



    