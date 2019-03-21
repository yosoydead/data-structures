* A **graph** is a collection of nodes and connections between those nodes. Imagine a bunch of dots and connections between them. There is no **parent node**/starting point/patterns.
* Uses:
    - social networkings
    - location/mapping
    - routing algorithms
    - visual hierarchy
    - etc
* Terminology:
    - **vertex** -> a node
    - **edge** -> connection between nodes
    - **weighted/unweighted** -> values assigned to distances between vertices (IE between node B and node E there is a "distance" of 35)
    - **directed/undirected** -> directions assigned to distances between vertices (IE node A and B point to each other, but A also points to C)
* Storing graphs:
    - you need to store **nodes/vertices**
    - a way to store their connection
    1. **Adjacency matrix**
        - inside a **boolean** matrix, you store values of 0 and 1 if there is/isn't a connection between some nodes
        - it takes up more space (in sparse graphs)
        - it is slower to iterate over all edges
        - it is faster to lookup a specific edge
    2. **Adjacency list**
        - use an array/list to store edges (node 3 has connections to nodes 4 and 2. check if node 3 has any other connections)
        - it can take up less space (in sparse graphs)
        - it faster to iterate over all edges
        - it can be slower to lookup a specific edge
* I'll use an **adjacency list** method here because most real-world data tends to lend itself to sparser and/or larger graphs.
* Methods (i'll build an **undirected** graph):
    - in the constructor, initialize an empty list to store connections
    - **adding a vertex**:
        * accepts a name of a vertex
        * it should add a key to the adjacency list with the name of the vertex and set its value to be an empty array
