from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators

class BasePage():
    
    def __init__(self, driver):
        self.driver = driver

    def accept_cookie(self):
        try:
            cookie_button = WebDriverWait(self.driver,7).until(expected_conditions.element_to_be_clickable((BasePageLocators.cookie_button)))
            cookie_button.click()
        except Exception:
            pass

    def find_element(self,locator):
        return self.driver.find_element(*locator)
    
    def find_element_after_waiting(self,locator):
        return WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locator))

    def click_element(self,locator):
        element = WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    def scrolling (self,locator):
        element=self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def text_input(self,locator,text):
        self.find_element(locator).send_keys(text)