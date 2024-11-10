from sqlalchemy.orm import Session
from schema.blog import CreateBlog, UpdateBlog
from db.model.blog import Blog


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

def update_blog_by_id(blog_id: int, blog: UpdateBlog, db: Session, author_id: int):
    existing_blog = get_blog_by_id(blog_id, db)
    if not existing_blog:
        return {"error": f"Blog with id {blog_id} not found."}
    if not existing_blog.author_id == author_id:
        return {"error": "You are not the author of this blog."}
    for key, value in blog.model_dump().items():
        setattr(existing_blog, key, value) if value else None
    db.commit()
    db.refresh(existing_blog)
    return existing_blog

def delete_blog_by_id(blog_id: int, db: Session, author_id: int):
    existing_blog = get_blog_by_id(blog_id, db)
    if not existing_blog:
        return {"error": f"Blog with id {blog_id} not found."}
    if not existing_blog.author_id == author_id:
        return {"error": "You are not the author of this blog."}
    db.delete(existing_blog)
    db.commit()
    return True