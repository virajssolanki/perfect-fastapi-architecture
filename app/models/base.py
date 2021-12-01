from tortoise.models import Model
from tortoise import fields


class BaseModel(Model):
    created = fields.DatetimeField(auto_now_add=True)
        