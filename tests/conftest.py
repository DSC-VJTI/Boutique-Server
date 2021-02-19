import pytest
from fastapi.testclient import TestClient
from src.app.main import app


@pytest.fixture(scope="module")
def client():
    test_client = TestClient(app)
    yield test_client
