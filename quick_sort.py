def quick_sort(values):

    # stopping condition
    if len(values) <= 1:
        return values

    # recursive pattern
    pivot = values[0]
    less_than_pivot = []
    more_than_pivot = []

    for i in values[1:]:
        if i <= pivot:
            less_than_pivot.append(i)
        else:
            more_than_pivot.append(i)
    # print("%15s %1s %-15s" %(less_than_pivot,[pivot],more_than_pivot))
    return quick_sort(less_than_pivot)+[pivot]+quick_sort(more_than_pivot)


alist = [4, 2, 1, 5, 3, 1, 4]

print("Before Quick-Sort!!: \n", alist)
print("\nAfter Quick-Sort!!: ", quick_sort(alist))
