from sqlalchemy.orm import Session
from backend.schema.blog import CreateBlog, UpdateBlog
from backend.db.model.blog import Blog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(title=blog.title, slug=blog.slug, content=blog.content, author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def get_blog_by_id(blog_id: int, db: Session):
    return db.query(Blog).filter(Blog.id == blog_id).first()

def list_all_active_blogs(db: Session):
    return db.query(Blog).filter(Blog.is_active == True).all()

def update_blog_by_id(blog_id: int, blog: UpdateBlog, db: Session, author_id: int = 1):
    db.query(Blog).filter(Blog.id == blog_id).update({"title": blog.title, "slug": blog.slug, "content": blog.content, "author_id": author_id})
    db.commit()
    return db.query(Blog).filter(Blog.id == blog_id).first()

def delete_blog_by_id(blog_id: int, db: Session):
    if db.query(Blog).filter(Blog.id == blog_id).delete():
        db.commit()
        return True
    return False