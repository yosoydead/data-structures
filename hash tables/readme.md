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