import requests

BASE_URL = "https://petstore.swagger.io/v2"


def test_create_pet():
    payload = {
        "id": 123456,
        "name": "QA_Pet",
        "status": "available"
    }

    response = requests.post(
        f"{BASE_URL}/pet",
        json=payload
    )

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["name"] == "QA_Pet"
    assert response_json["status"] == "available"
