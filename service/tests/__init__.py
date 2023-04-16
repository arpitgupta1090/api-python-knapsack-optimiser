from fastapi.testclient import TestClient

from service.main import app

client = TestClient(app)
