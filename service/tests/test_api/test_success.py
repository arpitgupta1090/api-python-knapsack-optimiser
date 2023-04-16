from unittest import mock
from service.tests import client
from service.openapi.sample_data import request_body, model_output


@mock.patch("service.api.api_router.optimiser", return_value=model_output, autospec=True)
def test_success(mocker):
    response = client.post("/api/optimiser", json=request_body)
    assert response.status_code == 200
    assert len(response.json().get("results")) > 0
    assert response.json().get("metadata").get("optimiser") == request_body.get("optimiser")
    assert len(response.json().get("results")[0]) > 0

