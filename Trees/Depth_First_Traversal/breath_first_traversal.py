from typing import Optional,List
from collections import deque
from tree_node import TreeNode as Node

def bfs(root: Optional[Node]) -> List[str]:
    if root == None:
        return []
    
    queue = deque([root])
    ans = [] 
    while queue:
        # check the lenght of the queue once per level
        nodes_in_current_level=len(queue)
        for _ in range(nodes_in_current_level):
            # pop off the first element
            curr = queue.popleft()
            ans.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

    return ans
        
    

