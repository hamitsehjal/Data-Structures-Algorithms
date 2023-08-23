''' QuickSort Implementation'''


def quicksort(items):
    '''Base Condition'''
    if len(items) < 2:
        return items

    pivot = items[0]
    less = [item for item in items if item < pivot]
    more = [item for item in items if item > pivot]

    return quicksort(less)+[pivot]+quicksort(more)


my_list = [5, 1, 992, 0, 9, 3, 4, 6, 8, 7]

print(quicksort(my_list))
