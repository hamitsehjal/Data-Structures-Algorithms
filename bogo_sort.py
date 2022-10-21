
import random


def bogo_sort(list):
    while (isSorted(list)==False):
        random.shuffle(list)
    
    return list


def isSorted(list):

    for i in range(len(list)-1):
        if(list[i]>list[i+1]):
            return False
        
        return True



