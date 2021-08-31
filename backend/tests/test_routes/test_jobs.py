import json


def test_create_job(client):
    data = {
        "title": "t",
        "company": "c",
        "company_url": "cu",
        "location": "l",
        "description": "d"
    }

    response = client.post('/jobs/', json.dumps(data))
    assert response.status_code == 200