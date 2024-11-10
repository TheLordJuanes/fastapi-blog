from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schema.user import UserCreate, ShowUser
from db.session import get_db
from db.repository.user import create_new_user


router = APIRouter()

@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)    # POST /api/v1/users
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(user, db)
