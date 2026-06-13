import pytest
@pytest.mark.api
@pytest.mark.order(11)
def test_delete_note_api(api_client):

    notes_api = api_client["notes_api"]
    token     = api_client["token"]

    create_response = notes_api.create_note(token, {
        "title":       "Note To Delete",
        "description": "Created for delete testing",
        "category":    "Work"
    })
    assert create_response.status_code == 200
    note_id = create_response.json()["data"]["id"]

    delete_response = notes_api.delete_note(note_id, token)
    assert delete_response.status_code in [200, 204]

    updated_notes = notes_api.get_all_notes(token).json()["data"]
    deleted = next((n for n in updated_notes if n["id"] == note_id), None)
    assert deleted is None, f"Deleted note {note_id} still exists"