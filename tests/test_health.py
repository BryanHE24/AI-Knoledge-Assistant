from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app) # Create a test client for the FastAPI application

# Test the health check endpoint
def test_health():
    response = client.get("/health") # Send a GET request to the health check endpoint

    assert response.status_code == 200 # Check if the response status code is 200
    assert response.json() == {"status": "ok"} # Check if the response JSON is {"status": "ok"}