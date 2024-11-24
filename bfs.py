# Graph representation using adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

# Function to perform BFS
def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = [start]  # Initialize the queue with the start node

    while queue:
        current = queue.pop(0)  # Dequeue the front element
        if current not in visited:
            print(current, end=' ')  # Process the current node
            visited.add(current)
            # Enqueue all unvisited neighbors
            queue.extend([neighbor for neighbor in graph[current] if neighbor not in visited])

# Perform BFS starting from node 1
bfs(graph, 1)
