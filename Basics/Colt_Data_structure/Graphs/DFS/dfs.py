class Graphs:
    def __init__(self):
        self.adjancy_list = {}

    def addVertex(self, vertex):
        if(self.adjancy_list.get(vertex) is not None):
            return
        self.adjancy_list[vertex] = []

    def addEdge(self, first_vertex, second_vertex):
        if(self.adjancy_list.get(first_vertex) is None or self.adjancy_list.get(second_vertex) is None):
            return False
        # checking to see if the edge already exists and if so, don't add it
        if(self.adjancy_list[first_vertex].count(second_vertex) > 0):
            return False
        if(first_vertex is second_vertex):
            return False
        self.adjancy_list[first_vertex].append(second_vertex)
        self.adjancy_list[second_vertex].append(first_vertex)
        return True

    def printGraph(self):
        for item in self.adjancy_list:
            print(f"{item}:{self.adjancy_list[item]}")

    def returnGraph(self):
        return self.adjancy_list

    def removeEdge(self, first_vertex, second_vertex):
        if(self.adjancy_list.get(first_vertex) is None or self.adjancy_list.get(second_vertex) is None):
            return False
        if(first_vertex is second_vertex):
            return False
        self.adjancy_list[first_vertex].remove(second_vertex)
        self.adjancy_list[second_vertex].remove(first_vertex)
        return True

    def removeVertex(self, vertex):
        if (self.adjancy_list.get(vertex) is None):
            return
        for item in self.adjancy_list:
            self.removeEdge(item, vertex)

        self.adjancy_list.pop(vertex)

    def dfs(self,vertex):
        visited = {}
        result = []
        self.dfsHelper(vertex,visited,result)
        return result

    def dfsHelper(self,vertex, visited, result):
        if vertex is None:
            return

        if visited.get(vertex) is None:
            visited[vertex] = True
            result.append(vertex)
        else:
            return

        for item in self.adjancy_list[vertex]:
            self.dfsHelper(item,visited,result)

        
g = Graphs()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")


g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "E")
g.addEdge("D", "E")
g.addEdge("D", "F")
g.addEdge("E", "F")
# graph.printGraph()
# print("Removing vertex")
# graph.removeVertex("A")
# graph.printGraph()
print(g.dfs("A"))
