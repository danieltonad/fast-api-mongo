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

@todo_api_router.post('/todo')
async def insert_todo(todo: Todo):
    id = collection_name.insert_one(dict(todo))
    return {'message' : 'created', 'id': str(id.inserted_id), 'data' : dict(todo)}

@todo_api_router.put('/todo/{id}')
async def update_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({'_id': ObjectId(id)},{
        "$set": dict(todo)
    })
    update = await get_todo(id)
    print(update)
    return {'message' : 'Update', 'data': update}


@todo_api_router.delete('/todo/{id}')
async def delete_todo(id: str):
    deleted_data = await get_todo(id)
    id = collection_name.delete_one({'_id': ObjectId(id)})
    return {'message' : 'deleted', 'data': deleted_data}