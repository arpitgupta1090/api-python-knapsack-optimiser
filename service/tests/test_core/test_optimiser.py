from service.openapi.sample_data import model_output, request_body
from service.core.optimiser import optimiser
import pytest


def test_success_optimiser():
    field = request_body.get("fields")[0]
    capacity = field.get("capacity")
    values = field.get("values")
    weights = field.get("weights")
    result = optimiser(values, [weights], [capacity])

    assert result == model_output


# def test_invalid_optimiser_output(mocker):
#     with pytest.raises(Exception):
#         field = request_body.get("fields")[0]
#         capacity = field.get("capacity")
#         values = field.get("values")
#         weights = field.get("weights")
#         result = optimiser(values, [weights], [])
