class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def get_priority(self):
        return self.priority

    def get_value(self):
        return self.value


# we will be using min heap for this
class PriorityQueue:
    def __init__(self):
        self.values = []

    def get_length(self):
        return len(self.values)

    def enqueue(self, value, priority):
        new_node = Node(value, priority)
        self.insert(new_node)

    def insert(self, node):
        if len(self.values) <= 0:
            self.values.append(node)
            return
        self.values.append(node)
        index = len(self.values) - 1
        parent_index = (index - 1) // 2

        while self.values[index].get_priority() < self.values[parent_index].get_priority() and parent_index >= 0:
            self.values[parent_index], self.values[index] = self.values[index], self.values[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def dequeue(self):
        return self.extract_min()

    def extract_min(self):
        if len(self.values) <= 0:
            return None
        if len(self.values) == 1:
            return self.values.pop()

        length = len(self.values) - 1
        self.values[0], self.values[length] = self.values[length], self.values[0]
        return_node = self.values.pop()
        index = 0

        while True:
            left_child = (2 * index) + 1
            right_child = (2 * index) + 2
            if left_child < 0 or left_child >= length:
                return return_node

            if right_child < 0 or right_child >= length:
                return return_node

            if self.values[left_child].get_priority() == self.values[right_child].get_priority() == self.values[
                index].get_priority():
                return return_node

            # \ is for simplified operation, in python in expression if we wanna go to new line, we use \
            if self.values[index].get_priority() < self.values[left_child].get_priority() and self.values[
                index].get_priority() < self.values[right_child].get_priority():
                return return_node
            if self.values[index].get_priority() > self.values[right_child].get_priority() > self.values[
                left_child].get_priority():
                self.values[index], self.values[left_child] = self.values[left_child], self.values[index]
                index = left_child
                continue

            if self.values[index].get_priority() > self.values[left_child].get_priority() > self.values[
                right_child].get_priority():
                self.values[index], self.values[right_child] = self.values[right_child], self.values[index]
                index = right_child
                continue

            if self.values[index].get_priority() > self.values[left_child].get_priority():
                self.values[index], self.values[left_child] = self.values[left_child], self.values[index]
                index = left_child
                continue

            if self.values[index].get_priority() > self.values[right_child].get_priority():
                self.values[index], self.values[right_child] = self.values[right_child], self.values[index]
                index = right_child
                continue

    def returnQueue(self):
        return_heap = []

        for i in range(len(self.values)):
            value_priority_pair = {self.values[i].get_priority(): self.values[i].get_value()}
            return_heap.append(value_priority_pair)

        return return_heap


class Vertex:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"[{self.name},{self.weight}]"

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight


class Graphs:
    def __init__(self):
        self.adjancy_list = {}

    def addVertex(self, vertex_name):
        if self.adjancy_list.get(vertex_name) is not None:
            return
        self.adjancy_list[vertex_name] = []

    def addEdge(self, first_vertex_name, second_vertex_name, weight):
        if self.adjancy_list.get(first_vertex_name) is None or self.adjancy_list.get(second_vertex_name) is None:
            return False

        if first_vertex_name is second_vertex_name:
            return False

        first_vertex = Vertex(first_vertex_name, weight)
        second_vertex = Vertex(second_vertex_name, weight)
        # checking to see if the edge already exists and if so, don't add it
        if self.adjancy_list[first_vertex.name].count(second_vertex) > 0:
            return False
        self.adjancy_list[first_vertex.name].append(second_vertex)
        self.adjancy_list[second_vertex_name].append(first_vertex)
        return True

    def printGraph(self):
        for item in self.adjancy_list:
            print(f"{item}:{self.adjancy_list[item]}")

    def returnGraph(self):
        return self.adjancy_list

    # def removeEdge(self, first_vertex_name, second_vertex_name):
    #     if self.adjancy_list.get(first_vertex_name) is None or self.adjancy_list.get(second_vertex_name) is None:
    #         return False
    #     if first_vertex_name is second_vertex_name:
    #         return False
    #     self.adjancy_list[first_vertex_name].remove(second_vertex)
    #     self.adjancy_list[second_vertex].remove(first_vertex)
    #     return True
    #
    # def removeVertex(self, vertex):
    #     if (self.adjancy_list.get(vertex) is None):
    #         return
    #     for item in self.adjancy_list:
    #         self.removeEdge(item, vertex)
    #
    #     self.adjancy_list.pop(vertex)

    def dijkstra(self, first, last):
        nodes = PriorityQueue()
        previous = {}
        distance = {}
        inf = 99999
        result = []

        # initialization
        for item in self.adjancy_list:
            if item == first:
                nodes.enqueue(first, 0)
                distance[first] = 0
                previous[first] = None
            else:
                nodes.enqueue(item, inf)
                distance[item] = inf
                previous[item] = None

        # print(nodes.returnQueue())
        # item = nodes.dequeue()
        # print(item)

        # print(nodes.get_length())
        while nodes.get_length() > 0:
            item = nodes.dequeue().get_value()

            # explore the neighbours
            for neighbour in self.adjancy_list[item]:
                totalDistance = distance[item] + neighbour.get_weight()
                if totalDistance < distance[neighbour.get_name()]:
                    distance[neighbour.get_name()] = totalDistance
                    previous[neighbour.get_name()] = item
                    nodes.enqueue(neighbour.get_name(), totalDistance)

        smallest = last
        while previous[smallest] is not None:
            result.append(smallest)
            smallest = previous[smallest]

        result.append(smallest)

        result.reverse()

        return result

    def dfs(self, vertex):
        visited = {}
        result = []
        self.dfsHelper(vertex, visited, result)
        return result

    def dfsHelper(self, vertex, visited, result):
        if vertex is None:
            return

        if visited.get(vertex) is None:
            visited[vertex] = True
            result.append(vertex)
        else:
            return

        for item in self.adjancy_list[vertex]:
            self.dfsHelper(item, visited, result)

    # the recursive and iterative result won't match exactly
    # however the way the iterative and recursive solution traverse
    # the list are same here, so it is fine
    # https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/learn/lecture/8344890#questions
    # watch from 3:56
    # def dfsIterative(self, vertex):
    #     stack = []
    #     stack.append(vertex)
    #     result = []
    #     visited = {}
    #
    #     while len(stack) > 0:
    #         poped_vertex = stack.pop()
    #         if visited.get(poped_vertex) is None:
    #             result.append(poped_vertex)
    #             visited[poped_vertex] = True
    #         for item in self.adjancy_list[poped_vertex]:
    #             if visited.get(item) is None:
    #                 stack.append(item)
    #     return result
    #
    # def bfs(self, vertex):
    #     visited = {}
    #     result = []
    #     queue = []
    #
    #     queue.append(vertex)
    #
    #     while len(queue):
    #         current_vertex = queue.pop(0)
    #         if visited.get(current_vertex) is None:
    #             visited[current_vertex] = True
    #             result.append(current_vertex)
    #         for item in self.adjancy_list[current_vertex]:
    #             if visited.get(item) is None:
    #                 visited[item] = True
    #                 result.append(item)
    #                 queue.append(item)
    #     return result


graph = Graphs()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")
graph.addVertex("F")

graph.addEdge("A", "B", 4)
graph.addEdge("A", "C", 2)
graph.addEdge("B", "E", 3)
graph.addEdge("C", "D", 2)
graph.addEdge("C", "F", 4)
graph.addEdge("D", "E", 3)
graph.addEdge("D", "F", 1)
graph.addEdge("E", "F", 1)

print(graph.dijkstra("A", "E"))
