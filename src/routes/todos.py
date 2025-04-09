from fastapi import APIRouter
from typing import List
from src.models.todo import Todo

router = APIRouter()

todos: List[Todo] = []

@router.get("/todos", response_model=List[Todo])
def get_all_todos() -> List[Todo]:
    return todos

@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo:
    for todo in todos:
        if todo.id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")

@router.post("/todos", status_code=201, response_model=Todo)
def create_todo(todo: Todo) -> Todo:
    todos.append(todo)
    return todo

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo) -> Todo:
    for todo in todos:
        if todo.id == todo_id:
            todo.title = updated_todo.title
            todo.description = updated_todo.description
            todo.completed = updated_todo.completed
            return todo

    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")

@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return

    raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")