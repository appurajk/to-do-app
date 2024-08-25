from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[datetime] = None

class TodoItemCreate(TodoItemBase):
    pass

class TodoItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None

class TodoItemInDB(TodoItemBase):
    id: str
    owner_id: str  # Reference to the user who owns the to-do item
