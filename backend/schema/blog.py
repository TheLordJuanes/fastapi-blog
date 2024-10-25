from pydantic import BaseModel, model_validator
from typing import Optional
from datetime import datetime


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(self, values):
        if values.get("slug"):
            return values
        values["slug"] = values.get("title").replace(" ", "-").lower()
        return values

class UpdateBlog(CreateBlog):
    pass

class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True