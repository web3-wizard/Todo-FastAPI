from fastapi import FastAPI
from src.routes import todos_route
from src.DB.db_config import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(todos_route.router, prefix="/api")

@app.get("/api", tags=["Welcome"])
def welcome():
    return {"message": "Welcome to Todos Api"}

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": 200,
        "message": "Api is healthy"
    }