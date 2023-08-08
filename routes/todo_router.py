from fastapi import APIRouter
from config.db import collection_name
from models.todo import Todo
from schemas.todo  import todo_serializer, todos_serializer 
from bson import ObjectId

todo_api_router = APIRouter()

@todo_api_router.get('/todos')
async def get_todos():
    todo = todos_serializer(collection_name.find())
    return {'data': todo}

@todo_api_router.get('/todo/{id}')
async def get_todo(id: str):
    return todos_serializer(collection_name.find({'_id': ObjectId(id)}))

@todo_api_router.post('/post')
async def insert_todo(todo: Todo):
    id = collection_name.insert_one(dict(todo))
    # data = "todos_serializer(collection_name.find({'_id': id.inserted_id}))"
    # return {'message' : 'created', 'id': id, 'data' : data}
    return 100