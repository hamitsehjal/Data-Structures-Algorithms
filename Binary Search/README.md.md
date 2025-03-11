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
![comparison between minimization template and maximization template for binary search](https://assets.leetcode.com/users/images/0dae011f-bb67-48bc-a870-5662fa42e6a0_1659209465.9950979.png)
Binary search usually works for sorted arrays. But don't make the mistake of assuming it works  _only_  on sorted arrays. A bigger question to ask is if the search space can be  `perceived as`  or  `converted into`  a monotonically increasing / decreasing function. Typically, you'll be asked to return a minimum value that satisfies a given condition or the maximum value that satisfies a given condition. We'll learn it as we go through the examples below.

## Process
1.  Decide the search space.(`lo`  and  `hi`  will be initialized accordingly)
2.  Find a monotonic function which increases or decreases with the input. It can take one of the two forms (`false`  followed by  `true`  or  `true`  followed by  `false`)
3.  decide whether  `lo`  holds the answer or  `hi`  holds the answer. If it is a  `minimization`  problem (`FFFFTTT`) then hi holds the answer. If it is a  `maximization`  problem (`TTTFFFF`) then  `lo`  holds the answer.

*Usually, coming up with a monotonic function is the most crucial steps.*
![image](https://assets.leetcode.com/users/images/6b7e07ff-38fa-4dc7-8636-eda758e0a7e2_1659260190.2577953.png)
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

Yes, binary search problems can indeed be framed as either **minimization** or **maximization** problems based on how the condition changes across the search space. In **minimization**, you're typically looking for the first point where a condition becomes `True` in a sequence like `[False, False, ..., False, True, True, ..., True]`. In **maximization**, you're looking for the last point where a condition remains `True` in a sequence like `[True, True, ..., True, False, False, ..., False]`. For both types, there are general templates that guide how to set up the pointers, define the loop condition, and update the pointers. Below, I’ll outline these templates clearly, addressing your specific questions about initial pointer values, loop conditions, and pointer updates.

---

### **1. Minimization (Finding the First True)**

#### **Pattern**
- The condition starts as `False` and switches to `True` at some point, and you want the **smallest index** where the condition is `True`.

#### **General Template**
```python
def binary_search_min(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):  # Condition is True
            right = mid     # Look for an earlier True
        else:
            left = mid + 1  # Condition is False, look to the right
    return left  # Points to the first True
```

#### **Answers to Your Questions**
1. **Initial Values for `left` and `right`**:
   - `left = 0`: Start at the beginning of the array.
   - `right = len(arr) - 1`: Start at the end of the array. This assumes the answer lies within the array bounds. If the problem allows an insertion point beyond the array (e.g., at `len(arr)`), you could initialize `right = len(arr)`.

2. **While Loop Condition**:
   - Use `while left < right`. This ensures the pointers converge to a single point. When the loop ends, `left == right`, and this position is the answer.
   - Avoid `while left <= right` here because it requires extra care to avoid infinite loops and often needs an additional check after the loop.

3. **Pointer Updates**:
   - If `condition(mid)` is `True`: Set `right = mid`. This includes `mid` in the search space to check if there’s an earlier `True`.
   - If `condition(mid)` is `False`: Set `left = mid + 1`. Move past `mid` since we know everything at and before `mid` is `False`.

#### **Why It Works**
- When the condition is `True` at `mid`, we move `right` to `mid` to search the left half (including `mid`) for the earliest `True`.
- When the condition is `False`, we move `left` to `mid + 1` to search the right half.
- The loop ends with `left == right` at the smallest index where the condition is `True`.

#### **Example**
Finding the insertion point for a target in a sorted array (e.g., `[1, 3, 5, 6]`, target `5`):
- Condition: `arr[mid] >= target`.
- Result: Index `2` (first position where `arr[mid] >= 5`).

---

### **2. Maximization (Finding the Last True)**

#### **Pattern**
- The condition starts as `True` and switches to `False` at some point, and you want the **largest index** where the condition is `True`.

#### **General Template**
```python
def binary_search_max(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left + 1) // 2  # Bias towards the right
        if condition(mid):  # Condition is True
            left = mid      # Look for a later True
        else:
            right = mid - 1 # Condition is False, look to the left
    return left  # Points to the last True
```

#### **Answers to Your Questions**
1. **Initial Values for `left` and `right`**:
   - `left = 0`: Start at the beginning of the array.
   - `right = len(arr) - 1`: Start at the end of the array. This works when the answer is within the array bounds.

2. **While Loop Condition**:
   - Use `while left < right`. Like minimization, this ensures convergence to a single point (`left == right`), which is the answer.
   - The `left <= right` condition can work but risks infinite loops without careful pointer updates.

3. **Pointer Updates**:
   - If `condition(mid)` is `True`: Set `left = mid`. This includes `mid` in the search space to check for a later `True`.
   - If `condition(mid)` is `False`: Set `right = mid - 1`. Move before `mid` since everything at and after `mid` is `False`.

   **Note**: Use `mid = left + (right - left + 1) // 2` (bias towards the right) to avoid infinite loops when `left` and `right` are close.

#### **Why It Works**
- When the condition is `True` at `mid`, we move `left` to `mid` to search the right half (including `mid`) for the latest `True`.
- When the condition is `False`, we move `right` to `mid - 1` to search the left half.
- The loop ends with `left == right` at the largest index where the condition is `True`.

#### **Example**
Finding the last occurrence of a target in a sorted array with duplicates (e.g., `[1, 2, 2, 2, 3]`, target `2`):
- Condition: `arr[mid] <= target`.
- Result: Index `3` (last position where `arr[mid] == 2`).

---

### **Key Differences Between the Templates**
| Aspect                | Minimization (First True)          | Maximization (Last True)          |
|-----------------------|------------------------------------|------------------------------------|
| **Pattern**           | `False` → `True`                  | `True` → `False`                  |
| **Goal**              | Smallest index where `True`       | Largest index where `True`        |
| **Mid Calculation**   | `left + (right - left) // 2`      | `left + (right - left + 1) // 2` |
| **True Update**       | `right = mid`                     | `left = mid`                      |
| **False Update**      | `left = mid + 1`                  | `right = mid - 1`                 |

---

### **General Guidelines**
- **Initial Pointers**:
  - Typically, `left = 0` and `right = len(arr) - 1` work for most problems where the answer is within the array.
  - Adjust `right` to `len(arr)` if the answer could be outside (e.g., insertion at the end).

- **Loop Condition**:
  - `while left < right` is preferred for both templates because it’s simpler and ensures convergence without extra checks.
  - `while left <= right` can be used, but you must ensure proper pointer updates (e.g., `right = mid - 1` or `left = mid + 1`) to avoid infinite loops.

- **Pointer Updates**:
  - For minimization: `right = mid` (True), `left = mid + 1` (False).
  - For maximization: `left = mid` (True), `right = mid - 1` (False).

- **Post-Loop Check**:
  - After the loop, `left == right`. You may need to verify `condition(left)` to confirm it’s the correct boundary.

---

### **Conclusion**
These templates provide a reliable framework for solving binary search problems as either minimization or maximization tasks. By defining the condition appropriately and following the pointer initialization, loop condition, and update rules, you can efficiently find the first `True` or last `True` in any binary search scenario. Practice applying these templates to problems like finding insertion points, boundaries, or last occurrences, and you’ll see how versatile they are!
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjMyMDI0MzI2LC0xNzE3MjU2Mzk0LC01OD
Y4MjQ1NiwxNDU4NjYyNzEyXX0=
-->