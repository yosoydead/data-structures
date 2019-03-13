* What is a **priority queue**:
    - a data structure where each element has a priority
    - elements with higher priorities are served before elements with lower priorities
    - they are separate from heaps
    - can be implemented with a list or an array
* A naive version would be to use a list to store all elements as they come in. 
    - example `[priority: 3, priority: 1, priority: 2, priority: 5]`
    - when you need to remove something you would need to **iterate** over the entire list an check the item with the **highest** priority.
    - sometimes, a lower number can indicate a higher priority
* Another way to implement a priority queue is to use a **heap**.
    - imagine people are walking into a hospital with different problems
    - if there are no people waiting, a person with fever would be the first one to get help
    - if another person with a concussion walks in, that person would have a priority over the one with fever
* **!We are not storing numbers like in a binary heap**.
* Pseudocode (very similar to binary heap):
    - class named *PriorityQueue*
        - properties: *values = []*
    - class named *Node*
        - properties: *val*, *priority*
            - example of a node: `val: "pay bills", priority: 1` 
            - example of a node: `val: "walk dog", priority: 2` 
        - **the value doesn't matter**. For comparison, only the priority is used.
    - write a *MinBinaryHeap** -> lower numbers mean higher priority
    - each Node has a val and priority. Use the priority to build the heap
    - **enqueue** method that accepts a value and a priority, makes a new node and puts it in the right spot based off of its priority
    - **dequeue** method removes root element, returns it and rearranges heap using priority