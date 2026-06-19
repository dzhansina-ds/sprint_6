from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys

class OrderPage():
   
    def __init__(self, driver):
        self.driver = driver

    def accept_cookie(self):
        try:
            cookie_button = WebDriverWait(self.driver,7).until(expected_conditions.element_to_be_clickable((OrderPageLocators.cookie_button)))
            cookie_button.click()
        except Exception:
            pass

    def click_top_order_button(self):
        self.accept_cookie()
        self.driver.find_element(*OrderPageLocators.top_order_button).click()

    def click_bottom_order_button(self):
        self.accept_cookie()
        element = self.driver.find_element(*OrderPageLocators.bottom_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
    
    def set_name(self,name):
        self.driver.find_element(*OrderPageLocators.name_field).send_keys(name) 

    def set_surname(self,surname):
        self.driver.find_element(*OrderPageLocators.surname_field).send_keys(surname)

    def set_address(self,address):
        self.driver.find_element(*OrderPageLocators.address_field).send_keys(address)

    def set_station(self,station):
        selected_station = self.driver.find_element(*OrderPageLocators.station_field)
        selected_station.send_keys(station)
        selected_station.send_keys(Keys.DOWN,Keys.ENTER)

    def set_phone(self,phone):
        self.driver.find_element(*OrderPageLocators.phone_field).send_keys(phone)

    def click_forward_button(self):
        self.driver.find_element(*OrderPageLocators.forward_button).click()

    def set_order_date(self,date):
        selected_date=self.driver.find_element(*OrderPageLocators.order_date_field)
        selected_date.send_keys(date)
        selected_date.send_keys(Keys.ENTER)
        
    def set_duration_field(self):
        self.driver.find_element(*OrderPageLocators.second_order_header).click()
        self.driver.find_element(*OrderPageLocators.order_duration_field).click()
        self.driver.find_element(*OrderPageLocators.one_day_duration).click()
        
    def set_colour(self):
        self.driver.find_element(*OrderPageLocators.scooter_colour_field).click()
        self.driver.find_element(*OrderPageLocators.black_colour).click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.comment_field).send_keys(comment)
        
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    def click_yes_button(self):
        WebDriverWait(self.driver,7).until(expected_conditions.visibility_of_element_located((OrderPageLocators.yes_button))).click()
 
    def get_text_of_header_success_order (self):
        return self.driver.find_element(*OrderPageLocators.success_order_window_header).text

    def click_header_logo_yandex(self):
        self.driver.find_element(*OrderPageLocators.header_logo_yandex).click()

    def click_header_logo_samokat(self):
        self.driver.find_element(*OrderPageLocators.header_logo_samokat).click()
    
    def make_order (self,order_button_place, name,surname,address,station,phone,date,comment):
        if order_button_place == 'top':
            self.click_top_order_button()
        else:
            self.click_bottom_order_button()
        
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone(phone)
        self.click_forward_button()
        self.set_order_date(date)
        self.set_duration_field()
        self.set_colour()
        self.set_comment(comment)
        self.click_order_button()
        self.click_yes_button()