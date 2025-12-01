import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test to check if the /inventory/{store_id} endpoint returns the inventory for a store
def test_get_inventory():
    store_id = 101  # Replace with a store that exists in your database
    response = client.get(f"/inventory/{store_id}")
    
    # Assert if the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response body is a list (inventory items)
    assert isinstance(response.json(), list)

    # Assert that each inventory item contains the required fields
    for item in response.json():
        assert "product_id" in item
        assert "quantity" in item
        assert "last_updated" in item

# Test to check if empty inventory returns an empty list
def test_get_empty_inventory():
    store_id = 999  # Use a store_id that doesn't exist in your database
    response = client.get(f"/inventory/{store_id}")

    assert response.status_code == 200
    assert response.json() == []

# Test to check if correct inventory details are returned for store_id 101
def test_get_inventory_details():
    store_id = 101
    response = client.get(f"/inventory/{store_id}")

    # Check that the inventory for store 101 matches the expected data
    inventory_data = response.json()

    # Assume product_id 2001 is in store 101's inventory with a quantity of 50
    inventory_item = next((item for item in inventory_data if item["product_id"] == 2001), None)
    assert inventory_item is not None
    assert inventory_item["quantity"] == 50
