from fastapi import APIRouter
from service.core.optimiser import optimiser
from service.openapi.api_spec import additional_responses
from service.schema.request import RequestModel
from service.schema.response import ResponseModel

router = APIRouter(
    prefix="/api",
)


@router.post("/optimiser", tags=["API"], response_model_exclude_none=True,
             summary="Get optimised data for your knapsack",
             response_model=ResponseModel, responses=additional_responses)
def optimised_data(request: RequestModel):
    results = dict()
    metadata = {"optimiser": {
        "name": "Knapsack Optimiser",
        "type": "zero-one",
        "version": "v1.0"
    }}
    fields = request.fields[0]
    result = optimiser(fields.values, [fields.weights], [fields.capacity])
    # result = []
    # results = optimiser([1, 2, 3], [[4, 5, 1]], [4])

    results["total_value"] = result[0]
    results["total_weight"] = result[1]
    results["values"] = result[2]
    results["weights"] = result[3]
    return {"metadata": metadata, "results": [results]}
