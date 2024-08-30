from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_checkout_endpoint():
    response = client.post("/checkout", json={"items": "AAABBD"})
    assert response.status_code == 200
    assert response.json() == 190

def test_pricing_rules_endpoint():
    response = client.get("/pricing_rules")
    assert response.status_code == 200
    rules = response.json()
    assert "A" in rules
    assert "unit_price" in rules["A"]
    assert "offer_1_quantity" in rules["A"]
    assert "offer_1_price" in rules["A"]

