# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)

#     def click(self, locator):
#         self.wait.until(EC.element_to_be_clickable(locator)).click()

#     def enter_text(self, locator, text):
#         self.wait.until(EC.visibility_of_element_located(locator)).clear()
#         self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

#     def get_text(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator)).text

#     def is_visible(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator))

#     def get_element(self, locator):
#         return self.wait.until(
#             EC.visibility_of_element_located(locator)
#         )

#     def validate_note(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator)).text

#     def scroll(self):
#         actions = ActionChains(self.driver)
#         actions.scroll_by_amount(0,300).perform()

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)

#     def click(self, locator):
#         self.wait.until(EC.element_to_be_clickable(locator)).click()

#     def enter_text(self, locator, text):
#         self.wait.until(EC.visibility_of_element_located(locator)).clear()
#         self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

#     def get_text(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator)).text

#     def is_visible(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator))

#     def get_element(self, locator):
#         return self.wait.until(
#             EC.visibility_of_element_located(locator)
#         )

#     def validate_note(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator)).text

#     def scroll(self):
#         actions = ActionChains(self.driver)
#         actions.scroll_by_amount(0,300).perform()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def is_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def get_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def validate_note(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def scroll(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 300).perform()
