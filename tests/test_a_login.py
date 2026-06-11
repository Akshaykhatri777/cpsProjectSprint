from config.env import ConfigReader
from pages.login_page import LoginPage
from time import sleep

from utils.screenshot import take_screenshot
from utils.loggers import get_logger



def test_invalid_login(setup_and_teardown):
    driver = setup_and_teardown
    lp = LoginPage(driver)

    config = ConfigReader.read_config()["invalid"]

    username = config["username"]
    password = config["passwd"]

    # get_logger().info("Testing invalid login with username: %s", username)

    lp.scroll()
    lp.click_login()
    sleep(1)

    lp.scroll()
    lp.enter_username(username)
    lp.enter_password(password)
    lp.click_submit()

    sleep(1)
    take_screenshot(driver,'invalid_login.png')
    sleep(1)

    assert driver.current_url == "https://practice.expandtesting.com/notes/app/login"

    # driver.refresh()

def test_valid_login(setup_and_teardown):
    driver = setup_and_teardown
    lp = LoginPage(driver)

    config = ConfigReader.read_config()["qa"]

    username = config["username"]
    password = config["passwd"]

    get_logger().info("Testing valid login with username: %s", username)


    sleep(2)
    lp.click_login()

    sleep(1)
    lp.scroll()
    lp.enter_username(username)
    lp.enter_password(password)
    lp.click_submit()
    sleep(2)

    assert driver.current_url == "https://practice.expandtesting.com/notes/app"

