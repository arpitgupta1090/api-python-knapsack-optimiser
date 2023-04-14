from pydantic import BaseModel
from typing import List
from service.openapi.sample_data import request_body


class Optimiser(BaseModel):
    name: str
    type: str
    version: str


class Fields(BaseModel):
    capacity: int
    values: List[int]
    weights: List[int]


class RequestModel(BaseModel):
    request_version: str
    optimiser: Optimiser
    fields: List[Fields]

    class Config:
        schema_extra = {
            "example": request_body
        }
