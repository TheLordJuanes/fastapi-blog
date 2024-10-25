from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from backend.schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from backend.db.session import get_db
from backend.db.repository.blog import create_new_blog, get_blog_by_id, list_all_active_blogs, update_blog_by_id, delete_blog_by_id


router = APIRouter()

@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)    # POST /api/v1/blogs
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    return create_new_blog(blog, db, 1)

@router.get("/{id}", response_model=ShowBlog)    # GET /api/v1/blogs/{id}
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = get_blog_by_id(blog_id, db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
    return blog

@router.get("/", response_model=List[ShowBlog])    # GET /api/v1/blogs
def get_all_active_blogs(db: Session = Depends(get_db)):
    return list_all_active_blogs(db)

@router.put("/{id}", response_model=ShowBlog)    # PUT /api/v1/blogs/{id}
def update_blog(blog_id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
    blog = update_blog_by_id(blog_id, blog, db, 1)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
    return blog

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)    # DELETE /api/v1/blogs/{id}
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    if not delete_blog_by_id(blog_id, db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
    return None