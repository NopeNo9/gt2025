import heapq

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.num_nodes = len(graph)

    def prim_mst(self, root):
        visited = [False] * self.num_nodes
        min_heap = [(0, root, -1)]  # (weight, node, parent)
        mst_edges = []
        total_weight = 0

        while min_heap:
            weight, node, parent = heapq.heappop(min_heap)
            if visited[node]:
                continue

            visited[node] = True
            total_weight += weight
            if parent != -1:
                mst_edges.append((parent + 1, node + 1, weight))

            for adj in range(self.num_nodes):
                if not visited[adj] and self.graph[node][adj] != float('inf'):
                    heapq.heappush(min_heap, (self.graph[node][adj], adj, node))

        return mst_edges, total_weight

    def kruskal_mst(self):
        edges = []
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                if self.graph[i][j] != float('inf'):
                    edges.append((self.graph[i][j], i, j))

        edges.sort()
        uf = UnionFind(self.num_nodes)
        mst_edges = []
        total_weight = 0

        for weight, u, v in edges:
            if uf.union(u, v):
                mst_edges.append((u + 1, v + 1, weight))
                total_weight += weight

        return mst_edges, total_weight

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 4, float('inf'), float('inf'), 1, float('inf'), 2, float('inf'), float('inf')],
        [4, 0, 7, float('inf'), float('inf'), 5, float('inf'), float('inf'), float('inf')],
        [float('inf'), 7, 0, 1, float('inf'), 8, float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), 1, 0, float('inf'), 6, 4, 3, float('inf')],
        [1, float('inf'), float('inf'), float('inf'), 0, 9, 10, float('inf'), float('inf')],
        [float('inf'), 5, 8, 6, 9, 0, float('inf'), float('inf'), 2],
        [2, float('inf'), float('inf'), 4, 10, float('inf'), 2, float('inf'), 8],
        [float('inf'), float('inf'), float('inf'), 3, float('inf'), float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2, 8, 1, 0]
    ]

    g = Graph(graph)

    root_node = int(input("Enter the root node (1-9): ")) - 1
    mst_edges, total_weight = g.prim_mst(root_node)
    print("\nPrim's Algorithm - MST edges and weights:")
    for edge in mst_edges:
        print(f"Edge: {edge[0]}-{edge[1]} with weight {edge[2]}")
    print(f"Total weight of MST: {total_weight}")

    mst_edges_kruskal, total_weight_kruskal = g.kruskal_mst()
    print("\nKruskal's Algorithm - MST edges and weights:")
    for edge in mst_edges_kruskal:
        print(f"Edge: {edge[0]}-{edge[1]} with weight {edge[2]}")
    print(f"Total weight of MST: {total_weight_kruskal}")
