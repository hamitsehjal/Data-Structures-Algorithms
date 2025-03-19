# LinkedList
Main Techniques:
1. Fast and Slow Pointers
2. Reversing a LinkedList (Logic used is transferable)
3. Singly and Doubly LinkedList
4. Using auxillary data structure like *Hashmap* along with LinkedList. *Sometimes, you may map a key to a Node of LinkedList instead of value*. Watch out for those problems.

## Problems
1. [Reverse a LinkedList](https://leetcode.com/problems/reverse-linked-list/description/)
2. [Merge Two Sorted LinkedLists](https://leetcode.com/problems/merge-two-sorted-lists/description/)
3. [LinkedList Cycle](https://leetcode.com/problems/linked-list-cycle/description/)
4. [Reorder List](https://leetcode.com/problems/reorder-list/description/)


### Common Patterns

#### Fast and Slow Pointers

#### Reverse a LinkedList

#### How to create a Deep copy of a linked list

```python
def deepCopy(head):
    dummy = ListNode(-1)
    cur = dummy
    original = head
    
    while original:
        new_node = ListNode(original.val)
        cur.next = new_node
        cur = new_node
        original = original.next
    
    return dummy.next

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTU4OTEzNTcxXX0=
-->