from typing import List
from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.db import get_session
from app.models.user import User, UserCreate
from app.crud.user import list_users, create_user, get_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User], summary="List users", description="Return a list of users.")
def read_users(*, session: Session = Depends(get_session)):
    return list_users(session)

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED, summary="Create user", description="Create a user and return it.")
def create_new_user(*, session: Session = Depends(get_session), user: UserCreate):
    return create_user(session, user)

@router.get("/{user_id}", response_model=User, summary="Get user by id")
def read_user(*, user_id: int, session: Session = Depends(get_session)):
    db_user = get_user(session, user_id)
    if not db_user:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
