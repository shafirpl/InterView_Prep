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
        if(self.length == 0):
            print(None)
            return
        newNode = self.head
        while newNode is not None:
            print(newNode.data)
            newNode = newNode.next

    def pop(self):
        
        if self.length <= 0:
            return
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
    
    def removeFromHead(self):
        if(self.length == 0):
            return
        if(self.length == 1):
            self.head = None
            self.length = 0
            self.tail = None
            return
        self.head = self.head.next
        self.length -= 1

    def insertIntoHead(self,val):
        newNode = Node(val)

        if(self.length == 0):
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return
        
        self.length += 1
        newNode.next = self.head
        self.head = newNode

    def getValAtIndex(self,index):
        if(self.length <= 0):
            return None
        if(index>self.length):
            return "Index out of range"
        node = self.head
        
        for i in range(0,index+1):
            if(i != index):
                node = node.next
        return node.data

    def setValAtIndex(self, index, data):
        if(self.length <= 0):
            return None
        if(index > self.length):
            return "Index out of range"
        node = self.head

        for i in range(0, index+1):
            if(i != index):
                node = node.next
        node.data = data
        return node.data
    
    def insertAtIndex(self,index,val):
        if(index <0 and index > self.length):
            return ("Invalid index")
        newNode = Node(val)
        if(self.length == 0 ):
            self.head  = newNode
            self.tail = newNode
            self.length +=1
            return
        
        if(index == 0):
            newNode.next = self.head
            self.head = newNode
            self.length +=1
            return
        if(index == self.length):
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
            return
        
        i = 1
        currentNode = self.head
        while(i!= index):
            currentNode = currentNode.next
            i+= 1
        newNode.next = currentNode.next
        currentNode.next = newNode
        self.length += 1

    def removeAtIndex(self,index):
        if(index < 0 and index > self.length):
            return ("Invalid index")
        if(self.length == 0):
            return None

        if(index == 0):
            self.head = self.head.next
            self.length -= 1
            return 
        
        if(index == self.length):
            # TODO
            pass




linkedList = LinkedList()
linkedList.push(10)
linkedList.push(20)
linkedList.push(30)
linkedList.push(40)
# linkedList.printVals()
linkedList.pop()
linkedList.pop()
linkedList.pop()
# linkedList.printVals()
linkedList.pop()
linkedList.pop()
linkedList.pop()
linkedList.push(10)
linkedList.push(20)
linkedList.push(30)
linkedList.push(40)
linkedList.removeFromHead()
# linkedList.printVals()
linkedList.removeFromHead()
linkedList.removeFromHead()
linkedList.removeFromHead()
linkedList.removeFromHead()
# linkedList.printVals()
linkedList.insertIntoHead(5)
linkedList.push(10)
linkedList.push(20)
linkedList.push(30)
linkedList.push(40)
linkedList.insertIntoHead(1)
# linkedList.printVals()
# print(f" Head is {linkedList.head.data}, taile is {linkedList.tail.data}, length is {linkedList.length}") 
# print(linkedList.getValAtIndex(120))
linkedList.setValAtIndex(0,0)
linkedList.setValAtIndex(5,35)
linkedList.setValAtIndex(1,1)
linkedList.insertAtIndex(2,2)
linkedList.printVals()


