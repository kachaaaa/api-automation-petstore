import requests

BASE_URL = "https://petstore.swagger.io/v2"


def test_get_created_pet():
    pet_id = 123456

    response = requests.get(f"{BASE_URL}/pet/{pet_id}")

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["id"] == pet_id
    assert response_json["name"] == "QA_Pet"
    assert response_json["status"] == "available"
