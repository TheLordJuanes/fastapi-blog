from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.schemas.user import UserCreate, ShowUser
from backend.db.session import get_db
from backend.db.repository.user import create_new_user


router = APIRouter()

@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)    # POST /api/v1/create-user
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(user, db)
