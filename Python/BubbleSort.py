def bubble_sort(list):
    list_lenght = len(list) - 1
    for i in range(list_lenght):
        no_swaps = True
        for j in range(list_lenght - i): # -i żeby nie sprawdzać już posortowanych elementów
            if list[j] > list[j+1]:
                list[j], list[j + 1] = list[j + 1], list[j] #zamiana miejscami, w innych językach wymagałaby zmiennej tymczasowej
                no_swaps = False
        if no_swaps:
            return list
    return list


print(bubble_sort([1,20,12,876,665,2,76,55,234,122]))
