from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI(title="DS Visualizer API", description="API for DS Visualizer", version="1.0.0")


# Define a GET route for the root URL
@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "API is healthy"}
