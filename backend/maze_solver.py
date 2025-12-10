import numpy as np
import heapq
import random

# -----------------------------------------------------------
#  DFS MAZE GENERATION (Best fix)
#  Creates perfect mazes with unique, interesting A* paths
# -----------------------------------------------------------

def generate_maze(rows=20, cols=20, wall_count=None, seed=None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    # Start with all walls
    maze = np.ones((rows, cols), dtype=int)

    # Helper to check bounds
    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # DFS stack
    stack = [(0, 0)]
    maze[0][0] = 0

    # Move directions for DFS (2 steps)
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    while stack:
        r, c = stack[-1]

        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and maze[nr][nc] == 1:
                neighbors.append((nr, nc))

        if not neighbors:
            stack.pop()
            continue

        nr, nc = random.choice(neighbors)

        # Knock down the wall between
        wall_r = r + (nr - r) // 2
        wall_c = c + (nc - c) // 2

        if in_bounds(wall_r, wall_c):
            maze[wall_r][wall_c] = 0
        if in_bounds(nr, nc):
            maze[nr][nc] = 0

        stack.append((nr, nc))

    start = (0, 0)
    end = (rows - 1, cols - 1)

    maze[start] = 0
    maze[end] = 0

    return maze, start, end



# -----------------------------------------------------------
#  A* Algorithm
# -----------------------------------------------------------

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(maze, start, end):
    rows, cols = maze.shape
    pq = []
    heapq.heappush(pq, (0, start))

    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    parent = {}

    while pq:
        _, current = heapq.heappop(pq)

        if current == end:
            # Reconstruct path
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        cr, cc = current
        neighbors = [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]

        for nbr in neighbors:
            nr, nc = nbr
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                new_g = g_score[current] + 1

                if nbr not in g_score or new_g < g_score[nbr]:
                    parent[nbr] = current
                    g_score[nbr] = new_g
                    f_score[nbr] = new_g + heuristic(nbr, end)
                    heapq.heappush(pq, (f_score[nbr], nbr))

    return None


# -----------------------------------------------------------
#  Wrapper
# -----------------------------------------------------------

def solve_random_maze(rows=20, cols=20, wall_count=None, seed=None):
    maze, start, end = generate_maze(rows, cols, wall_count, seed)
    path = a_star(maze, start, end)
    return maze, start, end, path
