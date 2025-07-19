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

    def pop(self):
        temp = self.head
        pre = self.head
        if self.length == 0 or self.head is None:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next = None
        self.length -= 1
        return temp.value

    def prepend(self,value):
        if self.length == 0:
            self.append(value)
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
        return node

    def popleft(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        first = self.head
        temp = self.head.next
        self.head.next = None
        self.head = temp
        return first







myList = LinkedList(1)
myList.append(2)
myList.append(3)

print('Printing all the nodes:')
myList.print_list()
print('After popping the last node :')
myList.pop()
myList.print_list()
print('After prepending node :')
myList.prepend(0)
myList.print_list()
print('After popleft node :')
myList.popleft()
myList.print_list()
