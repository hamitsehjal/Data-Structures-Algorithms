"""Depth First Traversal Implementation using Recursion"""
from typing import Optional,List
from tree_node import TreeNode as Node

def depth_first_traversal(root:Optional[Node]) -> List[str]:
    """
        1. Handle the Base case. (if current node == null)
        2. Do some logic on the current node
        3. Make a recursive call on the current node's children
        4. return the Result
    """
    ans = []
    if root == None:
        return []
    
    ans.append(root)
    # prioritizing left subtree
    left_values = depth_first_traversal(root.left)
    right_values = depth_first_traversal(root.right)

    return [root.val] + left_values[:] + right_values[:] 
     
