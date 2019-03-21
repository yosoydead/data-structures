class MyGraph:
    def __init__(self):
        self.adjacencyList = {}


    #add vertex method
    def addVertex(self, vertex):
        #check to see if the vertex already exits
        if vertex not in self.adjacencyList:
            #if it doesn't, add a vertex with an empty list
            self.adjacencyList[vertex] = []
    
    #add edge method
    def addEdge(self, vertex1, vertex2):
        #find in the adjacency list the key of vertex1 and push vertex2 to the array
        self.adjacencyList[vertex1].append(vertex2)

        #find in the adjacency list the key of vertex2 and push vertex1 to the array
        self.adjacencyList[vertex2].append(vertex1)