from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False

todos: List[Todo]  = [];

@app.get("/")
def welcome():
    return {"message": "Welcome to Todos Api"}

@app.get("/todos", response_model=List[Todo])
def get_all_todos() -> List[Todo]:
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo:
    for todo in todos:
        if todo.id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")

@app.post("/todos", status_code=201, response_model=Todo)
def create_todo(todo: Todo) -> Todo:
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo) -> Todo:
    for todo in todos:
        if todo.id == todo_id:
            todo.title = updated_todo.title
            todo.description = updated_todo.description
            todo.completed = updated_todo.completed
            return todo

    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return

    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")