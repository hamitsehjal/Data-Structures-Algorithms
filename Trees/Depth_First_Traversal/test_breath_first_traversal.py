'''Testing the Breath First Traversal'''
import pytest

from tree_node import TreeNode as Node
from breath_first_traversal import bfs

# Define nodes
a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('e')
f=Node('f')

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f

@pytest.fixture
def binary_tree_several_nodes():
    '''returns a binary tree with several nodes'''
    return a

def test_binary_tree_with_several_nodes(binary_tree_several_nodes):
    '''Breath first traversal using Queue on a binary tree with several nodes'''
    ans = ['a','b','c','d','e','f']
    assert ans == bfs(binary_tree_several_nodes)
