from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return {"message": "hello"}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created and title is {request.title}'}
