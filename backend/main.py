from fastapi import FastAPI
from typing import Optional
from core.config import settings
from db.session import engine
from db.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)

def run_app():
    app = FastAPI(title = settings.PROJECT_NAME, version = settings.PROJECT_VERSION)
    create_tables()
    return app

app = run_app()

@app.get('/')
async def hello():
    return {"text": "hello world"}