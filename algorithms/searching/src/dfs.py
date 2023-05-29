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