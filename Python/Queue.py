class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.num = 1
    def addToQueue(self, value):
        node = Node(value)
        if self.num == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.num += 1
    def removeFromQueue(self):
        if self.num == 0:
            print('Empty queue')
            return
        temp = self.head
        self.head = self.head.next
        self.num -= 1
        return temp.value
    def peek(self):
        if self.num == 0:
            print('Empty queue')
            return
        return self.head.value


q = Queue(10)
print(q.peek())
q.addToQueue(5)
q.addToQueue(8)
print('Removed: {0}'.format(q.removeFromQueue()))
print('Removed: {0}'.format(q.removeFromQueue()))
print(q.peek())
print('Removed: {0}'.format(q.removeFromQueue()))
print(q.peek())