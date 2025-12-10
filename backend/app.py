from flask import Flask, request, jsonify
from flask_cors import CORS
from maze_solver import solve_random_maze

app = Flask(__name__)
CORS(app)  # Allow all origins


@app.route("/ping")
def ping():
    return "pong", 200


@app.route("/solve", methods=["POST"])
def solve():
    try:
        data = request.get_json(force=True)

        rows = int(data.get("rows", 20))
        cols = int(data.get("cols", 20))

        # DFS generator no longer uses wall_count or seed
        maze, start, end, path = solve_random_maze(
            rows=rows,
            cols=cols,
            seed=None  # Always random
        )

        return jsonify({
            "rows": rows,
            "cols": cols,
            "maze": maze.tolist(),
            "start": list(start),
            "end": list(end),
            "path": [list(p) for p in path] if path else [],
            "found": path is not None
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


if __name__ == "__main__":
    app.run(debug=True)
