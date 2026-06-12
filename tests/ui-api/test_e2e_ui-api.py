from time import sleep
import pytest

from api.auth_api import AuthAPI
from api.notes_api import NotesAPI
from config.env import ConfigReader
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.order(12)
def test_e2e(setup_and_teardown):
	"""Simple E2E: create via API, delete via API, verify absent on UI."""
	driver = setup_and_teardown
	cfg = ConfigReader.read_config()["qa"]

	# API clients
	auth = AuthAPI(cfg["api_base_url"])
	notes = NotesAPI(cfg["api_base_url"])

	# 1) Login via API and get token
	r = auth.login(cfg["username"], cfg["passwd"])
	assert r.status_code == 200
	token = r.json()["data"]["token"]

	# 2) Create note via API
	payload = {"title": "E2E Delete Note", "description": "will be deleted", "category": "Home"}
	cr = notes.create_note(token, payload)
	assert cr.status_code == 200
	note_id = cr.json()["data"]["id"]
	note_title = cr.json()["data"]["title"]

	# 3) Delete via API
	dr = notes.delete_note(note_id, token)
	assert dr.status_code in (200, 204)

	# 4) Confirm backend: note not in GET /notes
	gr = notes.get_all_notes(token)
	assert gr.status_code == 200
	ids = [n["id"] for n in gr.json()["data"]]
	assert note_id not in ids

	# 5) UI: login with UI so the browser session shows the user's notes
	lp = LoginPage(driver)
	lp.login()
	sleep(2)

	# navigate to app base URL and refresh
	if driver.current_url != cfg["base_url"]:
		driver.get(cfg["base_url"])
		sleep(1)
	driver.refresh()
	sleep(2)

	elems = driver.find_elements(By.XPATH, '//div[@data-testid="note-card-title"]')
	titles = [e.text for e in elems]

	assert note_title not in titles, f"Deleted note still visible in UI: {note_title}"
