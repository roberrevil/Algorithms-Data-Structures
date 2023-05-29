## Prim's Algorithm

Prim's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a weighted undirected graph. A minimum spanning tree is a subgraph that connects all the vertices of the original graph with the minimum total weight.

The steps involved in Prim's algorithm are as follows:

1. **Input:** Take an input weighted undirected graph `G`.
2. **Initialization:** Select a starting vertex `start` from `G` and create an empty set `MST` to store the edges of the minimum spanning tree and a list `key` to store the minimum weights of each vertex.
3. **Key Initialization:** Initialize the `key` list with a large value for all vertices except `start`. Set the `key` value of `start` to 0.
4. **Iterate:** Repeat the following steps until all vertices are included in the MST.
5. **Minimum Key:** Find the vertex `v` with the minimum `key` value that is not already part of the MST.
6. **Add Edge:** Add the edge `(v, parent[v])` to the MST, where `parent[v]` is the parent vertex of `v` in the MST.
7. **Update Key:** Update the `key` values of the adjacent vertices of `v` if they have a smaller weight than their current `key` value.
8. **Output:** Return the MST represented by the set of edges in `MST`.

Here is a Python implementation of Prim's algorithm:

```python
import heapq

def prim(graph, start):
    MST = set()
    key = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    key[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        weight, u = heapq.heappop(pq)
        
        if u in MST:
            continue
        
        MST.add(u)
        
        for v, w in graph[u]:
            if v not in MST and w < key[v]:
                key[v] = w
                parent[v] = u
                heapq.heappush(pq, (w, v))
    
    return MST
```

In the above implementation, `graph` is a dictionary representing the weighted undirected graph, where the keys are the vertices and the values are lists of tuples `(v, w)`, representing an edge between `u` and `v` with weight `w`. The `start` parameter is the starting vertex.

The algorithm maintains a priority queue `pq` to keep track of the vertices with their respective weights. It repeatedly selects the vertex with the minimum weight (`u`) and adds it to the MST. It then updates the `key` values of its adjacent vertices if necessary. The process continues until all vertices are included in the MST.

Finally, the function returns the set of edges in the minimum spanning tree (`MST`).

The time complexity of Prim's algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.