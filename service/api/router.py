from fastapi import APIRouter
from service.core.optimiser import optimiser
from service.core.sample_data import values, weights, capacities
from service.schema.request import RequestModel

router = APIRouter(
    prefix="/api",
)


@router.post("/optimiser", tags=["Optimiser"], response_model_exclude_none=True, summary="Get optimised data for your "
                                                                                         "knapsack ")
def optimised_data(request: RequestModel):
    output = dict()
    fields = request.fields[0]
    results = optimiser(fields.values, fields.weights, fields.capacities)
    # results = optimiser([1, 2, 3], [[4, 5, 1]], [4])

    output["total_value"] = results[0]
    output["total_weight"] = results[1]
    output["packed_values"] = results[2]
    output["packed_weights"] = results[3]
    return output
