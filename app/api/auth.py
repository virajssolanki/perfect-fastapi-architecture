from typing import List
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

from app.repos import authenticate, get_access_token, create_user
from app.schemas import CreateUserSchema, LoginSchema, user_schema
from app.models import User
from app.core.response import ResponseInfo
from app.core.config import get_app_settings

settings = get_app_settings()

router = APIRouter()

@router.post("/sign_up")
async def signup(data: CreateUserSchema = Depends()):
    if await User.get_or_none(email=data.email) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    user = await create_user(data.dict())

    access_token = get_access_token(user.id)
    res = ResponseInfo({'access_token': access_token["token"]}, "User registred successfully", True, 201)
    return res.custom_success_payload()


@router.post("/login")
async def login(credentials: LoginSchema = Depends()):
    user = await authenticate(credentials)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    
    access_token = get_access_token(user.id)
    
    res = ResponseInfo({
        "access_token": access_token["token"], 
        "token_type": "bearer",}, 
        "User registred successfully", True, 201)

    return res.custom_success_payload()




# @router.get("/users", response_model=List[User_Pydantic])
# async def get_users():
#     return await User_Pydantic.from_queryset(User.all())


# @router.post("/users", response_model=User_Pydantic)
# async def create_user(user: UserIn_Pydantic):
#     user_obj = await User.create(**user.dict(exclude_unset=True))
#     return await User_Pydantic.from_tortoise_orm(user_obj)


# @router.get(
#     "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
# )
# async def get_user(user_id: int):
#     return await User_Pydantic.from_queryset_single(User.get(id=user_id))


# @router.put(
#     "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
# )
# async def update_user(user_id: int, user: UserIn_Pydantic):
#     await User.filter(id=user_id).update(**user.dict(exclude_unset=True))
#     return await User_Pydantic.from_queryset_single(User.get(id=user_id))


# @router.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
# async def delete_user(user_id: int):
#     deleted_count = await User.filter(id=user_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"User {user_id} not found")
#     return Status(message=f"Deleted user {user_id}")


# @router.post("/consignment", response_model=add_consignment_schema)
# async def consignment(data: add_consignment_schema):
#     return await add_consignment(data.dict())

# @router.get("/consignments")
# async def all_consignment():
#     return await all_consignments()