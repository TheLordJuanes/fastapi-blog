from typing import Optional

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from db.repository.blog import list_all_active_blogs, get_blog_by_id
from db.session import get_db


templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/")
def home(request: Request, alert: Optional[str] = None, db: Session = Depends(get_db)):
    blogs = list_all_active_blogs(db)
    return templates.TemplateResponse("blogs/home.html", {"request": request, "blogs": blogs, "alert": alert})

@router.get("/app/blog/{blog_id}")
def blog_details(request: Request, blog_id: int, db: Session = Depends(get_db)):
    blog = get_blog_by_id(blog_id, db)
    return templates.TemplateResponse("blogs/detail.html", {"request": request, "blog": blog})