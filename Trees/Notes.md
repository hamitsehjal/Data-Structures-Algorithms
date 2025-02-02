# Trees




When solving binary tree problems, understanding the **direction of data flow** (top-down via parameters vs. bottom-up via return values) is critical. Here’s a structured guide to help you decide:

---

### **1. Top-Down (Passing Data via Parameters)**
**Use when:**
- You need to track **state** along the path from the root to the current node (e.g., min/max values, accumulated sums, ancestor lists).
- The logic depends on **ancestor information** (e.g., "Is the current node greater than all its ancestors?").

**Examples:**
- **Max Ancestor Difference** (`maxAncestorDiff`): Track the current `max` and `min` values from ancestors.
- **Path Sum Problems**: Track the accumulated sum from the root to the current node.
- **Validating BST**: Pass down allowed value ranges (`low`, `high`).

**Code Pattern:**
```python
def dfs(node, param1, param2):
    # Process node using param1/param2 (e.g., update max/min)
    dfs(node.left, updated_param1, updated_param2)
    dfs(node.right, updated_param1, updated_param2)
```

---

### **2. Bottom-Up (Returning Data via Values)**
**Use when:**
- The solution depends on **subtree results** (e.g., height, subtree validity, subtree sums).
- You need to **aggregate results** from subtrees (e.g., "What’s the maximum path sum in the entire tree?").

**Examples:**
- **Tree Height**: Return the height of the subtree rooted at the current node.
- **Balanced Tree Check**: Return subtree height and whether it’s balanced.
- **Maximum Path Sum**: Return the maximum path sum that can be extended upward.

**Code Pattern:**
```python
def dfs(node):
    left_result = dfs(node.left)
    right_result = dfs(node.right)
    # Combine left_result and right_result
    return combined_result
```

---

### **3. Hybrid Approach (Both Directions)**
**Use when:**
- You need both **ancestor context** and **subtree results**.
- Example: **Lowest Common Ancestor (LCA)**:
  - Pass down target nodes (top-down).
  - Return whether the current subtree contains either target (bottom-up).

---

### **Key Tips for LeetCode-Style Problems**
1. **Identify the Problem Type:**
   - Does it ask about **paths** (e.g., "max difference along a path")? → **Top-down**.
   - Does it ask about **subtree properties** (e.g., "is the subtree balanced?")? → **Bottom-up**.

2. **Avoid Global Variables:**
   - Use return values and parameters to encapsulate state instead of `nonlocal` or global variables.

3. **Time/Space Tradeoffs:**
   - Top-down often requires passing copies of data (e.g., `ancestors.copy()`), which can lead to \(O(n^2)\) time/space.
   - Bottom-up is usually more efficient (e.g., \(O(n)\) for tree height).

4. **Example Decision Flow:**
   - **Problem:** *"Find the maximum value where a node is an ancestor of another."*
     - **Top-down:** Track `max` and `min` along the path.
     - **Bottom-up:** Not sufficient alone (needs ancestor context).
   - **Problem:** *"Check if the tree is symmetric."*
     - **Hybrid:** Compare left and right subtrees by passing mirrored nodes.

---

### **Practice Scenarios**
1. **Top-Down Example:**
   ```python
   # Track the maximum depth from root to leaf
   def maxDepth(root):
       def dfs(node, depth):
           if not node:
               return 0
           if not node.left and not node.right:
               return depth
           return max(dfs(node.left, depth+1), dfs(node.right, depth+1))
       return dfs(root, 1)
   ```

2. **Bottom-Up Example:**
   ```python
   # Check if the tree is balanced
   def isBalanced(root):
       def dfs(node):
           if not node:
               return (True, 0)
           left_balanced, left_h = dfs(node.left)
           right_balanced, right_h = dfs(node.right)
           balanced = left_balanced and right_balanced and abs(left_h - right_h) <= 1
           return (balanced, 1 + max(left_h, right_h))
       return dfs(root)[0]
   ```

---

### **Summary**
- **Top-down (parameters):** Use for path-specific state (ancestors, accumulated values).
- **Bottom-up (return values):** Use for subtree aggregation (heights, validity).
- **Hybrid:** Combine when both are needed (e.g., LCA).


## Binary Search Trees

[Understanding Binary Search ](https://akcoding.com/dsa/non-linear-data-structures/tree-data-structure/binary-search-tree/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbODk1MDM3MzkzLC00OTYxNjM3NDldfQ==
-->