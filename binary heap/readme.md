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
    2. Removing from the heap
        - the standard place from where we remove elements is the root. In a MaxBinaryHeap it means removing the maximum value
        - remove the root
        - replace with the most recently added
        - adjust (sink down)
            * it is a procedure for deleting the root from the heap (extracting the maximum element in a max-heap or the minimum element in a min-heap) and restoring the properties is called **down-heap** (aka bubble-down, sift-down, extract min/max)
        - Pseudo Code:
            - swap the first value in the values property with the last one
            - pop from the values property, so you can return the value at the end
            - have the new root "sink down" to the correct spot:
                * your parent index starts at 0 (the root)
                * find the index of the left child: 2*index+1 (make sure its not out of bounds)
                * find the index of the right child: 2*index+2 (make sure its not out of bounds)
                * if the left or right child is greater than the element, swap. If both left and right children are larger, swap with the largest child
                * the child index you swapped to now becomes the new parent index
                * keep looping and swapping until neither child is larger than the element
                * **return the old root !**
