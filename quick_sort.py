
def quick_sort(values):

    # stopping condition for recursion
    if len(values) <= 1:
        return values

    # recursive pattern
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for i in values[1:]:
        if values[i] <= pivot:
            less_than_pivot.append(values[i])
        else:
            greater_than_pivot.append(values[i])

    return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)

