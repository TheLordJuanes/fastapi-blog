from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import datetime


class BlogCreate(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(cls, values):
        if "slug" in values:
            return values
        values["slug"] = values["title"].replace(" ", "-").lower()
        return values

class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True