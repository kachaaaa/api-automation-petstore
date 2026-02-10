import requests


def test_get_pet_by_id():
    pet_id = 1
    url = f"https://petstore.swagger.io/v2/pet/{pet_id}"

    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()["id"] == pet_id
