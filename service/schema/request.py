from pydantic import BaseModel
from typing import List


class Fields(BaseModel):
    capacities: List[int]
    values: List[int]
    weights: List[List[int]]


class RequestModel(BaseModel):
    request_version: int
    fields: List[Fields]
