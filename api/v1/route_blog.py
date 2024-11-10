from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schema.blog import CreateBlog, ShowBlog, UpdateBlog
from db.session import get_db
from db.model.user import User
from db.repository.blog import create_new_blog, get_blog_by_id, list_all_active_blogs, update_blog_by_id, delete_blog_by_id
from api.v1.route_login import get_current_user


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
def update_blog(blog_id: int, blog: UpdateBlog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = update_blog_by_id(blog_id, blog, db, current_user.id)
    if blog.get("error"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=blog.get("error"))
    return blog

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)    # DELETE /api/v1/blogs/{id}
def delete_blog(blog_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    blog = delete_blog_by_id(blog_id, db, current_user.id)
    if blog.get("error"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=blog.get("error"))
    return None