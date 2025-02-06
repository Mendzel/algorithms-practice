class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#First Tree
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

#Second Tree
h = BinaryNode(10)
i = BinaryNode(15)
j = BinaryNode(1)
k = BinaryNode(5)
l = BinaryNode(4)
m = BinaryNode(2)
#n = BinaryNode(3)

h.left = i
h.right = j
i.left = k
i.right = l
j.left = m
#j.right = n

def compare(node, node2):
    if node == None and node2 == None:
        return True
    if node == None or node2 == None:
        return False
    if node.value != node2.value:
        return False
    
    return compare(node.left, node2.left) and compare(node.right, node2.right)

print(compare(a, h))