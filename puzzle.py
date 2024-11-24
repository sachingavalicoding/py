from collections import deque

def is_solvable(puzzle):
    # Count inversions to check solvability
    inversion_count = 0
    flattened = [tile for row in puzzle for tile in row if tile != 0]
    for i in range(len(flattened)):
        for j in range(i + 1, len(flattened)):
            if flattened[i] > flattened[j]:
                inversion_count += 1
    return inversion_count % 2 == 0

def find_zero(puzzle):
    # Locate the position of the empty space (0)
    for i, row in enumerate(puzzle):
        for j, val in enumerate(row):
            if val == 0:
                return i, j

def valid_moves(x, y):
    # Define possible moves: up, down, left, right
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(nx, ny) for nx, ny in moves if 0 <= nx < 3 and 0 <= ny < 3]

def make_move(puzzle, x, y, nx, ny):
    # Perform a move and return the new puzzle state
    new_puzzle = [row[:] for row in puzzle]
    new_puzzle[x][y], new_puzzle[nx][ny] = new_puzzle[nx][ny], new_puzzle[x][y]
    return new_puzzle

def bfs_solve(start, goal):
    # Solve the puzzle using BFS
    queue = deque([(start, [])])
    visited = set()
    visited.add(tuple(tuple(row) for row in start))

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path

        x, y = find_zero(current)
        for nx, ny in valid_moves(x, y):
            new_state = make_move(current, x, y, nx, ny)
            new_state_tuple = tuple(tuple(row) for row in new_state)
            if new_state_tuple not in visited:
                visited.add(new_state_tuple)
                queue.append((new_state, path + [(nx, ny)]))
    return None

def print_puzzle(puzzle):
    for row in puzzle:
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()

# Example usage
if __name__ == "__main__":
    start_state = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    if not is_solvable(start_state):
        print("The puzzle is unsolvable!")
    else:
        print("Initial State:")
        print_puzzle(start_state)

        print("Goal State:")
        print_puzzle(goal_state)

        solution = bfs_solve(start_state, goal_state)
        if solution:
            print(f"Solution found in {len(solution)} moves!")
        else:
            print("No solution exists.")
