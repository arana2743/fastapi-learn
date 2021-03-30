from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
  return { 'data': {'Name': 'AbhisekRana' } }

@app.get('/about')
def about():
  return { 'data': { 'Name': 'about page' } }

@app.get('/blog')
def get_blogs(limit: int = 10, published: bool = True, sort: Optional[str] = None):
  # only get 10 published blogs
  if published and sort:
    return { 'data': f'{limit} published blogs from db sorted by {sort}.' }
  else:
    return { 'data': 'All blogs from db.'}

@app.get('/blog/{id}')
def get_blog(id: int):
  return {'data': id} 

class Blog(BaseModel):
  title: str
  body: str
  published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
  return request
  # return { 'data': 'Blog created successfully' }

if __name__ == '__main__':
  uvicorn.run(app, host="127.0.0.1", port=9000)