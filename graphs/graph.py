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

    #remove edge
    def removeEdge(self, vertex1, vertex2):
        #should reassign the key of vertex1 to be an array that does not contain vertex2
        self.adjacencyList[vertex1] = list(filter(lambda v: v != vertex2, self.adjacencyList[vertex1]))

        #should reassign the key of vertex2 to be an array that does not contain vertex1
        self.adjacencyList[vertex2] = list(filter(lambda v: v != vertex1, self.adjacencyList[vertex2]))

    #remove vertex function
    def removeVertex(self, vertex):
        #loop as long as there are any other vertices in the adjacency list for that vertex
        while len(self.adjacencyList[vertex]):
            #call the **removeEdge** function with the vertex we are removing and any values in the adjacency list for that vertex
            currVertex = self.adjacencyList[vertex].pop()
            self.removeEdge(vertex, currVertex)

        #delete the key in the adjacency list
        self.adjacencyList.pop(vertex, None)