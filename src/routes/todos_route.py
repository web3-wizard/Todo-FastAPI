from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import conint
from src.models.todo_model import Todo
from src.repositories.todo_repository import TodoRepository
from src.DB.db_config import get_session

router = APIRouter(prefix="/todos", tags=["Todos"])

def get_repository() -> TodoRepository:
    session = get_session()
    try:
        repo = TodoRepository(session)
        yield repo
    finally:
        session.close()

@router.get("/", response_model=List[Todo])
def get_all_todos(repo: TodoRepository = Depends(get_repository)) -> List[Todo]:
    todo_list = repo.get_all()
    return todo_list

@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: conint(gt=0), repo: TodoRepository = Depends(get_repository)) -> Todo:
    todo = repo.get(todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")
    return todo

@router.post("/", status_code=201, response_model=Todo)
def create_todo(todo: Todo, repo: TodoRepository = Depends(get_repository)) -> Todo:
    new_todo = repo.create(todo)
    return new_todo

@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: conint(gt=0), updated_todo: Todo, repo: TodoRepository = Depends(get_repository)) -> Todo:
    existing_todo = repo.get(todo_id=todo_id)
    if existing_todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")
    existing_todo.title = updated_todo.title
    existing_todo.completed = updated_todo.completed
    todo = repo.update(existing_todo)
    return todo

@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: conint(gt=0), repo: TodoRepository = Depends(get_repository)) -> None:
    todo = repo.get(todo_id=todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"Todo with id: {todo_id} not found")
    repo.delete(todo)
    return