from contextlib import contextmanager
from sqlmodel import SQLModel, create_engine, Session
from app.config import DATABASE_URL

# Create engine; in production you may want to set pool_pre_ping etc.
engine = create_engine(DATABASE_URL, echo=True)

@contextmanager
def get_session_context():
    with Session(engine) as session:
        yield session

# Dependency for FastAPI
def get_session():
    with Session(engine) as session:
        yield session

# Convenience to create tables during development
def init_db():
    SQLModel.metadata.create_all(engine)
