from typing import List
from pydantic import BaseModel
from fastapi import Depends
from fastapi import APIRouter

from app.schemas import user_schema
from app.models import User
from app.core.response import ResponseInfo
from app.core.config import get_app_settings
from app.core.dependency import get_current_user


settings = get_app_settings()
router = APIRouter()

@router.get("/users", response_model=List[user_schema])
async def get_users():
    return await user_schema.from_queryset(User.all())

@router.get("/get_user", response_model=user_schema)
async def authenticated_user(user: User = Depends(get_current_user)):
    return user
