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