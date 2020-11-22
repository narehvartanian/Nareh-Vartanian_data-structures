class Node:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None


class doubleLinkedList:
    last = None

    def __init__(self):
        self.headVal = None


    def addFirst(self,newData):
        newNode = Node(newData)
        newNode.next = self.headVal
        if self.headVal is None:
            self.last = newNode
        if self.headVal is not None:
            self.headVal.prev = newNode
        self.headVal = newNode

    def addLast(self, newData):
        newNode = Node(newData)
        newNode.next = None
        if self.headVal is None:
            newNode.prev = None
            self.headVal= newNode
            return
        last = self.headVal
        while (last.next is not None):
            last = last.next
        last.next = newNode
        newNode.prev = last
        self.last = newNode
        return

    def addBefore(self, nextNode, newData):
        if nextNode is None:
            return
        newNode = Node(newData)
        newNode.prev = nextNode.prev
        nextNode.prev = newNode
        newNode.next = nextNode
        if newNode.next is not None:
            newNode.prev.next = newNode




    def addAfter(self, prevNode, newData):
        if prevNode is None:
            return
        newNode = Node(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode
        newNode.prev = prevNode
        if newNode.next is not None:
            newNode.next.prev = newNode


    def removeFirst(self):
        self.removeNode(self.First())

    def removeNode(self, removeKey):

        headVal = self.headVal

        if headVal is not None:
            if headVal.data == removeKey:
                self.headVal = headVal.next
                headVal = None
                return
        while headVal is not None:
            if headVal.data == removeKey:
                break
            previous = headVal
            headVal = headVal.next
        if headVal == None:
            return
        previous.next = headVal.next

        headVal = None

    def removeLast(self):
        self.removeNode(self.last.data)
        self.last = self.last.prev

    def First(self):
        return self.headVal.data

    def Last(self):
        return self.last.data

    def IndexOf(self,node):
        item = self.headVal
        index = 0
        while item is not None:
            if item.data == node:
                return index
            item = item.next
            index += 1

    def Size(self):
        size = 1
        item = self.headVal
        if item == None:
            return 0
        while item is not None:
            if item.next == None:
                return size
            item = item.next
            size += 1

    def listprint(self):
        node = self.headVal
        while node is not None:
            print(node.data),
            node = node.next


def main():
    Dll = doubleLinkedList()

    Dll.addFirst("3")
    Dll.addFirst("2")
    Dll.addBefore(Dll.headVal.next, "1")
    Dll.addAfter(Dll.headVal.next,"4")
    Dll.removeLast()

    Dll.listprint()

    print(f'First is:{str(Dll.First())}')
    print(f'Last is:{str(Dll.Last())}')

main()