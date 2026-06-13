import pytest
from config.env import ConfigReader

@pytest.mark.api
@pytest.mark.order(8)
def test_create_note(api_client):
    config = ConfigReader.read_config()
    note_data = config["note_data"]

    token = api_client["token"]
    notes_api = api_client["notes_api"]

    payload = {
        "title": note_data["note_title"],
        "description": note_data["note_desc"],
        "category": "Home"
    }

    response = notes_api.create_note(token, payload)

    assert response.status_code == 200

    response_data = response.json()["data"]

    assert response_data["title"] == payload["title"]
    assert response_data["description"] == payload["description"]
    assert response_data["category"] == payload["category"]


@pytest.mark.api
@pytest.mark.order(9)
def test_create_note_invalid(api_client):

    token = api_client["token"]
    notes_api = api_client["notes_api"]

    payload = {
        "title": "",
        "description": "Test Description",
        "category": "Home"
    }

    response = notes_api.create_note(token, payload)

    assert response.status_code == 400
    assert "Title" in response.json()["message"]
