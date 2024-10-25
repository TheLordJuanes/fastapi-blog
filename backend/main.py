from fastapi import FastAPI
from backend.core.config import settings
from backend.api.base import api_router

from backend.db.models.blog import Blog


def include_router(application):
    application.include_router(api_router)

def start_application():
    application = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(application)
    return application

app = start_application()

@app.get("/")
def read_root():
    return {"msg": "Hello World!"}