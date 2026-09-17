from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """ამოწმებს Root/Health ენდპოინტს"""
    response = client.get("/")
    assert response.status_code == 200

def test_predict_endpoint():
    """ამოწმებს Fraud Prediction-ს 30-ელემენტიანი მასივით"""
    payload = {
        "features": [0.0] * 30
    }
    response = client.post("/predict", json=payload)
    
    # თუ API პირდაპირ სიაში ელოდება ველებს payload-ის გარეშე:
    if response.status_code == 422:
        # გადავცემთ ალტერნატიულ სტრუქტურას (30 ნული)
        payload = [0.0] * 30
        response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "is_fraud" in data or "prediction" in data