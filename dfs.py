# Directed graph represented using an adjacency list
graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [6],
    5: [],
    6: []
}

# Function to perform DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes

    visited.add(start)
    print(start, end=' ')  # Process the current node

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Perform DFS starting from node 1
dfs(graph, 1)
