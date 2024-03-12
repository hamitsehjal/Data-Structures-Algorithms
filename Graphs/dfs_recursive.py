"""Depth First Traversal - Recursion"""

def dfs(graph,source):
    '''print out the nodes of a graph in Depth-First Order'''
    print(source,end=" ")
    for neighbor in graph[source]:
        dfs(graph,neighbor)


example_graph={
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'f':[],
    'e':[]
}

dfs(example_graph,'a')

'''
in the above recursive solution, we don't have an explicit Base Case. Weird, huh?

What is a base case?
- case where DO NOT have any more recursive call
In the above function, we are iterating over all the neighbors. When the list of neighbors is empty, we
do not make any more recursive call and that acts as an implicit Base Case

'''
