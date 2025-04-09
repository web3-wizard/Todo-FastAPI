from fastapi import FastAPI, HTTPException
from src.routes import todos

app = FastAPI()

app.include_router(todos.router, prefix="/api", tags=["Todos"])

@app.get("/api", tags=["Welcome"])
def welcome():
    return {"message": "Welcome to Todos Api"}

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": 200,
        "message": "Api is healthy"
    }