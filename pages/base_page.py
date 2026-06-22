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
        return WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located((locator)))

    def click_element(self,locator):
        element = WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable((locator)))
        element.click()

    def scrolling (self,locator):
        element=self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def text_input(self,locator,text):
        self.find_element(locator).send_keys(text)

    def get_current_url (self):
        return self.driver.current_url
    
    def switch_window(self,original_window):
        WebDriverWait(self.driver, 7).until(expected_conditions.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    def waiting_text_in_url (self,text):
        WebDriverWait(self.driver, 7).until(expected_conditions.url_contains(text))

    def get_current_window_handle(self):
        return self.driver.current_window_handle
 