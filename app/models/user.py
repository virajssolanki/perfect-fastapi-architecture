from tortoise import fields
from typing import Optional
from tortoise.validators import *
from tortoise.exceptions import DoesNotExist

from app.models.base import BaseModel


class User(BaseModel):
    """
    The User model
    """
    email = fields.CharField(unique=True, null=False, max_length=255)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    hashed_password = fields.CharField(max_length=200, null=True)
    is_active = fields.BooleanField(null=False, default=True)

    def full_name(self) -> str:
        """
        Returns the full name
        """
        if self.first_name or self.last_name:
            return f"{self.first_name or ''} {self.last_name or ''}".strip()
        return ''

    @classmethod
    async def get_by_email(cls, email: str) -> Optional["User"]:
        try:
            query = cls.get_or_none(email=email)
            user = await query
            return user
        except DoesNotExist:
            return None

    class Meta:
        table: str = 'user'
    
    class PydanticMeta:
        computed = ["full_name"]
        exclude = ["hashed_password"]
