import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test to check if the /stores endpoint returns a list of stores
def test_get_all_stores():
    response = client.get("/stores/")
    
    # Assert if the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response body is a list
    assert isinstance(response.json(), list)

    # Assert that each store object contains specific keys
    for store in response.json():
        assert "store_id" in store
        assert "store_name" in store
        assert "region" in store
        assert "status" in store

# Test to check if a store returns correct data
def test_get_store_by_id():
    store_id = 101  # Replace with a store that exists in your database
    response = client.get(f"/stores/{store_id}")

    assert response.status_code == 200
    store = response.json()

    # Check the data for store 101 (adjust these values according to your test data)
    assert store["store_id"] == store_id
    assert store["store_name"] == "Amsterdam Central Store"
    assert store["region"] == "EU-West"
    assert store["status"] == "Active"
