# Advanced Graphs

## Topological Sort

**Topological sort arranges the nodes in a directed graph so that if there's an edge from A to B, then A appears before B in the final ordering.**
Or even more simply: **It's like creating a to-do list where you do all the prerequisites before the things that depend on them.**

For example, if you're getting dressed and you have dependencies like "put on socks before shoes" and "put on underwear before pants," a topological sort would give you a valid order like: underwear → socks → pants → shoes.

1. The key insight is that it only works on directed acyclic graphs (DAGs) - graphs with no cycles. If there were cycles (like A depends on B, B depends on C, and C depends on A), then there'd be no valid ordering possible.

### Modeling edges in topological Sort
The standard convention is to direct edges from **dependency → dependant.** This way, when you do a topological sort, dependencies naturally appear before dependants in the ordering.

So if task B depends on task A, you draw the edge as: **A → B**

This makes intuitive sense because:

-   The edge represents "A must come before B"
-   In the topological ordering, A will appear before B
-   The direction of the edge matches the direction of time/precedence

**Example:** If you're modeling course prerequisites:

-   "Calculus I must be taken before Calculus II"
-   Edge: Calculus I → Calculus II
-   Topological sort result: [...Calculus I...Calculus II...]

Some people initially think to model it backwards (dependant → dependency) because they think "B depends on A, so draw B → A." But this would break topological sort since you'd get B before A in the ordering, which is wrong.

So yes, always model it as **dependency → dependant**, and topological sort will give you the correct ordering where all dependencies come before the things that need them.

### Structing a Topological Sort Problem!!
 *Question: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error. 
 EXAMPLE
 Input: projects: a, b, c, d, e, f 
 dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) 
 Output: f, e, a, b, d, c*
```python
"""
Topological Sort 
dependency -> dependant 

1. Khan's Algorithm (BFS Based)
- compute indegree of each node (make sure you model the edge as dependency -> dependant)
- initialize a queue with nodes that have 0 indegree
- iterate while the queue is not empty
  - deque a node, add it to the topological order
  - iterate through all the neighbors of this node
    - decremnt indegree of each neibhor
    - check if indegree is 0,
      if yes, enqueue this neighbor 

- if len(topo_order) == number of nodes:
  # good, we got the topological order
- else:
  Cycle Detected
"""
from collections import deque

def topo_sort(edges,nodes):
  in_degree = {u: 0 for u in nodes}
  graph = {u: [] for u in nodes} # mapping a node to its neighbor
  
  # build a graph based on edges
  for u,v in edges:
    # u(dependency) --> v(depedant)
    graph[u].append(v)
    in_degree[v] += 1
  
  queue = deque([u for u in in_degree if in_degree[u] == 0])
  topo_order = []
  
  while queue:
    node = queue.popleft()
    topo_order.append(node)
    
    for nei in graph[node]:
      in_degree[nei] -= 1 
      if in_degree[nei] == 0:
        queue.append(nei)
  
  if len(topo_order) != len(nodes):
    raise Exception("Cycle Detected")
  else:
    return topo_order
  
  

projects = ['a','b','c','d','e','f']
dependencies = [['a','d'],['f','b'],['b','d'],['f','a'],['d','c']]

print(topo_sort(dependencies,projects))
```

Great question! Here are the key patterns that scream "topological sort":

## Core Signal: **Ordering with Dependencies**

If you see any variation of "arrange things in order where X must come before Y," that's your main clue.

### Common Question Patterns:

**1. Course/Task Scheduling**

-   "Given course prerequisites, find a valid order to take courses"
-   "Order tasks where some tasks must be completed before others"
-   "Build system: compile files in correct order based on dependencies"

**2. "Possible/Impossible" Questions**

-   "Is it possible to complete all courses given these prerequisites?"
-   "Can all tasks be finished?"
-   (These often combine cycle detection with topological sort)

**3. Job/Process Sequencing**

-   "Factory: some processes must finish before others can start"
-   "Project management: order activities based on dependencies"

**4. Compilation/Build Problems**

-   "Given module dependencies, what's the build order?"
-   "Import statements create dependencies - find compilation order"

**5. Recipe/Assembly Instructions**

-   "Steps in a recipe where some ingredients must be prepared first"
-   "Assembly line where some parts must be ready before others"

### Red Flag Keywords to Watch For:

-   "prerequisites"
-   "dependencies"
-   "must come before"
-   "required order"
-   "valid sequence"
-   "finish before starting"
-   "cycle" (often need to detect cycles first)

### Quick Test:

Ask yourself: _"Can I draw this as a directed graph where edges represent 'must happen before' relationships?"_ If yes, topological sort is likely your answer.

The beauty is that once you recognize the pattern, the solution structure is almost always the same: build the graph, then topologically sort it.



# Minimum Spanning Trees
## Kruskal's Algorithm
```
"""
Kruskal's Algorithm - undirected connected weighted graph
1. Union-Find Data structure
2. Get all the edges as pair of (w,u,v)
3. Sort all the edges by weight. declare variable mst and weight to track the mst and its weight
4. iterate over sorted edges:
5. Check if union(u,v) returns true or false:
  if false, which mean we came across a cycle so we skip it
  else:
    update the mst array
    update the weight array
"""

class UnionFind:
  def __init__(self,n):
    self.parent = [i for i in range(n)]
    self.rank = [0]*n
  
  def find(self,u):
    """
    Find parent of the node u 
    """
    if self.parent[u] == u:
      return u 
    
    self.parent[u] = self.find(self.parent[u]) # path compression
    return self.parent[u]
  
  def union(self,u,v):
    """
    Merge sets containing u and v into one set 
    """
    pu = self.find(u)
    pv = self.find(v)
    
    if pu == pv:
      # cycle
      return False
    
    if self.rank[pu] > self.rank[pv]:
      self.parent[pv] = pu
    elif self.rank[pu] < self.rank[pv]:
      self.parent[pu] = pv
    else:
      self.parent[pv] = pu
      self.rank[pu] += 1
      
    return True
    

def findMST(num_vertices,edges):
  edges = sorted(edges,key=lambda x:x[2])
  mst = []
  total_weight = 0
  uf = UnionFind(num_vertices)
  
  for u,v,w in edges:
    
    if uf.union(u,v):
      mst.append([u,v,w])
      total_weight += w
    else:
      continue
  
  return mst
    

edges = [
    [0, 1, 4],  # Edge between vertex 0 and 1 with weight 4
    [0, 2, 8],  # Edge between vertex 0 and 2 with weight 8
    [1, 2, 2],  # Edge between vertex 1 and 2 with weight 2
    [1, 3, 5],  # Edge between vertex 1 and 3 with weight 5
    [2, 3, 3],  # Edge between vertex 2 and 3 with weight 3
    [2, 4, 6],  # Edge between vertex 2 and 4 with weight 6
    [3, 4, 9]   # Edge between vertex 3 and 4 with weight 9
]
num_vertices = 5

print(findMST(num_vertices,edges))

```


## Prim's Algorithm


### How to Recognize MST Problems in General

To identify MST problems in the future, look for these patterns:

-   **Connectivity Requirement**: The problem asks to connect all nodes/points in some way (e.g., roads, cables, or paths).
-   **Minimization of Cost**: The goal is to minimize the total cost (sum of edge weights) while ensuring all nodes are connected.
-   **Graph Representation**: The problem can be modeled as a graph, even if it’s disguised as a geometric or network problem (e.g., points on a plane, cities, or servers).
-   **No Cycles Implied**: The solution typically avoids redundant connections, suggesting a tree structure (n-1 edges for n vertices).
-   **Edge Weights**: Costs are associated with connections (e.g., distances, times, or other metrics), and the problem doesn’t restrict which nodes can connect (implying a dense or complete graph).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ4NTI3NDkzNCwxOTUyMzA1NzgzLC01Mj
gzODUzMjIsMjA2MTM2NzE0OCwyMDY5MzkwNTEsNzE4NDQ4NDc3
XX0=
-->