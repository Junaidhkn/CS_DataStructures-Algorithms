class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
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
            return True
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0 or self.head is None:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self,value):
        if self.length == 0:
            self.append(value)
        node = Node(value)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1
        return True

    def popleft(self):
        if self.length == 0:
            return None
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.head.prev = None
        self.length -= 1
        return temp

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp= temp.next
        return temp

    def set_value(self,index,value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return temp
        # temp = self.get(index)
        # if temp:
        #     temp.value = value
        #     return True
        # return False

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        node = Node(value)
        temp = self.get(index - 1)
        node.next = temp.next
        temp.next.prev = node
        node.prev = temp
        temp.next = node
        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popleft()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


myList = DoubleLinkedList(0)

myList.append(1)
myList.append(2)
myList.append(3)
myList.insert(4,4)



print('Printing all nodes :\nWith Length equals to:',myList.length,'\nWith head equals:',myList.head.value,'\nWith tail equals:',myList.tail.value)
myList.print_list()