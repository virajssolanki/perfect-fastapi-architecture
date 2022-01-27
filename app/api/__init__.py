from fastapi import APIRouter

from app.api.modules import user

api_router = APIRouter()
api_router.include_router(user.router, tags=["user"])
