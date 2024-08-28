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
