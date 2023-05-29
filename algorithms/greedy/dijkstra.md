# Dijkstra's Algorithm

Dijkstra's algorithm is a greedy algorithm used to find the shortest path from a single source vertex to all other vertices in a weighted directed graph. It assigns tentative distances to all vertices and gradually improves these distances by finding shorter paths. The algorithm guarantees to find the shortest path when all edge weights are non-negative.

The steps involved in Dijkstra's algorithm are as follows:

1. **Input:** Take an input weighted directed graph `G` and a source vertex `start`.
2. **Initialization:** Create a distance dictionary `dist` to store the shortest distances from `start` to each vertex in `G`. Set the distance of `start` to 0 and the distance of all other vertices to infinity.
3. **Priority Queue:** Create a priority queue `pq` to store the vertices and their corresponding distances. Insert `start` with distance 0 into `pq`.
4. **Iterate:** Repeat the following steps until `pq` is empty.
5. **Extract Min:** Extract the vertex `u` with the minimum distance from `pq`.
6. **Relaxation:** For each neighbor `v` of `u`, calculate the tentative distance from `start` to `v` through `u`. If this distance is smaller than the current distance stored in `dist[v]`, update `dist[v]` with the new smaller distance and update `v` in `pq` with the new distance.
7. **Output:** Return the `dist` dictionary containing the shortest distances from `start` to each vertex in `G`.

Here is a Python implementation of Dijkstra's algorithm:

```python
import heapq

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    return dist
```

In the above implementation, `graph` is a dictionary representing the weighted directed graph, where the keys are the vertices and the values are lists of tuples `(v, w)`, representing an edge from `u` to `v` with weight `w`. The `start` parameter is the source vertex.

The algorithm maintains a priority queue `pq` to keep track of the vertices and their corresponding distances. It repeatedly selects the vertex with the minimum distance (`u`) from `pq` and relaxes its neighbors. If a shorter path is found to a neighbor `v`, its distance in the `dist` dictionary is updated, and `v` is inserted into `pq` with the new distance.

Finally, the function returns the `dist` dictionary containing the shortest distances from `start` to each vertex in the graph.

The time complexity of Dijkstra's algorithm is O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph.