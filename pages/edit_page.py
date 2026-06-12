from selenium.webdriver.common.by import By
from time import sleep
from config.env import ConfigReader
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select


class EditPage(BasePage):
    edit_btn = (By.XPATH,'(//button[@data-testid="note-edit"])[1]')
    title_btn = (By.ID, 'title')
    description_btn = (By.ID, "description")
    dropdown = (By.ID,"category")
    create_btn = (By.XPATH, '//button[@data-testid="note-submit"]')
    title = (By.XPATH, '//div[@data-testid="note-card-title"]')




    def __init__(self,driver):
        super().__init__(driver)

    def click_edit(self):
        self.click(self.edit_btn)

    def select_category(self, category):
        dropdown_element = self.get_element(self.dropdown)
        Select(dropdown_element).select_by_visible_text(category)

    def enter_title(self,text):
        self.enter_text(self.title_btn,text)

    def enter_description(self,text):
        self.enter_text(self.description_btn,text)

    def click_create_btn(self):
        self.click(self.create_btn)

    def validate_title(self):
        return self.validate_note(self.title)