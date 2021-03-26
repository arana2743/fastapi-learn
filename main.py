from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
  return { 'data': {'Name': 'AbhisekRana' } }

@app.get('/about')
def about():
  return { 'data': { 'Name': 'about page' } }

@app.get('/blogs')
def get_blogs():
  return { 'data': 'Blog data' }

@app.get('/blog/{id}')
def get_blog(id: int):
  return {'data': id} 