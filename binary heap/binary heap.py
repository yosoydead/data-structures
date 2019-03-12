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




heap = MaxBinaryHeap()
heap.insert(55)
heap.insert(1)
heap.insert(45)
heap.insert(199)
print(heap.values)


        