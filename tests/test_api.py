from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_generate():
    response = client.post("/api/generate", json={
        "prompt": "On-prem applications connect securely through VPN to cloud APIs and databases."
    })
    assert response.status_code == 200
    body = response.json()
    assert "architecture" in body
    assert "graph" in body
    assert body["analysis"]["validation"]["valid"]
