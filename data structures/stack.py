class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None


    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False


    def push(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode



    def pop(self):

        if self.isEmpty():
            return None

        else:

            popped = self.head
            self.head = self.head.next
            popped.next = None
            return popped.data



    def peek(self):

        if self.isEmpty():
            return None

        else:
            return self.head.data


    def display(self):

        iternode = self.head
        if self.isEmpty():
            print("Stack Underflow")

        else:

            while (iternode != None):
                print(iternode.data, " ", end=" ")
                iternode = iternode.next
            return


def main():
    s = Stack()

    s.push("H")
    s.push("E")
    s.push("R")
    s.push("A")
    s.push("N")

    s.display()
    print("\nTop element: ", s.peek())

    s.pop()
    s.display()

    print("\nTop element: ", s.peek())


main()

