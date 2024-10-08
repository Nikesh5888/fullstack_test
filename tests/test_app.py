from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Flight Search API"}

def test_get_flights():
    response = client.get("/flights", params={
        "source": "London",
        "sink": "Paris",
        "departure_date": "2024-10-08",
        "return_date": "2024-10-15"
    })
    assert response.status_code == 200
    assert len(response.json()) > 0
