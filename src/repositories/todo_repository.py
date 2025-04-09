from sqlmodel import Session, select
from src.models.todo_model import Todo
from typing import Optional

class TodoRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, todo: Todo) -> Todo:
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def get_all(self) -> list[Todo]:
        statement = select(Todo)
        return self.session.exec(statement).all()

    def get(self, todo_id: int) -> Optional[Todo]:
        statement = select(Todo).where(Todo.id == todo_id)
        return self.session.exec(statement).first()

    def update(self, todo: Todo) -> Todo:
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def delete(self, todo: Todo) -> None:
        self.session.delete(todo)
        self.session.commit()