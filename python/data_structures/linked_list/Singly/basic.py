class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        node = Node(value)
        self.head = node
        self.tail= node
        self.length = 1

    def print_list(self):
        temp =  self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        node = Node(value)
        if self.head is None or self.tail is None:
            self.head = node
            self.tail = node
            self.length = 1
            return node
        self.tail.next = node
        self.tail = node
        self.length += 1
        return node


myList = LinkedList(1)
myList.append(2)
myList.append(3)
print(myList.head.value)
print(myList.tail.value)
print(myList.print_list())