import pytest
from time import sleep
from config.env import ConfigReader
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


@pytest.mark.order(14)
def test_e2e(setup_and_teardown, api_client):
    """
    Create note via API,
    Delete note via API,
    Validate note is not visible on UI.
    """

    driver = setup_and_teardown

    token = api_client["token"]
    notes_api = api_client["notes_api"]

    # Step 1: Create note via API
    payload = {
        "title": "E2E Delete Note",
        "description": "will be deleted",
        "category": "Home"
    }

    create_response = notes_api.create_note(token, payload)
    assert create_response.status_code == 200

    note_id = create_response.json()["data"]["id"]
    note_title = create_response.json()["data"]["title"]

    # Step 2: Delete note via API
    delete_response = notes_api.delete_note(note_id, token)
    assert delete_response.status_code in (200, 204)

    # Step 3: Verify note deleted from backend
    get_response = notes_api.get_all_notes(token)
    assert get_response.status_code == 200

    notes = get_response.json()["data"]
    ids = [note["id"] for note in notes]

    assert note_id not in ids, "Deleted note still exists in API response"

    # Step 4: Login via UI
    lp = LoginPage(driver)
    lp.login()
    sleep(2)

    # Step 5: Refresh notes page
    driver.refresh()
    sleep(2)

    # Step 6: Verify deleted note not present on UI
    note_titles = driver.find_elements(
        By.XPATH,
        '//div[@data-testid="note-card-title"]'
    )

    titles = [note.text for note in note_titles]

    assert note_title not in titles, (
        f"Deleted note still visible in UI: {note_title}"
    )
