class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,value):
        node = Node(value)
        self.top = node
        self.height = 1

    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
            self.height = 1
            return True
        node.next = self.top
        self.top = node
        self.height += 1
        return True

    def pop(self):
        if self.top is None:
            return None
        current = self.top
        self.top = self.top.next
        current.next = None
        self.height -= 1
        return current



myStack = Stack(0)

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.pop()
print('Printing all nodes :\nWith height equals to:',myStack.height,'\nWith top equals:',myStack.top.value)

myStack.print_stack()
