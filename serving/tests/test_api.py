from fastapi.testclient import TestClient
from serving.main import app

client = TestClient(app)

def test_predict_valid_input():
    response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], list)
    assert len(data["prediction"]) == 1

def test_predict_invalid_input():
    response = client.post("/predict", json={"features": "invalid"})
    assert response.status_code == 422  # Erro de validação

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
