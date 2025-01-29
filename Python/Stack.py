class Node:
    def __init__(self, value, prev = None):
        self.value = value
        self.prev = prev

class Stack:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.num = 1
    def addToStack(self, value):
        node = Node(value)
        if self.num == 0:
            self.head = node
        else:
            node.prev = self.head
            self.head = node
        self.num += 1
    def removeFromStack(self):
        if self.num == 0:
            print('Empty stack')
            return
        temp = self.head
        self.head = self.head.prev
        self.num -= 1
        return temp.value
    def peek(self):
        if self.num == 0:
            print('Empty stack')
            return
        return self.head.value


q = Stack(10)
print(q.peek())
q.addToStack(5)
q.addToStack(8)
print('Removed: {0}'.format(q.removeFromStack()))
print('Removed: {0}'.format(q.removeFromStack()))
print(q.peek())
print('Removed: {0}'.format(q.removeFromStack()))
print(q.peek())