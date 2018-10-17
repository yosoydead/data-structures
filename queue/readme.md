A queue is an ordered collection of items where the addition of new items happens at one end, called the "rear",
    and the removal of existing items occurs at the other end, commonly called the "front". 
    As an element enters the queue it starts at the rear and makes its way towards the front,
    waiting until that time when it is the next element to be removed.
This ordering principle is called FIFO -> first in first out.  
The queue operations are given below:  
    queue() -> create a new queue that is empty. It needs no params and returns an empty queue  
    enqueue(item) -> adds a new item to the rear of the queue. It needs the item and returns nothing  
    dequeue() -> removes the front item from the queue. It needs no params and returns the item. The queue is modified  
    isEmpty() -> tests to see whether the queue is empty. It needs no params and returns a bool  
    size() -> returns the number of items in the queue. It needs no params and returns an int  
I will use the internal list in python first. I'll implement the linked list version later.

Implementations:
1. [x] with the predefined list in python.  
2. [x] using a singly linked list. Methods:
    1. 1) [x] queue()  
    2. 2) [x] enqueue()  
    3. 3) [x] dequeue()  
    4. 4) [x] isEmpty()  
    5. 5) [x] size()  
    6. 6) [x] iter()
    7. 7) [x] check the first item
    8. 8) [x] check the last item