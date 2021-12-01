from app.schemas import *
from typing import List

#write crud and business logics here
async def add_consignment(data:add_consignment_schema) -> add_consignment_schema:
    consignment = await Consignment.create(**data)
    return consignment

async def all_consignments() -> list_consignment_schema:
    consignments = await list_consignment_schema.from_queryset(Consignment.all())
    return consignments