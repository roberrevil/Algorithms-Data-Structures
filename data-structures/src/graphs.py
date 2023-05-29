class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v):
        if u in self.adjacency_list and v in self.adjacency_list:
            self.adjacency_list[u].append(v)
            self.adjacency_list[v].append(u)