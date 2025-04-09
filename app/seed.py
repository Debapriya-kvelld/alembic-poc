from datetime import datetime
from app.models import Todo
from app.database import get_session

def seed():
    session = get_session()
    session.add_all([
        Todo(title="Learn FastAPI", completed=False, due_date=datetime.now(), priority=1),
        Todo(title="Build Alembic POC", completed=True, due_date=datetime.now(), priority=2),
        Todo(title="Push to GitHub", completed=False, due_date=datetime.now(), priority=3)
    ])
    session.commit()
    print("✅ Seed data inserted!")

if __name__ == "__main__":
    seed()
