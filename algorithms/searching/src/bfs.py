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