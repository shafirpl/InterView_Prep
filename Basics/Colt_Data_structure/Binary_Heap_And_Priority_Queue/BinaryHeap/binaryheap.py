class BinaryMaxHeap:
    def __init__(self):
        self.values = []

    def insert(self, value):
        if len(self.values) <= 0:
            self.values.append(value)
            return
        self.values.append(value)
        index = len(self.values) - 1
        parent_index = (index - 1) // 2

        while self.values[index] > self.values[parent_index] and parent_index >= 0:
            self.values[parent_index], self.values[index] = self.values[index], self.values[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def extract_max(self):
        if len(self.values) <= 0:
            return
        if len(self.values) == 1:
            self.values.pop()
            return

        length = len(self.values) - 1
        self.values[0], self.values[length] = self.values[length], self.values[0]
        self.values.pop()
        index = 0

        while True:
            left_child = (2*index) + 1
            right_child = (2 * index) + 2
            if left_child < 0 or left_child >= length:
                return

            if right_child < 0 or right_child >= length:
                return

            # \ is for simplified operation, in python in expression if we wanna go to new line, we use \
            if self.values[index] > self.values[left_child] and self.values[index] > self.values[right_child]:
                return
            if self.values[index] < self.values[right_child] < self.values[left_child]:
                self.values[index], self.values[left_child] = self.values[left_child], self.values[index]
                index = left_child
                continue

            if self.values[index] < self.values[left_child] < self.values[right_child]:
                self.values[index], self.values[right_child] = self.values[right_child], self.values[index]
                index = right_child
                continue

            if self.values[index] < self.values[left_child]:
                self.values[index], self.values[left_child] = self.values[left_child], self.values[index]
                index = left_child
                continue

            if self.values[index] < self.values[right_child]:
                self.values[index], self.values[right_child] = self.values[right_child], self.values[index]
                index = right_child
                continue

    def return_heap(self):
        return self.values

    def print_heap(self):
        for i in range(self.values):
            print(self.values[i])
