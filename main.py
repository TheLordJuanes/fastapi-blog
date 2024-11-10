from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from api.base import api_router
from apps.base import app_router


def include_router(application):
    application.include_router(api_router)
    application.include_router(app_router)

def configure_staticfiles(application):
    application.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    application = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(application)
    configure_staticfiles(application)
    return application

app = start_application()