from pydantic import BaseModel
from typing import List


class Optimiser(BaseModel):
    name: str
    type: str
    version: str


class Metadata(BaseModel):
    optimiser: Optimiser


class Result(BaseModel):
    total_value: int
    total_weight: int
    values: List[int]
    weights: List[int]


class ResponseModel(BaseModel):
    metadata: Metadata
    results: List[Result]
