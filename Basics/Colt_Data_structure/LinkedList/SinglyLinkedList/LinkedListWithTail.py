class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # insert an element after last item in the list
    def push(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        elif self.head is self.tail:
            self.head.next = newNode
            self.tail = newNode
        
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1

        

    def printVals(self):
        newNode = self.head
        while newNode is not None:
            print(newNode.data)
            newNode = newNode.next

    def pop(self):
        newNode = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        if self.length == 2:
            self.head.next = None
            self.tail = None
            self.length -= 1
            return
        while newNode.next.next is not None:
            newNode = newNode.next

        self.tail = newNode
        newNode.next = None
        self.length -= 1
        


linkedList = LinkedList()
linkedList.push(10)
linkedList.push(20)
linkedList.push(30)
linkedList.push(40)
# linkedList.printVals()
linkedList.pop()
linkedList.pop()
linkedList.pop()
linkedList.printVals()

