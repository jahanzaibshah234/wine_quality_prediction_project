from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_read_root():
    # This simulates a user visiting the homepage/root of your API
    response = client.get("/")
    
    # We expect the server to respond with a 200 OK status
    assert response.status_code == 200

def test_dummy_math():
    # A simple sanity check that will always pass
    assert 1 + 1 == 2
