class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

# in java, use a LinkedList class, use add method (compared to push method which
# adds item at the front/head) to enqueue/add item to the end, and pop to remove item from head/front/begining

class Queue:

    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    # for enqueuing, we add at the end
    def enqueue(self, val):
        new_item = Node(val)

        if self.length == 0:
            self.length += 1
            self.head = new_item
            self.tail = new_item
            return

        self.tail.next = new_item
        self.tail = new_item
        self.length += 1
        return

    # for dequeing remove item from the beginning

    def dequeue(self):

        if self.length == 0:
            return None

        if self.length == 1:
            self.length = 0
            removed_item = self.head
            self.head = None
            self.tail = None
            return removed_item.val

        removed_item = self.head
        self.head = removed_item.next
        removed_item.next = None
        return removed_item.val
