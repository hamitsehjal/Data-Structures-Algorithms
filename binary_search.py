def binary_search(list,target):
    first=0
    last=len(list)-1
    
    while first<=last:
        mid_point=(first+last)//2
        
        if list[mid_point]==target:
            return mid_point
        elif list[mid_point]<target:
            first=mid_point+1
        else:
            last=mid_point-1
    
    return None

def verify(index):
    if(index is not None):
        print("Target Found at index:",index)
    else:
        print("Target Not Found!!")
        

numbers=[1,2,3,4,5,6,6,8,9,10]

result=binary_search(numbers,5)

verify(result)