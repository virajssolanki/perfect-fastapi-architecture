from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from app.models import Consignment


add_consignment_schema = pydantic_model_creator(
    Consignment, 
    exclude = ["id", "created"]
    )

list_consignment_schema = pydantic_queryset_creator(
    Consignment
    )