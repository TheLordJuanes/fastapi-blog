from sqlalchemy.orm import Session
from backend.schemas.user import UserCreate
from backend.db.models.user import User
from backend.core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(email=user.email, password=Hasher.hash_password(user.password), is_active=True)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user