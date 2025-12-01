# app.py (root level entrypoint for deployment)
import sys
import os

# Add backend directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from flask import Flask, request, jsonify
from flask_cors import CORS
from maze_solver import solve_random_maze

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def home():
    return jsonify({
        "message": "AI Maze Solver API",
        "endpoints": {
            "/ping": "GET - Health check",
            "/solve": "POST - Generate and solve maze"
        }
    })

@app.route("/ping")
def ping():
    return "pong", 200


@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json(force=True)

    rows = int(data.get("rows", 20))
    cols = int(data.get("cols", 20))
    wall_count = int(data.get("wall_count", 120))
    seed = int(data.get("seed", 42))

    maze, start, end, path = solve_random_maze(
        rows=rows, cols=cols, wall_count=wall_count, seed=seed
    )

    return jsonify({
        "rows": rows,
        "cols": cols,
        "maze": maze.tolist(),
        "start": list(start),
        "end": list(end),
        "path": path if path else [],
        "found": bool(path)
    })


if __name__ == "__main__":
    app.run(debug=True)
