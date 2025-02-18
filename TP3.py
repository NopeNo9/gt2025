import numpy as np

# Construct Adjacency Matrix
def construct_adjacency_matrix(edges, n):
    adj_matrix = np.zeros((n, n), dtype=int)
    for u, v in edges:
        adj_matrix[u-1][v-1] = 1
    return adj_matrix

# Inorder Traversal of Tree
def inorder_traversal(tree, node):
    if node not in tree:
        return []
    
    left = inorder_traversal(tree, tree[node][0]) if len(tree[node]) > 0 else []
    right = inorder_traversal(tree, tree[node][1]) if len(tree[node]) > 1 else []
    
    return left + [node] + right

# Input Graph Data
edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
n = 8  # Number of nodes

# Step 1: Construct Adjacency Matrix
adj_matrix = construct_adjacency_matrix(edges, n)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

# Step 2: Convert Graph to Adjacency List for Tree
tree = {i: [] for i in range(1, n + 1)}
for u, v in edges:
    tree[u].append(v)

# Input: Node label (x)
x = int(input("Enter the node label to print subtree in Inorder: "))

# Step 3: Perform Inorder Traversal
inorder_result = inorder_traversal(tree, x)
print(f"Inorder Traversal of subtree rooted at node {x}: {inorder_result}")
