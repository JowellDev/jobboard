from fastapi import FastAPI
from typing import Optional

app = FastAPI(title='fastapi REST API', version="0.1.0")

@app.get('/')
async def hello():
    return {"text": "hello world"}





