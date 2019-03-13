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