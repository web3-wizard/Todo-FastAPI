from pydantic import BaseModel, validator, conint
from sqlmodel import SQLModel, Field
from typing import Optional

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    completed: bool = Field(default=False)

class TodoDTO(BaseModel):
    title: str
    completed: bool = False