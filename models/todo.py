from pydantic import BaseModel
import datetime

class Todo(BaseModel):
    name: str
    description: str
    completed: bool
    # date: datetime