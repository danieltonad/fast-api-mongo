from pydantic import BaseModel
import datetime

class Todo(BaseModel):
    name: str
    decription: str
    completed: bool
    date: datetime