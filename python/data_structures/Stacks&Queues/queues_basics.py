class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self,value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1

    def print_queue(self):
        current = self.first
        while current is not None:
            print(current.value)
            current = current.next

    def enqueue(self, value):
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
            self.length = 1
            return True
        self.last.next = node
        self.last = node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

#  Queue visual representation here

#         (last) <- O <- O <- O <- O  (First)






myQueue = Queue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

myQueue.dequeue()

print('Printing all nodes :\nWith length equals to:',myQueue.length,'\nWith first equals:',myQueue.first.value,'\nWith last equals:',myQueue.last.value)

myQueue.print_queue()
