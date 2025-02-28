# Binary Search

1.  Decide the search space.(`lo`  and  `hi`  will be initialized accordingly)
2.  Find a monotonic function which increases or decreases with the input. It can take one of the two forms (`false`  followed by  `true`  or  `true`  followed by  `false`)
3.  decide whether  `lo`  holds the answer or  `hi`  holds the answer. If it is a  `minimization`  problem (`FFFFTTT`) then hi holds the answer. If it is a  `maximization`  problem (`TTTFFFF`) then  `lo`  holds the answer.

*Usually, coming up with a monotonic function is the most crucial steps.*


Minimization Problem
- monotonically increasing function
- (False , False, False,...., True, True, True) = False -> True
- Finding the first true

Maximization Problem
- monotonically decreasing function
- (True, True, True, ..., False, False, False) = True -> False
- Finding the last true


## Choosing the Right Predicate
When approaching a binary search problem, choosing the right predicate is crucial. Here’s how to figure it out:

### 1. Understand the Problem’s Goal

-   **Identify the target or condition:**  
    Read the problem carefully and determine what exactly you’re trying to find. Is it a boundary point, an insertion index, or something else?
    
-   **Example:**  
    For the “search insert position” problem, you want to find the smallest index where the array element is not less than the target.
    

### 2. Determine What Condition Splits the Search Space

-   **Find a clear yes/no (boolean) condition:**  
    The predicate should clearly answer a binary question that divides the search space into two parts.
    
    -   **For instance:** In the “search insert position” problem, ask: “Is the current element greater than or equal to the target?”
-   **Ensure Monotonicity:**  
    Verify that once the predicate returns `True` (or `False`), it continues to do so for all subsequent values in one direction.
    
    -   **Monotonic Increasing (False → True):**  
        Before the answer, the predicate is `False`. At the answer and beyond, it becomes `True` (and stays `True`).
    -   **Monotonic Decreasing (True → False):**  
        The opposite pattern, where it starts as `True` and then becomes `False` and stays that way.

### 3. Connect the Predicate to the Answer

-   **Check how the predicate relates to the solution:**  
    Decide whether you’re looking for the first occurrence of `True` (minimization) or the last occurrence of `True` (maximization).
    -   In our “search insert position” example, since you’re looking for the first index where the element is at least the target, the predicate is designed to switch from `False` (element < target) to `True` (element ≥ target).

### 4. Validate the Predicate’s Behavior

-   **Test with examples:**  
    Consider a small, sorted array and simulate the predicate on each element. Does it change value only once? Does it split the array as expected?
    
-   **Refine if necessary:**  
    If the predicate isn’t consistently monotonic (i.e., it doesn’t switch just once), rethink the condition or the interpretation of the problem.
    

### Summary Example:

For the “search insert position” problem:

-   **Problem Goal:** Find the smallest index where the array element is ≥ target.
-   **Predicate:** `arr[i] >= target`
-   **Behavior:**
    -   For all indices where `arr[i] < target`, the predicate returns `False`.
    -   Starting at the insertion point, `arr[i] >= target` becomes `True` and remains so.
-   **Conclusion:** This is a monotonic increasing scenario (False → True), which fits perfectly with binary search.

By following these steps, you can systematically choose a predicate that not only meets the problem’s requirements but also ensures the binary search algorithm works correctly.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg5NDgzODA3NCwxNDU4NjYyNzEyXX0=
-->