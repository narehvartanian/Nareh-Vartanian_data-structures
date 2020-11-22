class Node:
    def __init__(self,data,next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def addFirst(self,obj):
        node = Node(obj,self.front,None)
        self.front = node

    def addLast(self,obj):
        node = Node(obj,None,self.rear)
        self.rear = node

    def removeFront(self):
        if (self.front == None):
            print("The list is empty")
        else:
            tmp = self.front
            self.front = self.front.next
            tmp.next = None


    def removeRear(self):
        if (self.rear == None):
            print("The list is empty")
        temp = self.rear
        self.rear = self.rear.prev
        temp.prev = None

    def first(self):
        if (self.front == None):
            print("The List is empty")
        else:
          print(f'First node: {self.front.data}')

    def last(self):
        if (self.rear == None):
            print("The List is empty")
        else:
         # print("Last Node is:", {self.rear.data})
            print(f'Last node: {self.rear.data}')

def main():
    deque = Deque()
    deque.addFirst(0)
    deque.addFirst(1)
    deque.addFirst(2)
    deque.addFirst("3")
    deque.addLast("4")
    deque.addLast("5")
    deque.removeFront()
    deque.removeRear()

    deque.first()
    deque.last()

main()