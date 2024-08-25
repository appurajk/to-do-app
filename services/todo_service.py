from repositories.todo_repository import TodoRepository
from models.todo_models import TodoItemCreate, TodoItemUpdate, TodoItemInDB

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    async def create_todo_item(self, todo: TodoItemCreate) -> TodoItemInDB:
        return await self.repository.create(todo)

    async def get_todo_item(self, todo_id: str) -> TodoItemInDB:
        return await self.repository.get_by_id(todo_id)

    async def update_todo_item(self, todo_id: str, todo: TodoItemUpdate) -> TodoItemInDB:
        return await self.repository.update(todo_id, todo)

    async def delete_todo_item(self, todo_id: str) -> bool:
        return await self.repository.delete(todo_id)
