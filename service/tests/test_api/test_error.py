from unittest import mock
import pytest
from service.tests import client
from service.openapi.sample_data import request_body, model_output
from copy import deepcopy


@mock.patch("service.api.api_router.optimiser", return_value=model_output, autospec=True)
def test_empty_body(mocker):
    response = client.post("/api/optimiser", json={})
    assert response.status_code == 400
    for error in response.json().get("errors"):
        assert error.get("code") == "KSO_INPUT_0001"


@mock.patch("service.api.api_router.optimiser", return_value=model_output, autospec=True)
def test_no_body(mocker):
    response = client.post("/api/optimiser")
    assert response.status_code == 400
    for error in response.json().get("errors"):
        assert error.get("code") == "KSO_INPUT_0001"


@mock.patch("service.api.api_router.optimiser", return_value=model_output, autospec=True)
def test_body_missing_data(mocker):
    temp_request_body = deepcopy(request_body)
    del temp_request_body["request_version"]
    response = client.post("/api/optimiser", json=temp_request_body)
    del temp_request_body
    assert response.status_code == 400
    for error in response.json().get("errors"):
        assert error.get("code") == "KSO_INPUT_0001"


@mock.patch("service.api.api_router.optimiser", return_value=model_output, autospec=True)
def test_body_invalid_data(mocker):
    temp_request_body = deepcopy(request_body)
    temp_request_body["fields"][0]["capacity"] = "string"
    response = client.post("/api/optimiser", json=temp_request_body)
    del temp_request_body
    assert response.status_code == 400
    for error in response.json().get("errors"):
        assert error.get("code") == "KSO_INPUT_0002"


@mock.patch("service.api.api_router.optimiser", return_value=model_output, autospec=True)
def test_body_invalid_json(mocker):
    temp_request_body = "string, not a json"
    response = client.post("/api/optimiser", content=temp_request_body)
    del temp_request_body
    assert response.status_code == 400
    for error in response.json().get("errors"):
        assert error.get("code") == "KSO_INPUT_0003"


@mock.patch("service.api.api_router.optimiser", return_value=model_output, autospec=True)
def test_invalid_method(mocker):
    response = client.get("/api/optimiser")
    assert response.status_code == 405
    for error in response.json().get("errors"):
        assert error.get("code") == "KSO_GENERAL_0000"


@mock.patch("service.api.api_router.optimiser", return_value=model_output, autospec=True)
def test_invalid_endpoint(mocker):
    response = client.post("/api/invalid_optimiser")
    assert response.status_code == 404
    for error in response.json().get("errors"):
        assert error.get("code") == "KSO_GENERAL_0000"


@mock.patch("service.api.api_router.optimiser", return_value={}, autospec=True)
def test_invalid_optimiser_output(mocker):
    with pytest.raises(Exception):
        response = client.post("/api/optimiser", json=request_body)


@mock.patch("service.api.api_router.optimiser", return_value={}, autospec=True, side_effect=Exception)
def test_invalid_optimiser_output2(mocker):
    response = client.post("/api/optimiser", json=request_body)
    assert response.status_code == 422
    for error in response.json().get("errors"):
        assert error.get("code") == "KSO_GENERAL_0000"
