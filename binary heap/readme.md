* What is a Binary Heap?
    - **very** similar to a binary search tree, but with some different rules.
    - in a **MaxBinaryHeap**, parent nodes are always larger than child nodes.
    - in a **MinBinaryHeap**, parent nodes are always smaller than child nodes.
    - each node can have **at most two** children
    - there is **no** order for nodes to the left or to the right
    - are used to implement Priority Queues, which are **very** commonly used data structures
    - heaps are also used quite a bit with graph traversal algorithms
* Methods:
    1. Insert:
        - **!Disclaimer** the relationship that helps find a parents children is: **2n+1** for the left child and **2n+2** for the right child -> **n** is the index of the current element
        - push the value into the values property on the heap
        - bubble the value up to its correct spot:
            - create a variable called index which is the length of the values property-1
            - create a variable called parentIndex which is the floor of (index-1)/2
            - keep looping as long as the values element at the parentIndex is less than the values element at the child index:
                - swap the value of the values element at the parentIndex with the value of the element property at the child index
                - set the index to be the parentIndex and start over
