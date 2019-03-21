from graph import MyGraph

g = MyGraph()
g.addVertex("tokyo")
g.addVertex("dallas")
g.addVertex("aspen")
g.addEdge("dallas", "tokyo")
g.addEdge("dallas", "aspen")
g.removeEdge("dallas", "aspen")
print(g.adjacencyList)