# backend/app.py
from flask import Flask, request, jsonify. , jsonify, make_response
from flask_cors import CORS
from maze_solver import solve_random_maze

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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

@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":
    app.run(debug=True)
