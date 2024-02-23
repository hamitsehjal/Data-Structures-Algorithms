"""Depth First Traversal using Stack"""

class TreeNode:
    '''Class to represent a single node of a Binary Tree'''
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def depth_first_search(root):
    '''
    # Pseudocode
    1. Intialize a stack with the root of the tree
    2. Iterate over the stack until it is not empty
    3. Pop of the top element and print it
    4. Check if the top element has left or right child
    5. Push right child first and then left child to the stack (We are prioritizing the left subtree)
    6. Continue Iteration
    '''
    
    stack=[root]
    while stack:
        node = stack.pop()
        print(f"{node.val} -> ",end = "")
        left = node.left
        right = node.right
        if right:
            stack.append(right)
        if left:
            stack.append(left)
        
