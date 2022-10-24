

def selection_sort(values):
    sorted_list=[]
    """
    iterate through list (values) and find minimun value and move it to "sorted_list"
    """
    attempts=0
    while len(values)!=0:
        indexToMove=find_Min_index(values)
        sorted_list.append(values.pop(indexToMove))
        attempts+=1
    

    return sorted_list,attempts

def find_Min_index(values):
    minIndex=0

    for index in range(1,len(values)):
        if values[index]<values[minIndex]:
            minIndex=index

    return minIndex


numbers=[5,4,2,12,23,1,9,34,2,14]
print("Before Algorithm: ",numbers)

print("After Algorithm: ",selection_sort(numbers))