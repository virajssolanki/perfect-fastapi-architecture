from fastapi import APIRouter

from app.api.modules import consignment, user

api_router = APIRouter()
api_router.include_router(consignment.router, tags=["consignment"])
api_router.include_router(user.router, tags=["user"])
