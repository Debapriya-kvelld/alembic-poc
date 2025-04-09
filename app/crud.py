from app.models import Todo
from app.database import get_session
from sqlmodel import select

def create_todo(todo: Todo):
    with get_session() as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo

def read_todos():
    with get_session() as session:
        return session.exec(select(Todo)).all()
