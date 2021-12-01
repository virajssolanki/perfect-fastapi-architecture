from tortoise import fields
from tortoise.validators import *
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from app.models.base import BaseModel

#models and schemas both can be here or we can use seprate file for schemas
#model
class Consignment(BaseModel):
    id = fields.IntField(pk=True)
    bl_number = fields.CharField(max_length=100)
    created = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.bl_number

#schemas
add_consignment_schema = pydantic_model_creator(
    Consignment, 
    exclude = ["id", "created"]
    )

list_consignment_schema = pydantic_queryset_creator(
    Consignment
    )