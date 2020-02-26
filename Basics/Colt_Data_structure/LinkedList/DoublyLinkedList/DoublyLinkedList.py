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
        
    def getValAtIndex(self,index):
        if (index<0 or index>= self.length):
            return "index out of range"
        if(self.length == 0):
            return None
        node = self.head
        for i in range(0,index+1):
            if (i != index):
                node = node.next
        return node.data

    def setValAtIndex(self,index,data):
        if (index < 0 or index >= self.length):
            return "index out of range"
        if(self.length == 0):
            return None
        node = self.head
        for i in range(0,index+1):
            if (i != index):
                node = node.next
        node.data = data
        return node.data


    def getValAtIndexOptimized(self, index):
        if (index < 0 or index >= self.length):
            return "index out of range"
        if(self.length == 0):
            return None

        halfLength = self.length // 2
        if(index <= halfLength):
            node = self.head
            for i in range(0, index+1):
                if (i != index):
                    node = node.next
        
        else:
            node = self.tail
            count = self.length - 1

            while(count != index):
                count -= 1
                node = node.prev

        return node.data

    def insert(self,index,data):
        if (index<0 or index>= self.length):
            return "Index out of range"
        
        if (self.length == 0):
            return 

        
        if(index == 0):
            self.insertAtHead(data)
            return
        
        if(index == self.length - 1):
            self.push(data)
            return

        newNode = Node(data)
        

        if(index <= self.length // 2):
            prevNode = self.head
            for i in range(1,index):
                prevNode = prevNode.next

        else:
            prevNode = self.tail
            i = self.length - 1
            while(i > index - 1):
                prevNode = prevNode.prev
                i -= 1

        nextNode = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = nextNode
        nextNode.prev = newNode
        self.length += 1
        return

    def remove(self,index,data):
        if(index<0 or index>= self.length):
            return "Index out of range"
        
        if(self.length == 0):
            return

        if(self.length == 1 or index == 0):
            self.removeFromHead()
            return

        # TODO other stuff

        
        

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
doublyLinkedList.push(40)
doublyLinkedList.push(40)
# doublyLinkedList.printList()
# print(doublyLinkedList.getValAtIndex(0))
# print(doublyLinkedList.getValAtIndex(1))
# print(doublyLinkedList.getValAtIndex(2))
doublyLinkedList.setValAtIndex(4,50)
# print(doublyLinkedList.getValAtIndexOptimized(0))
# print(doublyLinkedList.getValAtIndexOptimized(1))
# print(doublyLinkedList.getValAtIndexOptimized(2))
# print(doublyLinkedList.getValAtIndexOptimized(3))
# print(doublyLinkedList.getValAtIndexOptimized(4))
# doublyLinkedList.printList()
doublyLinkedList.insert(0,0)
doublyLinkedList.insert(doublyLinkedList.length-1,100)
doublyLinkedList.insert(5,45)
doublyLinkedList.insert(2,15)
doublyLinkedList.printList()

        


        
