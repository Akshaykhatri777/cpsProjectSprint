from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait



class LoginPage(BasePage):
    login_button = (By.XPATH,"//a[text()='Login']")
    email_text = (By.XPATH,"//input[@id='email']")
    password_text = (By.XPATH,"//input[@id='password']")
    login_submit = (By.XPATH,"//button[text()='Login']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def click_login(self):
        self.click(self.login_button)

    def enter_username(self, username):
        self.enter_text(self.email_text, username)

    def enter_password(self, password):
        self.enter_text(self.password_text, password)

    def click_submit(self):
        self.click(self.login_submit)