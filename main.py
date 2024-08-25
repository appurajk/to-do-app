''''' App to manage todo list'''
from fastapi import FastAPI, Depends
from repositories.todo_repository import TodoRepository
from services.todo_service import TodoService
from pymongo import MongoClient
from models.todo_models import TodoItemCreate, TodoItemUpdate, TodoItemInDB
from fastapi import FastAPI, Depends, HTTPException
from utils.db_connect import Dbconnect

app = FastAPI()
db=Dbconnect().mongodb_conn_get()
# Dependency
def get_todo_repository() -> TodoRepository:
    return TodoRepository(db["todos"])

def get_todo_service(repository: TodoRepository = Depends(get_todo_repository)) -> TodoService:
    return TodoService(repository)

@app.post("/todos/", response_model=TodoItemInDB)
async def create_todo_item(todo: TodoItemCreate, service: TodoService = Depends(get_todo_service)):
    print("started")
    return await service.create_todo_item(todo)

@app.get("/todos/{todo_id}", response_model=TodoItemInDB)
async def read_todo_item(todo_id: str, service: TodoService = Depends(get_todo_service)):
    return await service.get_todo_item(todo_id)

@app.put("/todos/{todo_id}", response_model=TodoItemInDB)
async def update_todo_item(todo_id: str, todo: TodoItemUpdate, service: TodoService = Depends(get_todo_service)):
    return await service.update_todo_item(todo_id, todo)

@app.delete("/todos/{todo_id}", response_model=dict)
async def delete_todo_item(todo_id: str, service: TodoService = Depends(get_todo_service)):
    success = await service.delete_todo_item(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"detail": "Todo item deleted"}
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

