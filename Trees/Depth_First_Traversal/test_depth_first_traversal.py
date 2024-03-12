'''Testing the depth first search '''
import pytest

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


@pytest.fixture
def binary_tree_several_nodes():
    '''return a binary Tree with several nodes'''
    return a

@pytest.fixture
def binary_tree_two_nodes():
    '''return a binary Tree with exactly two nodes'''
    return c

@pytest.fixture
def binary_tree_one_node():
    '''return a binary Tree with one node'''
    return f

@pytest.fixture
def binary_tree_empty():
    '''return an empty binary Tree'''
    return None


def test_tree_using_stack_with_several_nodes(binary_tree_several_nodes):
    '''Depth First Traversal using stack for Tree with serveral nodes'''
    ans = ['a','b','d','e','c','f']
    assert ans == dfs_stack(binary_tree_several_nodes)

def test_tree_using_stack_with_two_nodes(binary_tree_two_nodes):
    '''Depth First Traversal using stack for Tree with exactly two nodes'''
    ans = ['c','f']
    assert ans == dfs_stack(binary_tree_two_nodes)     

def test_tree_using_stack_with_one_node(binary_tree_one_node):
    '''Depth First Traversal using stack for Tree with exactly one node'''
    ans = ['f']
    assert ans == dfs_stack(binary_tree_one_node)     

def test_tree_using_stack_with_zero_node(binary_tree_empty):
    '''Depth First Traversal using stack for Tree with Zero Nodes'''
    ans = []
    assert ans == dfs_stack(binary_tree_empty)     

def test_tree_using_recursion_with_several_nodes(binary_tree_several_nodes):
    '''Depth First Traversal using stack for Tree with serveral nodes'''
    ans = ['a','b','d','e','c','f']
    assert ans == dfs_recursion(binary_tree_several_nodes)

def test_tree_using_recursion_with_two_nodes(binary_tree_two_nodes):
    '''Depth First Traversal using stack for Tree with exactly two nodes'''
    ans = ['c','f']
    assert ans == dfs_recursion(binary_tree_two_nodes)     

def test_tree_using_recursion_with_one_node(binary_tree_one_node):
    '''Depth First Traversal using recursion for Tree with exactly one node'''
    ans = ['f']
    assert ans == dfs_recursion(binary_tree_one_node)     

def test_tree_using_recursion_with_zero_node(binary_tree_empty):
    '''Depth First Traversal using stack for Tree with Zero Nodes'''
    ans = []
    assert ans == dfs_recursion(binary_tree_empty)     

