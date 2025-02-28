# Binary Search

## When to use binary search

Binary search divides the search space into half until we reach the result. As a result the time performance of binary search (`log n`) is considerably better than linear search (`n`). This means where linear search will take  `10^6`  steps, binary search will do it in only  `17`  steps.
## Template

I try to convert each binary search related problem in either of the two formats - minimization problem (minimize  `x`  such that  `condition(x)`  is  `true`) or maximization problem (maximize  `x`  such that  `condition(x)`  is  `true`). In both the cases we construct the  `condition(x)`  such that it is  `true`  for our answer.

```

// minimize x such that condition(x) is true
function binarySearch(arr) {
  // decide what is the search space
  // hi should be able to take all possible values in the search space
  // lo points to an invalid value (the negative case of the if condition)
  let lo = -1, hi = arr.length;
  while (lo + 1 < hi) {
    let mid = lo + Math.floor((hi - lo) / 2);
    if (condition(arr, mid)) {
      hi = mid
    } else {
      lo = mid;
    }
  }

  // in minimization template, hi contains the return index
  return hi;
}

// maximize x such that condition(x) is true
function binarySearch(arr) {
  // decide what is the search space
  // lo should be able to take all possible values in that search space
  // hi points to an invalid value (the negative case of the if condition)
  let lo = -1, hi = arr.length;
  while (lo + 1 < hi) {
    let mid = lo + Math.floor((hi - lo) / 2);
    if (condition(arr, mid)) {
      lo = mid;
    } else {
      hi = mid;
    }
  }

  // in maximization template, lo contains the return index
  return lo;
}

function condition(arr, idx) {
  // some condition on arr[idx]
  // return true or false
  return true;
}
```

#### Example

**Minimization**  - Find  _first occurrance_  of an element in a sorted array with duplicates.  
**Maximization**  - Find  _last occurrance_  of an element in a sorted array with duplicates.

## Notes

If you look at both the templates carefully. We can make the following  **observations**:

In minimization template,  `hi`  contains the final answer.  
In maximization template,  `lo`  contains the final answer.

In each of the template, the variable that contains the final answer (`hi`  for minimization /  `lo`  for maximization), should be able to take all possible values in the search space. In other words, one variable always holds the answer (or the valid value) and the other variable holds the invalid value.

When we exit from  `while`  loop,  `lo`  and  `hi`  are adjacent to each other.  `(lo + 1 < hi)`  will not be true when  `lo + 1 === hi`.

The  `while`  loop condition guarantees that you always will have at least three values in the search space (`lo`,  `mid`,  `hi`). Although, the way we initialize the values for  `lo`  and  `hi`, only one of them holds a valid value at any point in time.

Binary search usually works for sorted arrays. But don't make the mistake of assuming it works  _only_  on sorted arrays. A bigger question to ask is if the search space can be  `perceived as`  or  `converted into`  a monotonically increasing / decreasing function. Typically, you'll be asked to return a minimum value that satisfies a given condition or the maximum value that satisfies a given condition. We'll learn it as we go through the examples below.

1.  Decide the search space.(`lo`  and  `hi`  will be initialized accordingly)
2.  Find a monotonic function which increases or decreases with the input. It can take one of the two forms (`false`  followed by  `true`  or  `true`  followed by  `false`)
3.  decide whether  `lo`  holds the answer or  `hi`  holds the answer. If it is a  `minimization`  problem (`FFFFTTT`) then hi holds the answer. If it is a  `maximization`  problem (`TTTFFFF`) then  `lo`  holds the answer.

*Usually, coming up with a monotonic function is the most crucial steps.*

A short summary to remember
```
Minimization Problem
- monotonically increasing function
- (False , False, False,...., True, True, True) = False -> True
- Finding the first true

Maximization Problem
- monotonically decreasing function
- (True, True, True, ..., False, False, False) = True -> False
- Finding the last true
```

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
eyJoaXN0b3J5IjpbLTUxMzM3MDUwNiwtNTg2ODI0NTYsMTQ1OD
Y2MjcxMl19
-->