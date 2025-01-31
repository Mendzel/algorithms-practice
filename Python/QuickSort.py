def qs(arr, low, high):
    if low >= high:
        return
    
    pivotIndex = partition(arr, low, high)

    qs(arr, low, pivotIndex)
    qs(arr, pivotIndex + 1, high)

def partition(arr, low, high):
    middle = (low+ high) // 2
    pivot = arr[middle]
    pivotIndex = middle
    index = low - 1
    for i in range(low, high):
        if arr[i] < pivot:
            index += 1
            arr[i], arr[index] = arr[index], arr[i]
            if index == pivotIndex:
                pivotIndex = i
    
    index += 1
    arr[pivotIndex], arr[index] = arr[index], arr[pivotIndex]
    return index


array = [5, 2, 10, 201, 872, 11, 983, 99, 23]
qs(array, 0, len(array))
print(array)