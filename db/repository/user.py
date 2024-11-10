from sqlalchemy.orm import Session
from schema.user import UserCreate
from db.model.user import User
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(email=user.email, password=Hasher.hash_password(user.password), is_active=True)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()