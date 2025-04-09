from datetime import datetime
from app.models import Todo
from app.database import get_session

def seed():
    session = get_session()
    session.add_all([
        Todo(title="Learn FastAPI", completed=False, due_date=datetime.now(), priority=1, category="Work"),
        Todo(title="Build Alembic POC", completed=True, due_date=datetime.now(), priority=2, category="Work"),
        Todo(title="Push to GitHub", completed=False, due_date=datetime.now(), priority=3, category="Work")
    ])
    session.commit()
    print("✅ Seed data inserted!")

if __name__ == "__main__":
    seed()
