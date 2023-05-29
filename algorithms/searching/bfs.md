# Breadth-First Search (BFS)

Breadth-First Search is a graph traversal algorithm that explores all the vertices of a graph in breadth-first order, i.e., visiting all the vertices at the same level before moving to the next level. BFS starts from a specified source vertex and visits all the vertices that are reachable from the source vertex.

The steps involved in the BFS algorithm are as follows:

1. **Input:** Take an input graph `G` and a source vertex `start`.
2. **Initialization:** Create an empty queue `queue` and an empty set `visited`.
3. **Enqueue and Mark:** Enqueue the `start` vertex into the `queue` and mark it as visited by adding it to the `visited` set.
4. **Explore Neighbors:** Repeat the following steps until the `queue` is empty.
   - Dequeue a vertex `current` from the front of the `queue`.
   - Visit the `current` vertex and perform any desired operations.
   - Enqueue all the unvisited neighbors of the `current` vertex into the `queue` and mark them as visited.
5. **Output:** The BFS algorithm outputs the visited vertices in the order they were visited.

Here is a Python implementation of the BFS algorithm:

```python
from collections import deque

def bfs(graph, start):
    queue = deque()
    visited = set()
    
    queue.append(start)
    visited.add(start)
    
    while queue:
        current = queue.popleft()
        # Perform any desired operations on the current vertex
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    return visited
```

In the above implementation, `graph` is a dictionary representing the graph, where the keys are the vertices, and the values are lists of the neighboring vertices.

The algorithm uses a queue `queue` to store the vertices to be visited. It starts with the `start` vertex and adds it to the queue and the visited set. Then, it iteratively dequeues a vertex from the front of the queue, visits it, and enqueues its unvisited neighbors into the queue while marking them as visited.

Finally, the function returns the `visited` set containing all the vertices visited during the BFS traversal.

To use this function and perform a BFS traversal, you can do the following:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_vertex = 'A'
visited_vertices = bfs(graph, start_vertex)
print(visited_vertices)
```

This will output the visited vertices in the order they were visited:

```
{'A', 'B', 'C', 'D', 'E', 'F'}
```

The time complexity of the BFS algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph.