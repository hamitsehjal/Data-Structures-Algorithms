def merge_sort(values):

    # stopping condition for the recursive function
    if len(values)<=1:
        return values

    # recursive pattern
    mid_point=len(values)//2

    left_values=values[:mid_point]
    right_values=values[mid_point:]

    sorted_values=[]

    left_index=0
    right_index=0

    while left_index<len(left_index) and right_index<len(right_index):
        if left_values[left_index]<right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index+=1
        else:
            sorted_values.append(right_values[right_index])
            right_index+=1
        
    sorted_values.append(left_values[left_index:])
    sorted_values.append(right_values[right_index:])

    return sorted_values




