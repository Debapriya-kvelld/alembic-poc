from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///./todos.db"
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)
