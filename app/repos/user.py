from datetime import datetime, timedelta
from pydantic import UUID4
import uuid
from typing import List

from jose import jwt
from passlib.context import CryptContext

from app.schemas import *

from app.core.config import get_app_settings

settings = get_app_settings()


class Auth:
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(self, password: str) -> str:
        return self.password_context.hash(password)

    @staticmethod
    def get_token(data: dict, expires_delta: int):
        pass
        to_encode = data.copy()
        to_encode.update({
            "exp": datetime.utcnow() + timedelta(seconds=expires_delta),
            "iss": settings.title
        })
        return jwt.encode(
            to_encode,
            settings.secret_key,
            algorithm=settings.token_algorithm
        )

    @staticmethod
    def get_access_token(user_id: UUID4):
        jti = uuid.uuid4()
        claims = {
            "sub": str(user_id),
            "scope": "registration",
            "jti": str(jti)
        }
        return {
            "jti": jti,
            "token": Auth.get_token(
                claims,
                settings.token_lifetime
            )
        }










#write crud and business logics here
# async def add_consignment(data:add_consignment_schema) -> add_consignment_schema:
#     consignment = await Consignment.create(**data)
#     return consignment

# async def all_consignments() -> list_consignment_schema:
#     consignments = await list_consignment_schema.from_queryset(Consignment.all())
#     return consignments
    
# class Status(BaseModel):
#     message: str


# @app.get("/users", response_model=List[User_Pydantic])
# async def get_users():
#     return await User_Pydantic.from_queryset(Users.all())


# @app.post("/users", response_model=User_Pydantic)
# async def create_user(user: UserIn_Pydantic):
#     user_obj = await Users.create(**user.dict(exclude_unset=True))
#     return await User_Pydantic.from_tortoise_orm(user_obj)


# @app.get(
#     "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
# )
# async def get_user(user_id: int):
#     return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


# @app.put(
#     "/user/{user_id}", response_model=User_Pydantic, responses={404: {"model": HTTPNotFoundError}}
# )
# async def update_user(user_id: int, user: UserIn_Pydantic):
#     await Users.filter(id=user_id).update(**user.dict(exclude_unset=True))
#     return await User_Pydantic.from_queryset_single(Users.get(id=user_id))


# @app.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
# async def delete_user(user_id: int):
#     deleted_count = await Users.filter(id=user_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"User {user_id} not found")
#     return Status(message=f"Deleted user {user_id}")
