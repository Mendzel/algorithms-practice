class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def walk(curr, path):
    if curr is None:
        return path
    
    path.append(curr.value)
    walk(curr.left, path)
    walk(curr.right, path)

    return path

def in_walk(curr, path):
    if curr is None:
        return path
    
    walk(curr.left, path)
    path.append(curr.value)
    walk(curr.right, path)

    return path

def post_walk(curr, path):
    if curr is None:
        return path
    
    walk(curr.left, path)
    walk(curr.right, path)
    path.append(curr.value)

    return path
    
def pre_order_search(head):
    return walk(head, [])

def in_order_search(head):
    return in_walk(head, [])

def post_order_search(head):
    return post_walk(head, [])


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

print(pre_order_search(a))
print(in_order_search(a))
print(post_order_search(a))