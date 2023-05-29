# Depth-First Search (DFS)

Depth-First Search is a graph traversal algorithm that explores all the vertices of a graph by going as deep as possible along each branch before backtracking. DFS starts from a specified source vertex and visits all the vertices that are reachable from the source vertex.

The steps involved in the DFS algorithm are as follows:

1. **Input:** Take an input graph `G` and a source vertex `start`.
2. **Initialization:** Create an empty stack `stack` and an empty set `visited`.
3. **Push and Mark:** Push the `start` vertex onto the `stack` and mark it as visited by adding it to the `visited` set.
4. **Explore Neighbors:** Repeat the following steps until the `stack` is empty.
   - Pop a vertex `current` from the top of the `stack`.
   - Visit the `current` vertex and perform any desired operations.
   - Push all the unvisited neighbors of the `current` vertex onto the `stack` and mark them as visited.
5. **Output:** The DFS algorithm outputs the visited vertices in the order they were visited.

Here is a Python implementation of the DFS algorithm:

```python
def dfs(graph, start):
    stack = []
    visited = set()
    
    stack.append(start)
    visited.add(start)
    
    while stack:
        current = stack.pop()
        # Perform any desired operations on the current vertex
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    
    return visited
```

In the above implementation, `graph` is a dictionary representing the graph, where the keys are the vertices, and the values are lists of the neighboring vertices.

The algorithm uses a stack `stack` to store the vertices to be visited. It starts with the `start` vertex and adds it to the stack and the visited set. Then, it iteratively pops a vertex from the top of the stack, visits it, and pushes its unvisited neighbors onto the stack while marking them as visited.

Finally, the function returns the `visited` set containing all the vertices visited during the DFS traversal.

The time complexity of the DFS algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph.