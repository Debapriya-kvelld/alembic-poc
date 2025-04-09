from fastapi import FastAPI
from app.models import Todo
from app.crud import create_todo, read_todos

app = FastAPI()

@app.post("/todos/")
def add_todo(todo: Todo):
    return create_todo(todo)

@app.get("/todos/")
def list_todos():
    return read_todos()
