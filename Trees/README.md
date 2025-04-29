# Depth-First Traversal for Binary Trees

## Node Definition

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Recursive Approach

### Pre-order Traversal (Root, Left, Right)

```python
def preorder_recursive(root):
    if not root:
        return
    print(root.val, end=' ')  # Process root
    preorder_recursive(root.left)  # Traverse left subtree
    preorder_recursive(root.right)  # Traverse right subtree
```

### In-order Traversal (Left, Root, Right)

```python
def inorder_recursive(root):
    if not root:
        return
    inorder_recursive(root.left)  # Traverse left subtree
    print(root.val, end=' ')  # Process root
    inorder_recursive(root.right)  # Traverse right subtree
```

### Post-order Traversal (Left, Right, Root)

```python
def postorder_recursive(root):
    if not root:
        return
    postorder_recursive(root.left)  # Traverse left subtree
    postorder_recursive(root.right)  # Traverse right subtree
    print(root.val, end=' ')  # Process root
```

## Iterative Approach

### Pre-order Traversal (Root, Left, Right)

```python
def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=' ')  # Process root
        if node.right:
            stack.append(node.right)  # Push right child
        if node.left:
            stack.append(node.left)  # Push left child
```

### In-order Traversal (Left, Root, Right)

```python
def inorder_iterative(root):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=' ')  # Process root
        current = current.right
```

### Post-order Traversal (Left, Right, Root)

```python
def postorder_iterative(root):
    if not root:
        return
    stack1, stack2 = [root], []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        print(stack2.pop().val, end=' ')
```

## Time and Space Complexity

- Time Complexity: O(n) for all traversals, where n is the number of nodes in the tree.
- Space Complexity:
  - Recursive: O(h) where h is the height of the tree (due to call stack).
  - Iterative: O(h) in the worst case, where h is the height of the tree.

## Key Points

1. Recursive approaches are more intuitive but may lead to stack overflow for very deep trees.
2. Iterative approaches use explicit stacks and are more memory-efficient for deep trees.
3. The order of processing (print) determines the type of traversal:
   - Pre-order: Process before recursing
   - In-order: Process between left and right recursion
   - Post-order: Process after recursing
4. For balanced trees, the space complexity is O(log n), but for skewed trees, it can be O(n).




# Trees (Solving with Recursion)
1. Base Case
2. Recursive Case
3. Flow of Information:
	1. Top Down : Pass information from parent to children (often as parameters)
	2. Bottom Up : Collect information from children to pass back to the parent (often as return values)

## Subtree-Thinking Approach
**Key points** to remember when thinking about subtrees:

1.  Identify the subproblem: What needs to be solved for each subtree?
2.  Combine results: How do you use the results from subtrees to solve the problem for the current node?
3.  Pass down or accumulate: Decide whether to pass information down to subtrees or accumulate results from subtrees.

This "subtree thinking" is powerful because it allows you to break complex tree problems into smaller, manageable pieces. Each recursive call solves the problem for a smaller subtree, and these solutions are combined to solve the problem for larger subtrees, ultimately solving it for the entire tree.



## Python's Strength
1. short-circuit evaluation in Python's logical OR operator. If a valid path is found in the left subtree, the right subtree won't be explored. [Path Sum Problem](https://leetcode.com/problems/path-sum/)



Sure! Here’s an extensive markdown note on the BST removal process, focusing on the thought process, step-by-step breakdown, and detailed explanations.

---

# Binary Search Tree (BST) Removal - Detailed Notes

## Overview

Removing a node from a Binary Search Tree (BST) involves three primary cases:
1. **Removing a leaf node** (a node with no children).
2. **Removing a node with one child**.
3. **Removing a node with two children**.

Each case requires a specific approach to ensure that the BST properties are maintained after the removal operation. The overall goal is to remove the target node while preserving the in-order sequence of the tree.

## Removal Process

### 1. Removing a Leaf Node

**Leaf Node**: A node with no children (`left == None` and `right == None`).

**Steps**:
- **Identify**: Check if the node to be removed is a leaf.
- **Delete**: Simply remove the node by setting its parent’s corresponding child pointer to `None`.

**Example**:
- **Initial BST**:
    ```
        5
       / \
      3   7
    ```
- **Remove node `3`** (a leaf node):
    - The code checks if the node has children. Since it doesn't, the node is removed.
- **Resulting BST**:
    ```
        5
         \
          7
    ```

### 2. Removing a Node with One Child

**Node with One Child**: A node with either a left child or a right child, but not both.

**Steps**:
- **Identify**: Determine if the node to be removed has only one child.
- **Bypass**: Replace the node with its single child by connecting the parent directly to the node’s child.

**Example**:
- **Initial BST**:
    ```
        5
       / \
      3   7
       \
        4
    ```
- **Remove node `3`** (has one child `4`):
    - The code checks if the node has children. It finds that `3` has a right child (`4`) and no left child.
    - Node `3` is bypassed by connecting `4` directly to the parent (`5`).
- **Resulting BST**:
    ```
        5
       / \
      4   7
    ```

### 3. Removing a Node with Two Children

**Node with Two Children**: A node with both a left child and a right child.

**Steps**:
1. **Find the In-Order Successor**: The smallest node in the right subtree of the node to be removed. This node will replace the value of the node to be removed, maintaining the BST properties.
2. **Replace the Node’s Value**: Copy the in-order successor’s value to the node to be removed.
3. **Recursively Remove the In-Order Successor**: The original in-order successor node must now be removed. It will either be a leaf node or have only one child.

**Example**:
- **Initial BST**:
    ```
         10
        /  \
       5    15
      / \   / \
     3   7 12  20
           \
            8
    ```
- **Remove node `5`** (has two children):
    - The code identifies that node `5` has two children (`3` and `7`).
    - **In-Order Successor**: The smallest node in the right subtree of `5` is `7`.
    - **Replacement**: Replace the value of `5` with `7`.
    - **Recursion**: The original `7` (now a duplicate) must be removed. The code makes a recursive call to remove `7` from the right subtree of `5`:
        - The subtree:
            ```
            7
             \
              8
            ```
        - The recursive call identifies that `7` has only one child (`8`).
        - Node `7` is bypassed by replacing it with `8`.
- **Resulting BST**:
    ```
         10
        /  \
       7    15
      / \   / \
     3   8 12  20
    ```

---

## Detailed Thought Process During Removal

### Step-by-Step Thought Process

1. **Identifying the Node to Remove**:
    - Traverse the tree comparing the key to be removed with each node’s value.
    - Move left if the key is smaller, or right if it is larger.

2. **Handling Different Cases**:
    - **Leaf Node**: Easiest case. Directly delete the node and set the parent’s child pointer to `None`.
    - **One Child**: Replace the node with its child by setting the parent’s pointer to the node’s single child.
    - **Two Children**: Requires careful handling:
        - **Find In-Order Successor**: This is the smallest node in the right subtree.
        - **Value Replacement**: Replace the node’s value with the in-order successor's value.
        - **Remove In-Order Successor**: Recursively remove the in-order successor node, which will now either be a leaf node or have one child.

3. **Maintaining the BST Properties**:
    - Ensure that the BST properties are preserved after removal:
        - Left subtree contains only nodes with values less than the node’s value.
        - Right subtree contains only nodes with values greater than the node’s value.
    - The in-order traversal of the tree should remain the same as before the removal (except for the removed node).

### Recursive Call Thought Process

- **Recursion on the Right Subtree**:
    - After replacing a node with its in-order successor, the original successor node must be removed.
    - The recursive call will follow the same steps to ensure the node is properly removed, whether it is a leaf node or has one child.

- **Handling Special Cases**:
    - When the in-order successor is the immediate right child of the node to be removed, special care is needed to handle the replacement correctly.

### Important Considerations

- **Edge Cases**:
    - Removing the root node.
    - Removing nodes in a very skewed BST (e.g., all nodes have only right children).
    - Ensuring that the function handles an empty tree (i.e., `root == None`).

- **Efficiency**:
    - Each removal operation should ideally run in O(h) time, where h is the height of the tree.
    - In a balanced BST, this would be O(log n), but in the worst case (completely unbalanced tree), it could degrade to O(n).

### Code Implementation
```
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    def remove(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self.remove(root.left, key)
        elif key > root.val:
            root.right = self.remove(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.find_min(root.right)

            # Copy the inorder successor's content to this node
            root.val = temp.val

            # Delete the inorder successor
            root.right = self.remove(root.right, temp.val)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

# Example Usage
bst = BST()
root = None
keys = [10, 5, 15, 3, 7, 12, 20, 8]

for key in keys:
    root = bst.insert(root, key)

print("Inorder traversal before deletion:")
bst.inorder(root)
print()

root = bst.remove(root, 5)

print("Inorder traversal after deletion:")
bst.inorder(root)
print()


```

### BST-Based Set Implementation

Time Complexity:

-   Best case (balanced tree): O(log n) for insert, remove, and contains
-   Worst case (unbalanced tree): O(n) for insert, remove, and contains


Space Complexity:

-   O(n) for storing n elements
```python
class SetNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

        
class BSTSet:
    def __init__(self):
        self.root = None
        self.size = 0
    
    # insert
    def insert(self,value)->bool:
        if not self.contains(value):
            self.root = self._insert_recursive(self.root,value)
            self.size += 1
            return True
        else:
            return False
        
    def _insert_recursive(self,node,val):
        if not node:
            return SetNode(val)
        if val < node.val:
            node.left = self._insert_recursive(node.left,val)
        else:
            node.right = self._insert_recursive(node.right,val)
        return node
    
    # remove
    def remove(self,value)->bool:
        if self.contains(value):
            # remove the value
            self.root = self._remove_recursive(self.root,value)
            self.size -= 1
            return True
        else:
            return False
    
    def _remove_recursive(self,node,val):
        if not node:
            return node
        if val < node.val:
            node.left = self._remove_recursive(node.left,val)
        elif val > node.val:
            node.right = self._remove_recursive(node.right,val)
        else:
            # Found the node
            # one child or no children
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                # Two children
                # Find the in-order sucessor
                cur = node.right
                while cur.left:
                    cur = cur.left

                # replace node's val with in-order successor
                node.val = cur.val
                
                # recursively remove the in-order successor
                node.right = self._remove_recursive(node.right,cur.val)
        
        return node
    
    # contains
    def contains(self,value)->bool:
        return self._contains_recursive(self.root,value)
    
    def _contains_recursive(self,node,val):
        if not node:
            return False
        if val < node.val:
            return self._contains_recursive(node.left,val)
        elif val > node.val:
            return self._contains_recursive(node.right,val)
        else:
            return True
    
    # is_empty
    def is_empty(self)->bool:
        return self.size == 0
    
    # size
    def size(self)->int:
        return self.size
```

### BST-Based Map
Time Complexity:

-   Best case (balanced tree): O(log n) for put, get, remove, and contains_key
-   Worst case (unbalanced tree): O(n) for put, get, remove, and contains_key


Space Complexity:

-   O(n) for storing n key-value pairs
```python
class MapNode:
    def __init__(self,val=0,left=None,right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

        
class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0
    
    # insert
    def put(self,key,value)->bool:
        if not self.contains(key):
            self.root = self._put_recursive(self.root,key,value)
            self.size += 1
            return True
        else:
            return False
        
    def _put_recursive(self,node,key,value):
        if not node:
            return MapNode(key,value)
        if key < node.key:
            node.left = self._put_recursive(node.left,key,value)
        elif key > node.key:
            node.right = self._put_recursive(node.right,key,value)
        else:
            # update value if it already exits
            node.val = val
        return node
    
    # remove
    def remove(self,key)->bool:
        if self.contains(key):
            # remove the key-value pair
            self.root = self._remove_recursive(self.root,key)
            self.size -= 1
            return True
        else:
            return False
    
    def _remove_recursive(self,node,key):
        if not node:
            return node
        if key < node.key:
            node.left = self._remove_recursive(node.left,key)
        elif key > node.key:
            node.right = self._remove_recursive(node.right,key)
        else:
            # Found the node
            # one child or no children
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                # Two children
                # Find the in-order sucessor
                cur = node.right
                while cur.left:
                    cur = cur.left

                # replace node's val with in-order successor
                node.val = cur.val
                node.key = cur.key
                
                # recursively remove the in-order successor
                node.right = self._remove_recursive(node.right,cur.key)
        
        return node
    
    # contains
    def contains(self,key)->bool:
        return self._contains_recursive(self.root,key)
    
    def _contains_recursive(self,node,key):
        if not node:
            return False
        
        if key < node.key:
            return self._contains_recursive(node.left,key)
        elif key > node.key:
            return self._contains_recursive(node.right,key)
        else:
            return True
    
    # is_empty
    def is_empty(self)->bool:
        return self.size == 0
    
    # size
    def size(self)->int:
        return self.size
```

## Binary Trees

## **1. Logarithmic Relationship Between Height and Nodes**

In a full binary tree, the height hhh grows logarithmically with the number of nodes nnn:  
h≈log⁡2(n+1)−1h \approx \log_2(n + 1) - 1h≈log2(n+1)−1

## **Why This Matters**

-   **Efficiency**: As nnn increases, the height grows slowly (logarithmically). For example:
    
    -   n=1,000n = 1,000n=1,000 → h≈9h \approx 9h≈9
        
    -   n=1,000,000n = 1,000,000n=1,000,000 → h≈19h \approx 19h≈19  
        This ensures operations like search, insertion, and deletion take O(log⁡n)O(\log n)O(logn) time, which is exponentially faster than linear time O(n)O(n)O(n)
-   **Balanced Structure**: Logarithmic height guarantees the tree remains "shallow," minimizing the number of comparisons or traversals needed to reach any node[3](https://www.andrew.cmu.edu/course/15-121/lectures/Trees/trees.html)[8](https://en.wikipedia.org/wiki/Binary_tree).
    

## **2. Leaf Nodes in a Full Binary Tree**

In a **perfect** full binary tree of height hhh:

-   **Leaf nodes**: 2h2^h2h
    
-   **Total nodes**: 2h+1−12^{h+1} - 12h+1−1
    

## **Why Leaves Are Half the Total Nodes**

-   The last level (height hhh) contains 2h2^h2h nodes, which is **double** the nodes at level h−1h-1h−1 (2h−12^{h-1}2h−1).
    
-   The total nodes are the sum of all levels:  
    20+21+⋯+2h=2h+1−12^0 + 2^1 + \dots + 2^h = 2^{h+1} - 120+21+⋯+2h=2h+1−1
    
-   Thus, leaves (2h2^h2h) are approximately **half** of the total nodes:  
    2h2h+1−1≈12\frac{2^h}{2^{h+1} - 1} \approx \frac{1}{2}2h+1−12h≈21[

## **Example**

For h=3h = 3h=3:

-   Total nodes: 23+1−1=152^{3+1} - 1 = 1523+1−1=15
    
-   Leaf nodes: 23=82^3 = 823=8
    
-   Ratio: 815≈53%\frac{8}{15} \approx 53\%158≈53%
    


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjYzNDIxODU0LC03NzEwNzQ4Ml19
-->