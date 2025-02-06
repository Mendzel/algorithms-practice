class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(head, needle):
    queue = [head]

    while (len(queue)):
        curr = queue.pop(0)
        if curr.value == needle:
            return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return False
    




a = BinaryNode(10)
b = BinaryNode(15)
c = BinaryNode(1)
d = BinaryNode(5)
e = BinaryNode(4)
f = BinaryNode(2)
g = BinaryNode(3)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(bfs(a, 5))