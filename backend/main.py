from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI(title="DS Visualizer API", description="API for DS Visualizer", version="1.0.0")

# changes to be noticed for ci-protection for main


# Define a GET route for the root URL
@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "API is healthy"}
