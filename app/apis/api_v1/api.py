from fastapi import APIRouter

from app.apis.api_v1.endpoints import consignment

api_router = APIRouter()
api_router.include_router(consignment.router, tags=["consignment"])
