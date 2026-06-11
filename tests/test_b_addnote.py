from config.env import ConfigReader
from pages.home_page import HomePage

from time import sleep

from utils.screenshot import take_screenshot


def test_addnote(setup_and_teardown):
    driver = setup_and_teardown
    hp = HomePage(driver)

    config = ConfigReader.read_config()["note_data"]

    category = config["category"]
    title = config["note_title"]
    desc = config["note_desc"]

    hp.click_add()
    sleep(1)
    hp.select_category(category)
    hp.enter_title(title)
    hp.enter_description(desc)
    hp.click_create()

    assert hp.validate_title() == "Test Note","Note not created"
    assert hp.validate_description() == "This is a test note","Note description not matching"

def test_addnote2(setup_and_teardown):
    driver = setup_and_teardown
    hp = HomePage(driver)

    config = ConfigReader.read_config()["note_invalid_data"]

    category = config["category"]
    title = config["note_title"]
    desc = config["note_desc"]

    sleep(5)
    hp.click_add()
    sleep(1)
    hp.select_category(category)
    hp.enter_title(title)
    hp.enter_description(desc)
    hp.click_create()

    try:
        assert hp.validate_title() == "","Note not created"
    except AssertionError:
        take_screenshot(driver,'add_note_invalid.png')



