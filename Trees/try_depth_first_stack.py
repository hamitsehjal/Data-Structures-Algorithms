'''Testing the depth first search '''
from tree_node import TreeNode as Node
from depth_first_traversal_stack import depth_first_traversal as dfs_stack
from depth_first_traversal_recursion import depth_first_traversal as dfs_recursion

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

print("DEPTH FIRST TRAVERSAL - STACK IMPLEMENTATION") 
print("Test 01: Tree with just several nodes")
print(dfs_stack(a))
print("Test 02: Tree with just one node")
print(dfs_stack(f))
print("Test 03: Tree with two nodes")
print(dfs_stack(b))
print("Test 04: EMPTY Tree")
print(dfs_stack(None))



print("DEPTH FIRST TRAVERSAL - RECURSION IMPLEMENTATION") 
print("Test 01: Tree with just several nodes")
print(dfs_recursion(a))
print("Test 02: Tree with just one node")
print(dfs_recursion(f))
print("Test 03: Tree with two nodes")
print(dfs_recursion(b))
print("Test 04: EMPTY Tree")
print(dfs_recursion(None))


