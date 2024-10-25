from fastapi import APIRouter
from backend.api.v1 import route_user, route_blog


api_router = APIRouter()

api_router.include_router(route_user.router, prefix="/users", tags=["users"])
api_router.include_router(route_blog.router, prefix="/blogs", tags=["blogs"])