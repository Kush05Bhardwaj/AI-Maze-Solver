# AI Maze Solver (A* Algorithm)

An interactive web-based maze solver that uses the A* pathfinding algorithm to find the shortest path through randomly generated mazes.

![AI Maze Solver](https://img.shields.io/badge/Algorithm-A*-blue)
![Python](https://img.shields.io/badge/Python-3.10-green)
![Flask](https://img.shields.io/badge/Flask-3.1.2-red)

## 🚀 Features

- **A* Pathfinding Algorithm**: Efficient pathfinding using Manhattan distance heuristic
- **Random Maze Generation**: Create custom mazes with configurable parameters
- **Interactive Web Interface**: Real-time visualization of maze solving
- **Fast Performance**: Solves mazes in milliseconds
  - 20×20 maze: ~1-10 ms
  - 50×50 maze: ~4-15 ms
  - 100×100 maze: ~15-30 ms
- **RESTful API**: Backend API for maze generation and solving
- **CORS Enabled**: Frontend can communicate with backend seamlessly

## 📁 Project Structure

```
AI Maze Solver/
├── backend/
│   ├── app.py                    # Flask API server
│   ├── maze_solver.py            # A* algorithm implementation
│   ├── test_run.py              # Quick test script
│   ├── performance_test.py      # Performance benchmarks
│   └── api_performance_test.py  # API response time tests
├── frontend/
│   └── index.html               # Web interface
├── Capstone.ipynb              # Jupyter notebook demo
├── test_frontend_connection.py # Connection verification script
├── README.md
└── .gitignore
```

## 🛠️ Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kush05Bhardwaj/AI-Maze-Solver.git
   cd AI-Maze-Solver
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install flask flask-cors numpy requests gunicorn
   ```

## 🎮 Usage

### Running the Application

1. **Start the Backend Server**
   ```bash
   cd backend
   python app.py
   ```
   The API will be available at `http://127.0.0.1:5000`

2. **Start the Frontend Server**
   ```bash
   cd frontend
   python -m http.server 8000
   ```
   Open your browser to `http://localhost:8000/index.html`

3. **Use the Interface**
   - Set maze dimensions (Rows & Columns)
   - Set wall count (fewer walls = easier maze)
   - Click "Generate & Solve" to see the solution!

### Recommended Settings

| Difficulty | Maze Size | Wall Count |
|-----------|-----------|------------|
| Easy      | 20×20     | 40-60      |
| Medium    | 20×20     | 70-90      |
| Hard      | 30×30     | 200-250    |
| Expert    | 50×50     | 500-700    |

## 🔌 API Endpoints

### `GET /ping`
Health check endpoint.

**Response:**
```
pong
```

### `POST /solve`
Generate and solve a maze.

**Request Body:**
```json
{
  "rows": 20,
  "cols": 20,
  "wall_count": 60,
  "seed": 42
}
```

**Response:**
```json
{
  "rows": 20,
  "cols": 20,
  "maze": [[0, 1, 0, ...], ...],
  "start": [0, 0],
  "end": [19, 19],
  "path": [[0, 0], [0, 1], ...],
  "found": true
}
```

**Maze Values:**
- `0` = Empty cell (walkable)
- `1` = Wall (blocked)

## 🧪 Testing

### Run Performance Tests
```bash
cd backend
python performance_test.py
```

### Test API Performance
```bash
cd backend
python api_performance_test.py
```

### Verify Frontend-Backend Connection
```bash
python test_frontend_connection.py
```

### Run Basic Test
```bash
cd backend
python test_run.py
```

## 🎨 Visualization

The web interface uses color coding:
- 🔵 **Blue** = Start position (top-left)
- 🔴 **Red** = End position (bottom-right)
- 🟢 **Green** = Solution path
- ⬛ **Dark Gray** = Walls
- ⬜ **Light Gray** = Empty cells

## 📊 Performance Benchmarks

Based on 10 runs per configuration:

| Maze Size | Walls | Avg Time | Success Rate |
|-----------|-------|----------|--------------|
| 10×10     | 20    | 1.11 ms  | 90%          |
| 20×20     | 60    | 0.74 ms  | 90%          |
| 50×50     | 500   | 4.30 ms  | 90%          |
| 100×100   | 2000  | 15.45 ms | 80%          |

API response times (including network overhead):
- Small mazes (10×10): ~13-15 ms
- Medium mazes (20×20): ~15-20 ms
- Large mazes (50×50): ~40-70 ms
- Very large mazes (100×100): ~100-130 ms

## 🧠 Algorithm Details

### A* (A-Star) Pathfinding

The A* algorithm finds the shortest path by combining:
- **g(n)**: Cost from start to current node
- **h(n)**: Heuristic estimate from current node to goal (Manhattan distance)
- **f(n)**: Total estimated cost = g(n) + h(n)

The algorithm explores nodes with the lowest f(n) first, guaranteeing the shortest path.

### Manhattan Distance Heuristic
```python
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
```

This heuristic is admissible (never overestimates) and perfect for grid-based movement with 4 directions.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created as a capstone project demonstrating AI pathfinding algorithms.

## 🙏 Acknowledgments

- A* algorithm by Peter Hart, Nils Nilsson, and Bertram Raphael (1968)
- Flask web framework
- NumPy for efficient array operations

## 📚 Resources

- [A* Algorithm Wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Pathfinding Visualization](https://qiao.github.io/PathFinding.js/visual/)
- [Introduction to A*](https://www.redblobgames.com/pathfinding/a-star/introduction.html)

## 🚀 Deployment

### Deploy to Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow the prompts

Or click: [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Kush05Bhardwaj/AI-Maze-Solver)

### Deploy to Render

1. Create a new Web Service on [Render](https://render.com)
2. Connect your GitHub repository
3. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### Deploy to Heroku

```bash
heroku create your-maze-solver
git push heroku master
```

The `Procfile` and `requirements.txt` are already configured!

### Local Production Mode

```bash
gunicorn app:app --bind 0.0.0.0:5000
```

---

⭐ **Star this repository if you find it helpful!**
