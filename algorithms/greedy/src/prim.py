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