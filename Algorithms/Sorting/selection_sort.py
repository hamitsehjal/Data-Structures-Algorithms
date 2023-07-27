"Selection Sort O(n^2) - Quadratic Runtime"


def selection_sort(item_list):
    """Sorts a list of items using the Selection Sort algorithm."""
    new_list = []
    while item_list:
        # Retrieve index of the smallest element
        index = smallest_item_index(item_list)
        new_list.append(item_list.pop(index))

    return new_list


def smallest_item_index(item_list):
    """ Returns the index of the smallest item in the list"""
    min_value = item_list[0]
    index = 0

    for i in range(1, len(item_list)):
        if item_list[i] < min_value:
            min_value = item_list[i]
            index = i

    return index


print(selection_sort([100, 4, 1, 99, 2, 0, -1, -9]))
