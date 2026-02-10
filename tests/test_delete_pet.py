import requests

BASE_URL = "https://petstore.swagger.io/v2"


def test_delete_pet():
    pet_id = 123456

    delete_response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert delete_response.status_code == 200

    get_response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert get_response.status_code == 404
