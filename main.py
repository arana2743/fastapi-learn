from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
  return { 'data': {'Name': 'AbhisekRana' } }

@app.get('/about')
def about():
  return { 'data': { 'Name': 'about page' } }