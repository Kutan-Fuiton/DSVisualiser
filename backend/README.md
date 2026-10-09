# Code-to-Data-Structure Visualizer

Write code, watch the data structure being built step by step.

## Stack
FastAPI, Python tracer, React + Vite (planned), Docker, GitHub Actions.

## Run the backend
    cd backend
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements-dev.txt
    uvicorn app.main:app --reload

## Run the checks
    ruff check . && mypy && pytest