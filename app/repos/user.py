from app.schemas import user_schema
from app.models import User
from typing import List
from app.repos import get_password_hash

async def create_user(data:user_schema) -> user_schema:
    user = await  User.create(
        email=data.email,
        hashed_password=get_password_hash(
            data.password.get_secret_value()
        )
    )  
    return user

