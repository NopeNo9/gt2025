from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)  # Assuming the graph is undirected

    def is_path_exists(self, start, end):
        if start not in self.graph or end not in self.graph:
            return False

        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node == end:
                return True
            if node not in visited:
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph[node] if neighbor not in visited)
        
        return False

# Example Usage:
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(4, 7)
graph.add_edge(6, 4)
graph.add_edge(6, 7)

# User input
start_node = int(input("Enter the start node: "))
end_node = int(input("Enter the end node: "))

# Check if path exists
if graph.is_path_exists(start_node, end_node):
    print("Path exists")
else:
    print("Path does not exist")
