from fastapi.exceptions import HTTPException
from typing import List

from fastapi import APIRouter

from app.repos import all_consignments
from app.schemas import list_consignment_schema, add_consignment_schema

router = APIRouter()

#write api endpoints here

@router.post("/consignment", response_model=add_consignment_schema)
async def consignment(data: add_consignment_schema):
    return await add_consignment_schema(data.dict())

@router.get("/consignments")
async def all_consignment():
    return await all_consignments()