from fastapi import FastAPI
from starlette.responses import HTMLResponse
import config.db

app = FastAPI()

@app.get('/')
def index():
    return HTMLResponse('You in MF')