def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        while i > 0 and list[i-1] > value:
            list[i] = list[i-1]
            i -= 1
        list[i] = value
    return list


print(insertion_sort([1,20,12,876,665,2,76,55,234,122]))