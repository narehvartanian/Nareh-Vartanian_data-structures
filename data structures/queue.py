class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def AddItem(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def RemoveItem(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None



def main():
    queue = Queue()
    queue.AddItem(1)
    queue.AddItem(2)
    queue.RemoveItem()
    queue.AddItem(3)
    queue.AddItem(4)
    queue.AddItem(5)
    queue.AddItem(6)
    queue.RemoveItem()
    queue.RemoveItem()

    print(f'Queue Front:{str(queue.front.data)}')
    print(f'Queue Front:{str(queue.rear.data)}')


main()
