import requests

def test_generate():
    response = requests.post("http://localhost:8000/generate", json={"prompt": "Hello"})
    assert response.status_code == 200
    assert "response" in response.json()
