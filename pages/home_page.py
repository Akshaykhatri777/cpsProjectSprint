from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class HomePage(BasePage):
    add_note_button = (By.XPATH,"//button[text()='+ Add Note']")
    dropdown = (By.ID,"category")
    title_text = (By.XPATH,"//input[@id='title']")
    description_text = (By.XPATH,"//textarea[@id='description']")
    submit_note = (By.XPATH,"//button[text()='Create']")
    title = (By.XPATH, '//div[@data-testid="note-card-title"]')
    desc = (By.XPATH, '//p[@data-testid="note-card-description"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_add(self):
        self.click(self.add_note_button)

    def enter_title(self, title):
        self.enter_text(self.title_text, title)

    def enter_description(self, description):
        self.enter_text(self.description_text, description)

    def click_create(self):
        self.click(self.submit_note)

    def select_category(self, category):
        dropdown_element = self.get_element(self.dropdown)
        Select(dropdown_element).select_by_visible_text(category)

    def validate_title(self):
        return self.validate_note(self.title)

    def validate_description(self):
        return self.validate_note(self.desc)