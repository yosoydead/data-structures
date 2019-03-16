* What a **hash table** is:
    - a data structure that is used to store **key-value** pairs
    - they are like arrays, but the keys are not ordered
    - unlike arrays, hash tables are *fast* for all of the following operations: 
        - finding values
        - adding new values
        - removing values
* Why should I care?
    - nearly every programming language has some sort of hash table data structure
    - because of their speed, hash tables are very commonly used
* Hash tables in the wild:
    - python has *Dictionaries* or *dict*
    - javascript has *objects* and *maps*
    - java, go, scala have *maps*
    - c# has *dictionary* -> a collection of *Key-Value* pair
* Example:
    - imagine we want to store some colors. We could just use an array/list:
        - colors = ["#ff69b4", "#ff4500", "#00ffff"]
    - if we need a certain color, we can't access it directly without looping over the entire array
    - it would be nice if instead of using indices to access the color, we could use more human-readable keys
        - colors["cyan"]
* To implement a hash table, I'll be using an array.
* In order to loop up values by key, we need a way to **convert keys into valid array indices**.
    - a function that performs this task is called a **hash function**
    - what makes a good hash function:
        - needs to be fast(i.e. constant time)
        - doesn't cluster outputs at specific indices, but distributes uniformly
        - deterministic (same input yields same output)
* This is a very basic implementation. It doesn't know what to do if you add an item which has duplicate key and many more.
