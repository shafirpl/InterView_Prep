# array based implementation

class ArrayBasedStack:

    def __init__(self):
        self.stack = []
        self.length = 0

    def push(self, val):
        self.stack.append(val)
        self.length += 1
        return val

    def pop(self):
        self.length -= 1
        return self.stack.pop()

    def search(self, val):
        if self.length == 0:
            return False

        for i in range(0, self.length):
            if self.stack[i] == val:
                return True

        return False


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedListBasedStack:

    def __init__(self):
        self.length = 0
        self.first = None
        self.last = None

    def push(self, val):
        new_item = Node(val)
        self.length += 1
        if self.length == 1:
            self.last = new_item
            self.first = new_item
            return

        new_item.next = self.last
        self.last = new_item

    def pop(self):
        if self.length == 0:
            return

        self.length -= 1

        if self.length == 1:
            last_node = self.last
            self.last = None
            self.first = None
            return last_node.val

        next_node = self.last.next
        return_node = self.last
        self.last.next = None
        self.last = next_node
        return return_node.val

    def search(self, val):
        if self.length == 0:
            return False

        item = self.last

        i = 0
        while item is not None:
            if item.val is val:
                return True
            item = item.next
            i += 1

        return False
