'''Testing the depth first search '''
from depth_first_traversal import depth_first_search as dfs, TreeNode as Node

# Define Nodes
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

# Connect nodes to form a tree
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

dfs(a)
