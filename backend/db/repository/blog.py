from sqlalchemy.orm import Session
from backend.schemas.blog import BlogCreate
from backend.db.models.blog import Blog


def create_new_blog(blog: BlogCreate, db: Session, author_id: int = 1):
    blog = Blog(title=blog.title, slug=blog.slug, content=blog.content, author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog