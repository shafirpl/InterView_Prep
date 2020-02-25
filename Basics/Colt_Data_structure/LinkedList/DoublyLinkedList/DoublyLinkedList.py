class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None


class doublyLinkedList:
    def  __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # insert an element after last item in the list
    def push(self,data):
        newNode = Node(data)
        if(self.length == 0):
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return

        if(self.head is self.tail):
            self.head.next = newNode
            newNode.prev = self.head
            self.tail = newNode
            self.length += 1
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.length += 1
        return


    def printList(self):
        currentNode = self.head
        while(currentNode is not None):
            print(currentNode.data)
            currentNode = currentNode.next

    def pop(self):
        if(self.length == 0):
            return
        if(self.length == 1):
            self.head = None
            self.tail = None
            self.length = 0
            return

        node = self.tail.prev
        node.next = None
        self.tail.prev = None
        self.length -= 1
        self.tail = node
        return

    def popWithoutTail(self):
        if(self.length == 0):
            return
        if(self.length == 1):
            self.head = None
            self.tail = None
            self.length = 0
            return

        node = self.head
        while(node.next is not None):
            node = node.next
        
        prevNode = node.prev
        prevNode.next = None
        node.prev = None
        self.length -= 1
        self.tail = prevNode
        return

    def removeFromHead(self):
        if (self.length == 0):
            return
        if (self.length == 1):
            self.head = None
            self.tail = None
            self.length = 0
            return

        node = self.head.next
        self.head.next = None
        node.prev = None
        self.head = node
        self.length -= 1
        return

    def insertAtHead(self,data):
        newNode = Node(data)
        if (self.length == 0):
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return

        self.length += 1
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        return
        






doublyLinkedList = doublyLinkedList()
doublyLinkedList.push(10)
doublyLinkedList.push(20)
doublyLinkedList.push(30)
# doublyLinkedList.printList()
doublyLinkedList.pop()
# doublyLinkedList.printList()
doublyLinkedList.pop()
# doublyLinkedList.printList()
doublyLinkedList.pop()
doublyLinkedList.push(10)
doublyLinkedList.push(20)
doublyLinkedList.push(30)
# doublyLinkedList.printList()
doublyLinkedList.popWithoutTail()
# doublyLinkedList.printList()
doublyLinkedList.popWithoutTail()
# doublyLinkedList.printList()
doublyLinkedList.popWithoutTail()
doublyLinkedList.push(10)
doublyLinkedList.push(20)
doublyLinkedList.push(30)
# doublyLinkedList.printList()
doublyLinkedList.removeFromHead()
# doublyLinkedList.printList()
doublyLinkedList.removeFromHead()
# doublyLinkedList.printList()
doublyLinkedList.removeFromHead()
# doublyLinkedList.printList()
doublyLinkedList.insertAtHead(30)
doublyLinkedList.insertAtHead(20)
doublyLinkedList.insertAtHead(10)
doublyLinkedList.printList()

        


        
