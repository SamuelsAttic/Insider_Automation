import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_create_pet_positive():
    url = f"{BASE_URL}/pet"
    data = {
        "id": 1,
        "category": {"id": 1, "name": "Dog"},
        "name": "Rex",
        "photoUrls": ["http://example.com/photo1"],
        "tags": [{"id": 1, "name": "Tag1"}],
        "status": "available"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Rex"

def test_create_pet_negative():
    url = f"{BASE_URL}/pet"
    data = {
        "id": "12345fjf",
        "category": {"id": 1, "name": "Dog"},
        "photoUrls": ["http://example.com/photo2"],
        "tags": [{"id": 1, "name": "Tag2"}],
        "status": "available"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400 


def test_get_pet_by_id_positive():
    pet_id = 1
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["name"] == "Rex"

def test_get_pet_negative():
    pet_id = 99999  
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    assert response.status_code == 404  
    assert "Pet not found" in response.text

def test_update_pet_positive():
    url = f"{BASE_URL}/pet"
    data = {
        "id": 1,
        "category": {"id": 1, "name": "Dog"},
        "name": "Max",
        "photoUrls": ["http://example.com/photo1"],
        "tags": [{"id": 1, "name": "Tag1"}],
        "status": "sold"
    }
    response = requests.put(url, json=data)
    assert response.status_code == 200
    assert response.json()["name"] == "Max"

def test_update_pet_negative():
    url = f"{BASE_URL}/pet"
    data = {
        "id": "12345fjf",
        "category": {"id": 1, "name": "Dog"},
        "name": "Max",
        "photoUrls": ["http://example.com/photo1"],
        "tags": [{"id": 1, "name": "Tag1"}],
        "status": ''
    }
    response = requests.put(url, json=data)
    assert response.status_code == 400 

def test_delete_pet_positive():
    pet_id = 1
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.delete(url)
    assert response.status_code == 200
    assert "message" in response.json()

def test_delete_pet_negative():
    pet_id = 99999 
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.delete(url)
    assert response.status_code == 404 
