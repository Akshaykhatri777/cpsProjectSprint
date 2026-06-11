import pytest
from selenium import webdriver
from config.env import ConfigReader
from api.auth_api import AuthAPI
from api.notes_api import NotesAPI
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def setup_and_teardown():
    base_url = ConfigReader.read_config()["qa"]["base_url"]

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)

    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def api_client():

    config = ConfigReader.read_config()["qa"]
    api_url = ConfigReader.read_config()["qa"]["api_base_url"]

    auth_api = AuthAPI(api_url)

    login_response = auth_api.login(
        config["username"],
        config["passwd"]
    )

    assert login_response.status_code == 200, "API Login Failed"

    token = login_response.json()["data"]["token"]

    return {
        "token": token,
        "notes_api": NotesAPI(config["api_base_url"])
    }
