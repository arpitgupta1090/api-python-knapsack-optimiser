from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from service.core.optimiser import optimiser
from service.openapi.api_spec import additional_responses
from service.schema.request import RequestModel
from service.schema.response import ResponseModel
from service.mapper.response_mapper import mapper

router = APIRouter(prefix="/api")


@router.post("/optimiser", tags=["API"], response_model_exclude_none=True,
             summary="Get optimised data for your knapsack",
             response_model=ResponseModel, responses=additional_responses)
def optimised_data(request: RequestModel):
    input_field = request.fields[0]
    try:
        result = optimiser(input_field.values, [input_field.weights], [input_field.capacity])
    except Exception as exc:
        raise HTTPException(422, exc)
    return mapper(request, result)
