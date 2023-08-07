from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def index():
    return HTMLResponse('You in MF')