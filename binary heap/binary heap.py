class MaxBinaryHeap:
    #the max binary heap can he stored inside an array
    #using some math tricks and array index manipulation
    #so, when the constructor is called, we just initialize an empty array
    def __init__(self):
        #a little test array to help me see if this works
        #this array should be empty otherwise
        self.values = [41,39,33,18,27,12]

    #insert method
    def insert(self, element):
        #just push the element at the end of the values array
        self.values.append(element)

        #after you insert the element, use the bubble up method
        self.bubbleUp()

    #the first thing this method does is to grab the last item that was added to values
    #after that, the task of this method is to check whether if the PARENT "node" of that element
    #is less than it; it it is less, swap them and repeat the process
    def bubbleUp(self):
        index = len(self.values)-1

        #store the value of the element from the end of values
        element =  self.values[index]

        while index > 0:
            #find the index of the parent
            parentIndex = (index-1)//2

            #compare the last item added to its parent
            parent = self.values[parentIndex]
            if element <= parent:
                break
            
            #swap values
            self.values[parentIndex] = element
            self.values[index] = parent

            #update index to be parentIndex
            index = parentIndex

    def extractMax(self):
        #swap the first value in the values property with the last one
        #the max value should be the first element in an array
        mx = self.values[0]
        #pop from the values property, so you can return the value at the end
        end = self.values.pop()

        #run this code if the array is not empty
        if len(self.values) > 0:
            self.values[0] = end
            self.sinkDown()
        #return the max
        return mx

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
                if leftChild > element:
                    swap = left

            #find the index of the right child: 2*index+2 (make sure its not out of bounds)
            right = 2*index+2
            if right < length:
                rightChild = self.values[right]
                # If both left and right children are larger, swap with the largest child
                if (swap == None and rightChild > element) or (swap != None and rightChild > leftChild):
                    swap = right

            #keep looping and swapping until neither child is larger than the element
            #if no swaps happen, break the loop
            if swap == None:
                break
                
            self.values[index]= self.values[swap]
            self.values[swap] = element

            #update index 
            index = swap




heap = MaxBinaryHeap()
heap.insert(55)
heap.insert(1)
heap.insert(45)
heap.insert(199)

print(heap.values)
print(heap.extractMax())
print(heap.values)