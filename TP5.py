import heapq

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.num_nodes = len(graph)

    def dijkstra(self, source, target):
        distance = [float('inf')] * self.num_nodes
        distance[source] = 0
        previous = [-1] * self.num_nodes
        priority_queue = [(0, source)]  # (distance, node)

        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)

            if current_dist > distance[current_node]:
                continue

            for neighbor, weight in enumerate(self.graph[current_node]):
                if weight != float('inf'):
                    new_dist = current_dist + weight
                    if new_dist < distance[neighbor]:
                        distance[neighbor] = new_dist
                        previous[neighbor] = current_node
                        heapq.heappush(priority_queue, (new_dist, neighbor))

        # Reconstruct the shortest path
        path = []
        current = target
        while current != -1:
            path.append(current)
            current = previous[current]

        path.reverse()
        return path, distance[target]

# Graph adjacency matrix representation
graph = [
    [0, 4, 1, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
    [4, 0, float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'), float('inf'), float('inf')],
    [1, float('inf'), 0, 8, float('inf'), 7, float('inf'), float('inf'), float('inf'), float('inf')],
    [float('inf'), float('inf'), 8, 0, float('inf'), float('inf'), float('inf'), 5, float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf'), 0, 1, float('inf'), 2, 2, float('inf')],
    [float('inf'), 3, 7, float('inf'), 1, 0, float('inf'), 1, float('inf'), float('inf')],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0, 3, 4, 4],
    [float('inf'), float('inf'), float('inf'), 5, 2, 1, 3, 0, 6, 7],
    [float('inf'), float('inf'), float('inf'), float('inf'), 2, float('inf'), 4, 6, 0, 1],
    [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 4, 7, 1, 0]
]

# Node labels
nodes = "ABCDEFGHLM"

# Input source and target
source_label = input("Enter source node (e.g., A): ").strip().upper()
target_label = input("Enter target node (e.g., M): ").strip().upper()

source = nodes.index(source_label)
target = nodes.index(target_label)

# Run Dijkstra's algorithm
g = Graph(graph)
path, total_weight = g.dijkstra(source, target)

# Convert path indices back to labels
path_labels = [nodes[i] for i in path]

# Output results
print("Shortest path:", path_labels)
print("Total weight of shortest path:", total_weight)
