from typing import List
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError
from jose import jwt


from app.repos import Auth
from app.schemas import CreateUserSchema, user_schema
from app.models import User

router = APIRouter()


from app.core.config import get_app_settings

settings = get_app_settings()


@router.post("/register", response_model=user_schema)
async def register(form_data: CreateUserSchema = Depends()):
    if await User.get_or_none(email=form_data.email) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    user = await User.create(
        email=form_data.email,
        hashed_password=Auth.get_password_hash(
            form_data.password.get_secret_value()
        )
    )
    access_token = Auth.get_access_token(user.id)
    user.access_token = access_token["jti"]
    await user.save()
    
    return user


# class Status(BaseModel):
#     message: str

# from fastapi import APIRouter
# from fastapi import Depends, HTTPException, status
# from services.auth import Auth
# from services.mailer import Mailer
# from models import users
# from jose import jwt

# auth_router = APIRouter()


# @auth_router.post("/register")
# async def register(form_data: users.CreateUser = Depends()):
#     if await users.UserModel.get_or_none(email=form_data.email) is not None:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User already exists"
#         )
#     user = await users.UserModel.create(
#         email=form_data.email,
#         hashed_password=Auth.get_password_hash(
#             form_data.password.get_secret_value()
#         )
#     )
#     confirmation = Auth.get_confirmation_token(user.id)
#     user.confirmation = confirmation["jti"]
#     try:
#         Mailer.send_confirmation_message(confirmation["token"], form_data.email)
#     except ConnectionRefusedError:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="Email couldn't be send. Please try again."
#         )
#     await user.save()


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


# from app.repos import all_consignments, add_consignment
# from app.schemas import list_consignment_schema, add_consignment_schema

# router = APIRouter()

# #write api endpoints here

# @router.post("/consignment", response_model=add_consignment_schema)
# async def consignment(data: add_consignment_schema):
#     return await add_consignment(data.dict())

# @router.get("/consignments")
# async def all_consignment():
#     return await all_consignments()