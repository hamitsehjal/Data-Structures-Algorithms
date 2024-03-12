"""Depth First Traversal using Stack"""

def depth_first_traversal(root):
    '''
    # Pseudocode
    1. Intialize a stack with the root of the tree
    2. Iterate over the stack until it is not empty
    3. Pop of the top element and and add it to the returning array
    4. Check if the top element has left or right child
    5. Push right child first and then left child to the stack (We are prioritizing the left subtree)
    6. Continue Iteration
    '''
    if root == None:
        return []    
    stack=[root]
    nodes=[]
    while stack:
        node = stack.pop()
        nodes.append(node.val)
        # print(f"{node.val} -> ",end = "")
        left = node.left
        right = node.right
        if right:
            stack.append(right)
        if left:
            stack.append(left)
       
    return nodes 
