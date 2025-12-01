from maze_solver import solve_random_maze

maze, start, end, path = solve_random_maze()
print("Start:", start, "End:", end)
print("Path length:", len(path) if path else None)
