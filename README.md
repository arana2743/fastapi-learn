# Learning FastAPI - for rapid building of REST APIs in Python.

To get started with project setup, below are the packages and command used.
Please refer to this [link](https://fastapi.tiangolo.com/) for official FastAPI documentation
```
pip install fastapi uvicorn[standard]
```

FastAPI uses uvicorn as webserver, below is the command to run any file.
```
uvicorn main:app --reload
```

By default uvicorn runs on port 8000, but if port needs to be changed, then just add below code to `main.py` and uvicorn will run on port 9000.
```
import uvicorn
if __name__ == '__main__':
  uvicorn.run(app, host="127.0.0.1", port=9000)
```