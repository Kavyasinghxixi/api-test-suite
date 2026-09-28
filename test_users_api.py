import requests

BASE_URL = "https://reqres.in/api"

def test_get_single_user_status_code():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200

def test_get_single_user_returns_correct_id():
    response = requests.get(f"{BASE_URL}/users/2")
    data = response.json()
    assert data["data"]["id"] == 2

def test_get_nonexistent_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/999")
    assert response.status_code == 404

def test_create_user_returns_201():
    payload = {"name": "Kavya", "job": "SDET"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Kavya"

def test_get_user_with_invalid_id_format():
    response = requests.get(f"{BASE_URL}/users/abc")
    assert response.status_code == 404

def test_create_user_with_empty_payload():
    response = requests.post(f"{BASE_URL}/users", json={})
    assert response.status_code == 201  # reqres accepts anything, but check the structure
    assert "id" in response.json()

def test_response_time_is_reasonable():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.elapsed.total_seconds() < 2