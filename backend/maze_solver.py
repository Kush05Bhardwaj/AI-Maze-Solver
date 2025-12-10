import numpy as np
import heapq

# ---------- Maze generation ----------
def generate_maze(rows=20, cols=20, wall_count=120, seed=None):
    # Only use seed if explicitly provided
    if seed is not None:
        np.random.seed(seed)

    maze = np.zeros((rows, cols), dtype=int)

    # Add random walls
    placed = 0
    while placed < wall_count:
        r = np.random.randint(0, rows)
        c = np.random.randint(0, cols)
        if (r, c) not in [(0, 0), (rows - 1, cols - 1)]:
            maze[r][c] = 1
            placed += 1

    start, end = (0, 0), (rows - 1, cols - 1)
    maze[start] = 0
    maze[end] = 0

    return maze, start, end


# ---------- A* ----------
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
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        cr, cc = current

        neighbors = [(cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)]

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


# ---------- Helper ----------
def solve_random_maze(rows=20, cols=20, wall_count=120, seed=None):
    maze, start, end = generate_maze(rows, cols, wall_count, seed)
    path = a_star(maze, start, end)
    return maze, start, end, path
