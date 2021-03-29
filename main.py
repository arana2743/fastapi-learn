from fastapi import FastAPI
from typing import Optional

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