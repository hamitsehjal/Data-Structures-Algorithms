Topological sorting can be tricky when setting up the problem, especially when dealing with dependencies and prerequisites. Let me help you understand how to structure this problem effectively.

In this build order problem, there are two ways to represent the graph:

1.  **Dependencies representation**: Node → List of nodes it depends on
2.  **Dependents representation**: Node → List of nodes that depend on it

The second approach (dependents) is typically more intuitive for topological sorting because:

-   It directly represents the "comes before" relationship
-   It makes identifying nodes with no prerequisites easier (these are your starting points)
-   It aligns well with the standard topological sort algorithm

Let's break down how to approach this specific problem:

## Step 1: Understand the Input Format

-   Dependencies like (a, d) mean "a must be completed before d"
-   Or in other words, "d depends on a"

## Step 2: Build the Graph

For each dependency (x, y):

-   x is a prerequisite for y
-   y depends on x
-   We add y to the list of nodes dependent on x

```
// Graph structure where each node points to nodes that depend on it
a → [d]
f → [b, a]
b → [d]
d → [c]
e → []  // e has no dependents

```

## Step 3: Track In-Degrees

We also need to track the number of prerequisites (dependencies) each node has:

```
a: 1 (depends on f)
b: 1 (depends on f)
c: 1 (depends on d)
d: 2 (depends on a and b)
e: 0 (no dependencies)
f: 0 (no dependencies)

```

## Step 4: Apply Topological Sort

1.  Start with nodes that have no prerequisites (in-degree = 0): e, f
2.  Process each node, decrementing the in-degree of its dependents
3.  When a node's in-degree becomes 0, add it to the queue

Here's how to implement this solution:

## Why This Structure Works Well

The key insight is understanding which direction the graph edges should point:

1.  When we say (a, d) means "a must be completed before d", in the graph:
    
    -   We add an edge from a → d
    -   But in the adjacency list, we're saying "a has d as a dependent"
2.  This approach makes finding our starting points simple:
    
    -   Nodes with no prerequisites (in-degree = 0) are our starting points
    -   As we process each node, we "remove" it from the graph by decrementing the in-degree of its dependents
3.  The topological sort naturally gives us the correct build order:
    
    -   Start with projects having no dependencies
    -   Gradually include projects as their dependencies are satisfied

## Common Confusion Points

-   The direction of edges might feel reversed from how we think about dependencies
-   Remember that we're building a graph where each node points to what comes after it, not what comes before it
-   The in-degree count is what helps us track prerequisites

When implementing, it helps to think of it as:

-   "Who is waiting for me to finish?" rather than "Who am I waiting for?"

Would you like me to explain any specific part of this approach in more detail?

That's an excellent question about the cycle detection logic! Let's break down why this condition works for identifying cycles in a topological sort.

## Why `buildOrder.length !== projects.length` Indicates a Cycle

When we perform a topological sort, we start with nodes that have no prerequisites (in-degree of 0) and gradually process nodes as all their prerequisites are completed. If there's a cycle in the graph, this creates a paradoxical situation where certain nodes can never be processed.

### How the Algorithm Works

1.  We start by adding all nodes with in-degree 0 to our queue
2.  We process each node in the queue:
    -   Add it to our build order
    -   Decrement in-degree for all its dependents
    -   If any dependent's in-degree becomes 0, add it to the queue
3.  We continue until the queue is empty

### Why Cycles Prevent Complete Processing

Let's consider a simple cycle: A depends on B, B depends on C, and C depends on A.

-   None of these nodes will ever have an in-degree of 0 during our algorithm
-   A can't start until C is done
-   C can't start until B is done
-   B can't start until A is done

This creates a catch-22 situation where none of the nodes in the cycle can ever be added to our queue, meaning they'll never be added to our build order.

### The Proof

1.  If there is no cycle:
    
    -   Every node in a directed acyclic graph (DAG) can be topologically sorted
    -   Our algorithm will eventually process all nodes
    -   Therefore, `buildOrder.length` will equal `projects.length`
2.  If there is a cycle:
    
    -   At least one node in the cycle will never have its in-degree reach 0
    -   This node (and potentially others in the cycle) will never be added to the queue
    -   Therefore, `buildOrder.length` will be less than `projects.length`

This is why checking if we've processed all nodes (`buildOrder.length === projects.length`) is a simple and effective way to detect cycles.

## Visual Example

Let's see this with a small example containing a cycle:

```
Projects: A, B, C
Dependencies: (A, B), (B, C), (C, A)

```

1.  Initialize:
    
    -   Graph: A→[B], B→[C], C→[A]
    -   In-degrees: A:1, B:1, C:1
    -   Queue: [] (empty, since no node has in-degree 0)
    -   BuildOrder: [] (empty)
2.  Since our queue starts empty (no node with in-degree 0), we can't process any nodes
    
3.  Our algorithm ends with buildOrder.length = 0, which is less than projects.length = 3
    
4.  We conclude there's a cycle
    

In contrast, if we had a valid DAG, there would always be at least one node with in-degree 0 at the start, and we'd eventually process all nodes.

## Alternative Cycle Detection Approaches

While this method works, there are other ways to detect cycles:

1.  **DFS with coloring**: Mark nodes as "visiting" and "visited" to detect back edges
2.  **Track visited counts**: If we've visited fewer nodes than total after the algorithm, there's a cycle
3.  **Explicit cycle finding**: When the queue becomes empty but unprocessed nodes remain

The approach in your code is elegant because it piggybacks on information we already have from the topological sort without requiring additional tracking.

Does this explanation help clarify why this condition guarantees cycle detection? Or would you like me to provide a more detailed example with our original problem?


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
eyJoaXN0b3J5IjpbMjA2MTM2NzE0OCwyMDY5MzkwNTEsNzE4ND
Q4NDc3XX0=
-->