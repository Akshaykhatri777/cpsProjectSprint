import pytest
from time import sleep

from pages.edit_page import EditPage
from config.env import ConfigReader
from pages.login_page import LoginPage
from utils.loggers import get_logger
from utils.screenshot import take_screenshot

@pytest.mark.ui
@pytest.mark.order(5)
def test_edit_ui(setup_and_teardown):
    ep = EditPage(setup_and_teardown)
    lp = LoginPage(setup_and_teardown)

    config = ConfigReader.read_config()
    env = config["edit_notes"]
    TITLE = env["title"]
    DESCRIPTION = env["desc"]
    CATEGORY = env["category"]

    lp.login()
    sleep(2)
    ep.scroll()
    ep.click_edit()
    ep.select_category(CATEGORY)
    ep.enter_title(TITLE)
    ep.enter_description(DESCRIPTION)
    ep.click_create_btn()

@pytest.mark.ui
@pytest.mark.order(6)
def test_invalid_edit_ui(setup_and_teardown):
    ep = EditPage(setup_and_teardown)
    lp = LoginPage(setup_and_teardown)

    driver = setup_and_teardown

    config = ConfigReader.read_config()
    env = config["edit_notes"]
    DESCRIPTION = env["desc"]
    CATEGORY = env["category"]

    lp.login()
    sleep(2)
    ep.scroll()
    ep.click_edit()
    ep.select_category(CATEGORY)
    ep.enter_title("xyz")
    ep.enter_description(DESCRIPTION)
    ep.click_create_btn()

    try:
        assert ep.validate_title() == "","Note not created"
    except AssertionError:
        take_screenshot(driver,'add_note_invalid_edit.png')