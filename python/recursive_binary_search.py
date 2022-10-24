def recursive_binary_search(list,target):
    
    """If list is empty"""
    if(len(list)==0):
        return False
    else:
        midPoint=(len(list))//2
        
        if(list[midPoint]==target):
            return True
        else:
            if(list[midPoint]<target):
                return recursive_binary_search(list[midPoint+1:],target)
            else:
                "he slice operator [n:m] returns the part of the string starting with the character at index n and go up to but not including the character at index m"
                
                return recursive_binary_search(list[:midPoint],target)
                
                
            

def verify(result):
    print("TARGET FOUND!!: ",result)
    
    
numbers=[1,2,3,4,5,6,7,8,9,10]

result=recursive_binary_search(numbers,5)

verify(result)

result=recursive_binary_search(numbers,50)

verify(result)
    