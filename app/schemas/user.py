from tortoise.contrib.pydantic import pydantic_model_creator
from app.models import User

from pydantic import BaseModel, ValidationError, validator
from pydantic import EmailStr, SecretStr


class CreateUserSchema(BaseModel):
    email: EmailStr
    password: SecretStr

user_schema = pydantic_model_creator(
    User, 
    name='UserSchema', 
    exclude = ["hashed_password"]
    )