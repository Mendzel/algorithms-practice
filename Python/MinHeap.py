class MinHeap:
    def __init__(self):
        self.length = 0
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self.heapifyUp(self.length)
        self.length += 1

    def delete(self):
        if self.length == 0:
            return None
        
        out = self.data[0]
        self.length -= 1
        if self.length == 0:
            self.data = []
            return out
        
        self.data[0] = self.data[self.length]
        self.data.pop()
        self.heapifyDown(0)
        return out



    def parentIndex(self, index):
        return (index - 1) // 2
    
    def leftChildIndex(self, index):
        return 2 * index + 1
    
    def rightChildIndex(self, index):
        return 2 * index + 2
    
    def heapifyUp(self, index):
        if index == 0:
            return
        
        parentIndex = self.parentIndex(index)
        parent = self.data[parentIndex]
        value = self.data[index]

        if parent > value:
            self.data[parentIndex], self.data[index] = self.data[index], self.data[parentIndex]
            self.heapifyUp(parentIndex)

    def heapifyDown(self, index):
        lIndex = self.leftChildIndex(index)
        rIndex = self.rightChildIndex(index)

        if index >= self.length or lIndex >= self.length:
            return
        
        lValue = self.data[lIndex]
        rValue = self.data[rIndex]
        value = self.data[index]

        if lValue > rValue and value > rValue:
            self.data[rIndex], self.data[index] = self.data[index], self.data[rIndex]
            self.heapifyDown(rIndex)
        elif rValue > lValue and value > lValue:
            self.data[lIndex], self.data[index] = self.data[index], self.data[lIndex]
            self.heapifyDown(lIndex)
        



heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(4)
heap.insert(20)
heap.delete()
heap.insert(70)
heap.insert(81)
heap.insert(1)
heap.insert(12)
heap.insert(3)
heap.delete()
print(heap.data)