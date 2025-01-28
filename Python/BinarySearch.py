def binary_search(arr, target):
    n = len(arr) // 2
    if arr[n] == target:
        return True
    if n <= 0:
        return False
    elif arr[n] < target:
        return binary_search(arr[n:], target)
    else:
        return binary_search(arr[0:n+1], target)

print(binary_search([1,2,3,4,5,6], 3))
