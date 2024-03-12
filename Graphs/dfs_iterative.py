''' Depth-First Traversal Graphs - Iterative Solution '''

def dfs(graph,source):
    stack=[source] # initialize stack with source node
    while stack:
        node=stack.pop()
        print(node,end=" ")
        for neighbor in graph[node]:
            stack.append(neighbor)

example_graph={
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'f':[],
    'e':[]
}

dfs(example_graph,'a')
