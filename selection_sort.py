
from queue import Empty


def selection_sort(values):
    sorted_list=[]
    """
    iterate through list (values) and find minimun value and move it to "sorted_list"
    """
    while len(values)!=0:
        indexToMove=find_Min_index(values)
        sorted_list.append(values.pop(indexToMove))
    

    return sorted_list

def find_Min_index(values):
    minIndex=0

    for index in range(1,len(values)):
        if values[index]<values[minIndex]:
            minIndex=index

    return minIndex

    