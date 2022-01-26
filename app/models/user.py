from tortoise import fields
from tortoise.validators import *

from app.models.base import BaseModel

class User(BaseModel):
    """
    The User model
    """
    email = fields.CharField(max_length=100, unique=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    hashed_password = fields.CharField(max_length=200, null=True)
    refresh_token = fields.UUIDField(null=True)

    def full_name(self) -> str:
        """
        Returns the best name
        """
        if self.first_name or self.last_name:
            return f"{self.first_name or ''} {self.last_name or ''}".strip()

    class PydanticMeta:
        computed = ["full_name"]
        exclude = ["hashed_password"]
