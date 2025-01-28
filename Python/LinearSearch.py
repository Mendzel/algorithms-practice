def linear_search(arr, target):
    for x in arr:
        if x == target:
            return True
    return False

print(linear_search([1,2,3,4,5], 4))