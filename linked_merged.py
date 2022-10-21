from heapq import merge
from linked_list import LinkedList


def split(linked_list):
    """
    Takes in a linked_list and divides it up into two sublists by their mid points
    """

    if linked_list == None or linked_list.head is None:
        left_half = linked_list
        right_half = None

        return left_half, right_half

    else:
        size = linked_list.size()
        mid_point = size//2

        node_at_mid = linked_list.node_at_index(mid_point-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = node_at_mid.next_node

        # severing the connection at the midpoint
        node_at_mid.next_node = None

        return left_half, right_half


def merge(left, right):
    merged = LinkedList()
    """
        It sorts and combines the left and right linked list and returns the new combined version
    """
    # Assign a fake head to merged (empty linked list)
    merged.add(0)

    current = merged.head
    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head is None:
            # if left_head is None, it means we are past the tail of left linked list

            current.next_node = right_head
            right_head = right_head.next_node

        elif right_head is None:
            # if right_head is None, it means we are past the tail of right linked list
            current.next_node = left_head
            left_head = left_head.next_node

        else:
            left_data = left_head.data
            right_data = right_head.data

            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        current = current.next_node

    head = merged.head.next_node
    merged.head = head

    return merged


def merge_sort(linked_list):
    """
    RETURNS a linked_list sorted in ascending order

    DIVIDE: divide the linked_list into sublists until we are left with sublists containing only one node
    CONQUIER: Recursively sort the sublists created in the previous step
    COMBINE: combine the sorted sublists created in the previous step
    """
    # (STOPPING CONDITION for Recursive function) If linked_list is empty or has only 1 element, return the linked_list
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)
