from sqlmodel import Session, select
from typing import List, Optional
from app.models.user import User, UserCreate


def get_user(session: Session, user_id: int) -> Optional[User]:
    return session.get(User, user_id)


def list_users(session: Session) -> List[User]:
    return session.exec(select(User)).all()


def create_user(session: Session, user_in: UserCreate) -> User:
    user = User(name=user_in.name, email=user_in.email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
