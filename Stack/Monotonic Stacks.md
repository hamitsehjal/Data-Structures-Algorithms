
# Monotonic Stacks: Finding Next/Previous Greater/Smaller Elements

Monotonic stacks are powerful tools for efficiently solving problems related to finding the next or previous greater/smaller elements in an array. This document provides a comprehensive template and examples for various scenarios.

## What is a Monotonic Stack?

A monotonic stack maintains a specific order (either increasing or decreasing) among its elements. We focus on stacks of indices, not the array values themselves.

* **Strictly Increasing:** Each element is strictly greater than the previous one (e.g., `[1, 4, 5, 8, 9]`).
* **Non-decreasing:** Each element is greater than or equal to the previous one (e.g., `[1, 4, 5, 5, 8, 9, 9]`).
* **Strictly Decreasing:** Each element is strictly smaller than the previous one (e.g., `[9, 8, 5, 4, 1]`).
* **Non-increasing:** Each element is smaller than or equal to the previous one (e.g., `[9, 9, 8, 5, 5, 4, 1]`).

We assume the rightmost element is the top of the stack.

## Generic Template

```javascript
function buildMonoStack(arr) {
  let stack = [];

  for (let i = 0; i < arr.length; i++) {
    while (stack.length && arr[stack.at(-1)] OPERATOR arr[i]) {
      let stackTop = stack.pop();
      // Do something with stackTop (e.g., nextGreater[stackTop] = i)
    }

    if (stack.length) {
      // Do something with stack.at(-1) (e.g., previousGreater[i] = stack.at(-1))
    }

    stack.push(i);
  }

  // Stack maintains its monotonic property
}

```

**Notes:**

-   The stack stores indices of array elements.
-   The `OPERATOR` determines the stack's monotonicity (`>`, `>=`, `<`, `<=`).
-   Time complexity: O(n).
-   Space complexity: O(n).

## Finding Next and Previous Greater/Smaller Elements

### 1. Next Greater

JavaScript

```
function findNextGreaterIndexes(arr) {
  let stack = [];
  let nextGreater = new Array(arr.length).fill(-1);

  for (let i = 0; i < arr.length; i++) {
    while (stack.length && arr[stack.at(-1)] < arr[i]) {
      let stackTop = stack.pop();
      nextGreater[stackTop] = i;
    }
    stack.push(i);
  }
  return nextGreater;
}

```

-   Uses a non-increasing stack (type 4).
-   `<` operator for strictly greater.
-   `<=` operator would result in greater or equal.

### 2. Previous Greater

JavaScript

```
function findPreviousGreaterIndexes(arr) {
  let stack = [];
  let previousGreater = new Array(arr.length).fill(-1);

  for (let i = 0; i < arr.length; i++) {
    while (stack.length && arr[stack.at(-1)] <= arr[i]) {
      stack.pop();
    }
    if (stack.length) {
      previousGreater[i] = stack.at(-1);
    }
    stack.push(i);
  }
  return previousGreater;
}

```

-   Uses a strictly decreasing stack (type 3).
-   `<=` operator for strictly greater.
-   `<` operator would result in greater or equal.

### 3. Next and Previous Greater (Combined)

JavaScript

```
function findNextAndPreviousGreaterIndexes(arr) {
  let stack = [];
  let previousGreater = new Array(arr.length).fill(-1);
  let nextGreater = new Array(arr.length).fill(-1);

  for (let i = 0; i < arr.length; i++) {
    while (stack.length && arr[stack.at(-1)] <= arr[i]) {
      let stackTop = stack.pop();
      nextGreater[stackTop] = i;
    }
    if (stack.length) {
      previousGreater[i] = stack.at(-1);
    }
    stack.push(i);
  }
  return [previousGreater, nextGreater];
}

```

-   One of `nextGreater` or `previousGreater` will include equal elements.

### 4. Next Smaller

JavaScript

```
function findNextSmallerIndexes(arr) {
  let stack = [];
  let nextSmaller = new Array(arr.length).fill(-1);

  for (let i = 0; i < arr.length; i++) {
    while (stack.length && arr[stack.at(-1)] > arr[i]) {
      let stackTop = stack.pop();
      nextSmaller[stackTop] = i;
    }
    stack.push(i);
  }
  return nextSmaller;
}

```

-   Uses a non-decreasing stack (type 2).

### 5. Previous Smaller

JavaScript

```
function findPreviousSmallerIndexes(arr) {
  let stack = [];
  let previousSmaller = new Array(arr.length).fill(-1);

  for (let i = 0; i < arr.length; i++) {
    while (stack.length && arr[stack.at(-1)] >= arr[i]) {
      stack.pop();
    }
    if (stack.length) {
      previousSmaller[i] = stack.at(-1);
    }
    stack.push(i);
  }
  return previousSmaller;
}

```

-   Uses a strictly increasing stack (type 1).

### 6. Next and Previous Smaller (Combined)

JavaScript

```
function findNextSmallerIndexes(arr) {
  let stack = [];
  let previousSmaller = new Array(arr.length).fill(-1);
  let nextSmaller = new Array(arr.length).fill(-1);

  for (let i = 0; i < arr.length; i++) {
    while (stack.length && arr[stack.at(-1)] >= arr[i]) {
      let stackTop = stack.pop();
      nextSmaller[stackTop] = i;
    }
    if (stack.length) {
      previousSmaller[i] = stack.at(-1);
    }
    stack.push(i);
  }
  return [nextSmaller, previousSmaller];
}

```

## Summary


| Problem             | Stack Type                | Operator in While Loop | Assignment Position |
| :------------------ | :------------------------ | :--------------------- | :------------------ |
| Next Greater        | Decreasing (equal allowed) | `stackTop < current`   | Inside while loop   |
| Previous Greater    | Decreasing (strict)       | `stackTop <= current`  | Outside while loop  |
| Next Smaller        | Increasing (equal allowed) | `stackTop > current`   | Inside while loop   |
| Previous Smaller    | Increasing (strict)       | `stackTop >= current`  | Outside while loop  |




![image](https://assets.leetcode.com/users/images/3b666e9c-4200-4245-bce8-7d7e81649f8f_1659039679.8631365.png)


## Resources
- [Original LeetCode Post](https://leetcode.com/discuss/post/2347639/a-comprehensive-guide-and-template-for-m-irii/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU2NzMyOTc5OSwtMTcwMzYyODQ2MCwtMT
IzMzAwNDY1Niw1NjkwMzEyMzMsLTQ1MTI3ODAzNCwtMTc5NzEx
NjY4MSw0NDA5MjA1ODVdfQ==
-->