from typing import List
from pymongo.collection import Collection
from models.todo_models import TodoItemCreate, TodoItemUpdate, TodoItemInDB
from bson import ObjectId

class TodoRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    async def create(self, todo: TodoItemCreate) -> TodoItemInDB:
        todo_dict = todo.dict()
        result = await self.collection.insert_one(todo_dict)
        todo_dict["id"] = str(result.inserted_id)
        return TodoItemInDB(**todo_dict)

    async def get_by_id(self, todo_id: str) -> TodoItemInDB:
        todo = await self.collection.find_one({"_id": ObjectId(todo_id)})
        if todo is None:
            return None
        todo["id"] = str(todo["_id"])
        return TodoItemInDB(**todo)

    async def update(self, todo_id: str, todo: TodoItemUpdate) -> TodoItemInDB:
        update_dict = {k: v for k, v in todo.dict().items() if v is not None}
        result = await self.collection.update_one({"_id": ObjectId(todo_id)}, {"$set": update_dict})
        if result.matched_count == 0:
            return None
        return await self.get_by_id(todo_id)

    async def delete(self, todo_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(todo_id)})
        return result.deleted_count > 0
