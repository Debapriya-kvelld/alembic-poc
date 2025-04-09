from app.models import Todo
from app.database import get_session

def seed():
    session = get_session()
    session.add_all([
        Todo(title="Learn FastAPI", completed=False),
        Todo(title="Build Alembic POC", completed=True),
        Todo(title="Push to GitHub", completed=False)
    ])
    session.commit()
    print("✅ Seed data inserted!")

if __name__ == "__main__":
    seed()
