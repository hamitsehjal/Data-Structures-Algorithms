from heapq import merge
from linked_list import LinkedList

def merge_sort(linked_list):
    """
    RETURNS a linked_list sorted in ascending order

    DIVIDE: divide the linked_list into sublists until we are left with sublists containing only one node
    CONQUIER: Recursively sort the sublists created in the previous step
    COMBINE: combine the sorted sublists created in the previous step
    """
    # (STOPPING CONDITION for Recursive function) If linked_list is empty or has only 1 element, return the linked_list
    if linked_list.size() <=1:
        return linked_list

    left_half,right_half=split(linked_list)

    left=merge_sort(left_half)
    right=merge_sort(right_half)

    return merge(left,right)

    