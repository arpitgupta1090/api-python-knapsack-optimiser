from enum import Enum
from pydantic import BaseModel, StrictInt, root_validator
from typing import List
from service.openapi.sample_data import request_body


class EnumOptimiserName(str, Enum):
    NAME = "Knapsack Optimiser"


class EnumOptimiserType(str, Enum):
    TYPE_ZERO_ONE = "zero-one"
    TYPE_PARTIAL = "partial"


class EnumOptimiserVersion(str, Enum):
    VERSION1_0 = "v1.0"


class Optimiser(BaseModel):
    name: EnumOptimiserName
    type: EnumOptimiserType
    version: EnumOptimiserVersion


class Fields(BaseModel):
    capacity: StrictInt
    values: List[StrictInt]
    weights: List[StrictInt]

    @root_validator(pre=True, allow_reuse=True)
    def check_names_differs(cls, value: dict):
        values = value.get('values')
        weights = value.get('weights')

        if len(values) != len(weights):
            raise ValueError(f"Number of elements in values and weights must be same.")
        return value


class RequestModel(BaseModel):
    request_version: str
    optimiser: Optimiser
    fields: List[Fields]

    class Config:
        schema_extra = {
            "example": request_body
        }
