# Kruskal's Algorithm

Kruskal's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a connected, weighted, undirected graph. A minimum spanning tree is a subgraph that connects all the vertices of the original graph with the minimum total weight.

The steps involved in Kruskal's algorithm are as follows:

1. **Input:** Take an input weighted undirected graph `G`.
2. **Initialization:** Create an empty set `MST` to store the edges of the minimum spanning tree.
3. **Sort Edges:** Sort all the edges of `G` in non-decreasing order of their weights.
4. **Iterate:** Iterate through each edge `(u, v)` in the sorted order.
5. **Check Cycle:** Check if adding the edge `(u, v)` to `MST` creates a cycle. If adding the edge does not create a cycle, add it to `MST`.
6. **Output:** Return the `MST` represented by the set of edges.

Here is a Python implementation of Kruskal's algorithm:

```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            elif self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

def kruskal(graph):
    num_vertices = len(graph)
    disjoint_set = DisjointSet(num_vertices)
    edges = []
    mst = set()
    
    for u in range(num_vertices):
        for v, weight in graph[u]:
            edges.append((weight, u, v))
    
    edges.sort()
    
    for edge in edges:
        weight, u, v = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.add((u, v))
    
    return mst
```

In the above implementation, `graph` is a dictionary representing the weighted undirected graph, where the keys are the vertices and the values are lists of tuples `(v, w)`, representing an edge between `u` and `v` with weight `w`.

The algorithm uses a `DisjointSet` class to keep track of disjoint sets and perform union-find operations efficiently. It sorts all the edges of the graph in non-decreasing order of their weights. Then, it iterates through each edge and checks if adding the edge to the minimum spanning tree `MST` creates a cycle. If adding the edge does not create a cycle, it adds the edge to `MST`.

Finally, the function returns the `MST` represented by the set of edges.

The time complexity of Kruskal's algorithm is O(E log E), where E is the number of edges in the graph.