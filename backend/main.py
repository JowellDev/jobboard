from fastapi import FastAPI
from typing import Optional
from core.config import settings
from db.session import engine
from db.base_class import Base

app = FastAPI(title = settings.PROJECT_NAME, version = settings.PROJECT_VERSION)

@app.get('/')
async def hello():
    return {"text": "hello world"}

