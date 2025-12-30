# Ensure models are importable for Alembic autogenerate
from app.models.user import User, UserCreate, UserBase  # noqa: F401
