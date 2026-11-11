from fastapi import status
from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    response = client.get("/health")
    assert response.status_code == status.HTTP_204_NO_CONTENT
