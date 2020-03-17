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
            left_child = (2*index) + 1
            right_child = (2 * index) + 2
            if left_child < 0 or left_child >= length:
                return return_node

            if right_child < 0 or right_child >= length:
                return return_node

            # \ is for simplified operation, in python in expression if we wanna go to new line, we use \
            if self.values[index].get_priority() < self.values[left_child].get_priority() and self.values[index].get_priority() < self.values[right_child].get_priority():
                return return_node
            if self.values[index].get_priority() > self.values[right_child].get_priority() > self.values[left_child].get_priority():
                self.values[index], self.values[left_child] = self.values[left_child], self.values[index]
                index = left_child
                continue

            if self.values[index].get_priority() > self.values[left_child].get_priority() > self.values[right_child].get_priority():
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
