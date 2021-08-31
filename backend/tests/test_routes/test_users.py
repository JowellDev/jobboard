import json

def test_create_user(client):
    data = {
        "username": "testusername",
        "email": "abc@test.com",
        "password": "123456"
    }

    response = client.post("/users", json.dump(data))
    assert response.status_code == 200