from fastapi.testclient import TestClient
from app.api.main import app
# Create a test client for the FastAPI application
client = TestClient(app) 

# Test the query endpoint
def test_query():
    # Send a POST request to the query endpoint
    response = client.post(
        "/query",
        json={"question": "What is RAG?"}
    )
    # Check if the response status code is 200
    assert response.status_code == 200
    # Check if the response JSON contains the answer key
    assert "answer" in response.json()