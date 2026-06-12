import pytest

from config.env import ConfigReader
from pages.login_page import LoginPage
from pages.home_page import HomePage
from time import sleep

@pytest.mark.order(13)
def test_validate_note(setup_and_teardown, api_client):
    """Create a note via UI, then validate it exists via API."""
    driver = setup_and_teardown
    config = ConfigReader.read_config()["note_data"]

    token = api_client["token"]
    notes_api = api_client["notes_api"]

    # Step 1: Login via UI
    lp = LoginPage(driver)
    lp.login()
    sleep(2)

    # Step 2: Create note via UI
    hp = HomePage(driver)
    hp.click_add()
    sleep(1)
    hp.select_category(config["category"])
    hp.enter_title(config["note_title"])
    hp.enter_description(config["note_desc"])
    hp.click_create()
    sleep(2)

    # Step 3: Validate note exists via API
    response = notes_api.get_all_notes(token)
    assert response.status_code == 200

    notes = response.json()["data"]
    found = next(
        (n for n in notes
         if n["title"] == config["note_title"] and
            n["description"] == config["note_desc"]),
        None
    )
    assert found is not None, "Note not found in API response"
