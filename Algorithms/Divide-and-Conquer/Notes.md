
## Farm-Plot Example
In the **Farm example** why did author choose `when one side is multiple of other` as the base case???


It simplifies the problems and provides a clear stopping condition. Explained below:

1. **Simplicity**: The base case should be the simplest possible scenario to solve. In this problem, `having one side as multiple of another` simplifies the `division of land` because you can `create square plots of equal size without any remainder`.

2. **Clear Stopping condition**: The base case should also provide a clear stopping condition. When one side is multiple of another, you have reached a situation, where you `don't need to divide the land further`. You can simply create 2 equal sized square plots of largest possible size and stop recursing.

3. **Efficiency**: This base case can lead to a more efficient solution as you `don't have to deal with partial slots or remainder`, which can complicate the algorithm.

## Merge-Sort 
```python
def merge_sort(arr):
    """
    Sorts a list using the Merge Sort algorithm.

    Merge Sort is a divide-and-conquer algorithm. It works by recursively
    dividing the input list into smaller sublists, sorting the sublists,
    and then merging the sorted sublists back together.

    Args:
        arr: The list to be sorted.

    Returns:
        A new list containing the sorted elements of arr.
    """
    # Base case: If the list has one or zero elements, it's already sorted.
    if len(arr) <= 1:
        return arr

    # 1. Divide: Split the list into two halves.
    mid = len(arr) // 2  # Find the middle index
    left_half = arr[:mid]  # Create the left sublist
    right_half = arr[mid:] # Create the right sublist

    # 2. Conquer: Recursively sort the two halves.
    #    This is where the recursion happens. We keep splitting the lists
    #    until we reach the base case (lists of size 0 or 1).
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # 3. Combine: Merge the sorted halves into a single sorted list.
    #    This is the crucial step where we combine the sorted sublists
    #    in a way that maintains the sorted order.
    return merge(sorted_left, sorted_right)

def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left: The first sorted list.
        right: The second sorted list.

    Returns:
        A new list containing all elements from left and right, sorted.
    """
    merged = []  # Initialize an empty list to store the merged result
    left_index = 0  # Index to track the current element in the left list
    right_index = 0 # Index to track the current element in the right list

    # Compare elements from both lists and add the smaller one to the merged list.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left list (if any).
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Add any remaining elements from the right list (if any).
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged  # Return the new sorted list



```
## Recap
1. D&C works by breaking down the problem into smaller and smaller pieces. If you are using D&C on a list, the `base case` is probably an empty list or list with just 1 element
2. If you are implementing QuickSort, choose `random element` as pivot. The Average Runtime of QuickSort is `O(n log n)`
3. The `Constant` in Big O Notation can matter sometimes. Classic Example: MergeSort Vs QuickSort - that's why QuickSort is faster than MergeSort
4. The `Constant` almost never matters for Simple search vs Binary Search. `O( log n)` is so much faster than `O(n)` as the list size increases.
    

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4Mzc4NTYyOF19
-->