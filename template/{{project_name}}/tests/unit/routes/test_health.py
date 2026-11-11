from http import HTTPStatus

from flask.testing import FlaskClient


def test_health_check(client: FlaskClient):
    response = client.get("/health")
    assert response.status_code == HTTPStatus.NO_CONTENT
