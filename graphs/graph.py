class MyGraph:
    def __init__(self):
        self.adjacencyList = {}


    #add vertex method
    def addVertex(self, vertex):
        #check to see if the vertex already exits
        if vertex not in self.adjacencyList:
            #if it doesn't, add a vertex with an empty list
            self.adjacencyList[vertex] = []