import pytest

@pytest.mark.api
@pytest.mark.order(12)
def test_edit_note_api(api_client):

    notes_api = api_client["notes_api"]
    token     = api_client["token"]

    # Step 1: Note create karo
    create_response = notes_api.create_note(token, {
        "title":       "Original Title",
        "description": "Original Description",
        "category":    "Work"
    })
    assert create_response.status_code == 200
    note_id = create_response.json()["data"]["id"]

    # Step 2: Same note update karo
    update_response = notes_api.update_note(note_id, token, {
        "title":       "Updated Title",
        "description": "Updated Description",
        "category":    "Home",
        "completed":   True
    })
    assert update_response.status_code == 200
    assert update_response.json()["success"] is True

    # Step 3: Response mein verify karo
    data = update_response.json()["data"]
    assert data["title"]       == "Updated Title"
    assert data["description"] == "Updated Description"
    assert data["category"]    == "Home"
    assert data["completed"]   is True

    # Step 4: GET se double confirm
    all_notes  = notes_api.get_all_notes(token).json()["data"]
    found_note = next((n for n in all_notes if n["id"] == note_id), None)

    assert found_note is not None
    assert found_note["title"]       == "Updated Title"
    assert found_note["description"] == "Updated Description"

@pytest.mark.api
@pytest.mark.order(13)
def test_edit_note_invalid_api(api_client):
    notes_api = api_client["notes_api"]
    token = api_client["token"]
    create_response = notes_api.create_note(token, {
        "title": "Original Title",
        "description": "Original Description",
        "category": "Work"
    })
    assert create_response.status_code == 200
    note_id = create_response.json()["data"]["id"]

    update_response = notes_api.update_note(note_id, token, {
        "title": "xyz",
        "description": "Updated Description",
        "category": "Home"
    })
    assert update_response.status_code == 400
