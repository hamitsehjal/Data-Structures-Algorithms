def linear_search(list,target):
    for i in range(0,len(list)):
        if (list[i]==target):
            return i
    
    return None
    

def verify(index):
    if(index is not None):
        print("Target Found at index:",index)
    else:
        print("Target Not Found!!")
        

numbers=[1,2,3,4,5,6,6,8,9,10]

result=linear_search(numbers,5)

verify(result)