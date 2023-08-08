from fastapi import FastAPI
from starlette.responses import HTMLResponse
from routes.todo_router import todo_api_router

app = FastAPI()
app.include_router(todo_api_router)
# @app.get('/')
# def index():
#     return HTMLResponse('You in MF')