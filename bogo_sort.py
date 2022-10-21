
# -- This code snipped , if you want to pass file as an argument on command line
# import sys
# import load_numbers from load

# number=load_numbers(sys.argv[1])


import random


def bogo_sort(list):
    attempts=0
    while (isSorted(list)==False):
        random.shuffle(list)
        attempts+=1
    
    return list,attempts


def isSorted(list):

    for i in range(len(list)-1):
        if(list[i]>list[i+1]):
            return False
        
    return True



numbers=[5,4,2,12,23,1,9,34]
print("Before Algorithm: ",numbers)

print("After Algorithm: ",bogo_sort(numbers))