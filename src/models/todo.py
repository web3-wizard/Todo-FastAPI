from pydantic import BaseModel, validator, conint

class Todo(BaseModel):
    id: conint(gt=0)
    title: str
    completed: bool = False

    @validator('id')
    def check_id_positive(cls, value):
        if value <= 0:
            raise ValueError('id must be a positive integer greater than zero')
        return value
