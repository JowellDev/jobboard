from fastapi import FastAPI
from typing import Optional
from core.config import settings

app = FastAPI(title = settings.PROJECT_NAME, version = settings.PROJECT_VERSION)

@app.get('/')
async def hello():
    return {"text": "hello world"}





