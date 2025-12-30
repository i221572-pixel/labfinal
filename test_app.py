import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_health_route(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["health"] == "healthy"
