from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.schemas.blog import BlogCreate, ShowBlog
from backend.db.session import get_db
from backend.db.repository.blog import create_new_blog


router = APIRouter()

@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)    # POST /api/v1/create-blog
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    return create_new_blog(blog, db, 1)