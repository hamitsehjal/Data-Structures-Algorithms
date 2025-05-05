
# DFS Notes
## Exactly `n-1` Edges
This is an important observation in graph theory. When a problem specifies that you have:

-   n nodes (labeled from 0 to n-1)
-   exactly n-1 edges

This strongly suggests you're working with a **tree** structure.

A tree is a connected, undirected graph with no cycles. The key properties of a tree are:

1.  It is connected (there's a path between any two nodes)
2.  It has exactly n-1 edges when there are n nodes
3.  It has no cycles

This is why you're seeing this statement frequently in graph problems. When you have exactly n-1 edges for n nodes, the problem is typically hinting that you're dealing with a tree or asking you to construct/analyze a tree.

If we had:

-   Fewer than n-1 edges: The graph would be disconnected
-   More than n-1 edges: The graph would contain at least one cycle

Great follow-up questions! Let me address each one:

1.  **Binary trees vs. general trees**
    
    You're correct about the distinction. Let me clarify:
    
    -   A **general tree** as I described is typically represented as an undirected graph with no cycles.
        
    -   A **binary tree** in implementation is often represented as a directed graph where edges point from parents to children (via node.left and node.right references). However, the underlying mathematical structure is still considered undirected when discussing graph theory properties. The directedness comes from our implementation, not the abstract structure.
        
    -   In a binary tree implementation, we can only traverse from parent to children using the explicit pointers, unless we maintain parent pointers as well.
        
2.  **Fewer than n-1 edges**
    
    Yes, exactly. In a graph with n nodes:
    
    -   If you have fewer than n-1 edges and no cycles, the graph must have at least 2 separate connected components.
        
    -   This is because each connected component with k nodes requires at least k-1 edges to be connected. If you have multiple components, you can't connect all n nodes with fewer than n-1 edges.
        
3.  **Connectivity in directed vs. undirected graphs**
    
    You're absolutely right:
    
    -   In an **undirected connected component**, there is guaranteed to be a path between any two nodes. That's the definition of connectivity for undirected graphs.
        
    -   In a **directed connected component**, we have two different notions:
        
        -   **Weakly connected**: There's a path between any two nodes if we ignore the direction of edges.
            
        -   **Strongly connected**: There's a directed path from any node to any other node, respecting edge directions.
            
    
    So in a directed graph, being in the same connected component (weakly connected) doesn't guarantee you can reach any node from any other node. For that guarantee, you need a strongly connected component.

## There is an undirected tree with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

This means:

1.  You have a single undirected connected component (the tree)
2.  There is exactly one unique path between any two nodes in this tree
3.  There are no cycles (which is what makes it a tree rather than just any connected graph)
4.  Every node is reachable from every other node

So yes, there is guaranteed to be a path between any two nodes in this tree. This is a fundamental property of trees - they are connected graphs with no cycles.

This property is often leveraged in tree problems where you might need to find paths between nodes, perform traversals, or calculate distances within the tree structure.

-   A connected graph with n nodes requires at least n-1 edges to connect all nodes
-   Having exactly n-1 edges in a connected graph means there's no room for any cycles



You're asking a great, fundamental question. Let me clarify the definition of a tree more precisely.

In graph theory, a tree is defined by either of these equivalent definitions:

1.  A tree is a connected, acyclic (no cycles) undirected graph.
    
2.  A tree is a minimally connected undirected graph, meaning:
    
    -   It is connected (there's a path between any two nodes)
    -   If you remove any edge, it becomes disconnected

The absence of cycles is part of the core definition of what a tree is. This isn't something that follows from other properties - it's baked into the definition itself.

When someone says "undirected tree," they're explicitly referring to a graph structure that, by definition, has no cycles. This is similar to how when someone says "square," they're referring to a shape that, by definition, has four equal sides and four right angles.

So when a problem statement mentions an "undirected tree," it's directly telling you:

-   The graph is connected
-   The graph has no cycles

The statement about having n nodes and n-1 edges is actually a property that follows from these defining characteristics. In fact, we can prove that any connected, acyclic graph with n nodes must have exactly n-1 edges.

Does that help clarify why "undirected tree" immediately tells us there are no cycles?


# BFS Notes
- BFS guarantees the shortest path only **if you're exploring from all sources at once** — that's why a **multi-source BFS** is the correct and optimal approach here. Example - [542. 01 Matrix](https://leetcode.com/problems/01-matrix/description/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTQ0NzIxMzczLC0xMTg4Mjc4MTQ2LDEyOD
IyNzM0MTAsNDE4NzcwMjY1XX0=
-->