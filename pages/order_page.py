from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class OrderPage(BasePage):

    def click_top_order_button(self):
        self.accept_cookie()
        self.click_element(BasePageLocators.top_order_button)

    def click_bottom_order_button(self):
        self.accept_cookie()
        self.scrolling(BasePageLocators.bottom_order_button)
        self.click_element(BasePageLocators.bottom_order_button)

    def set_name(self,name):
        self.text_input(OrderPageLocators.name_field,name) 

    def set_surname(self,surname):
        self.text_input(OrderPageLocators.surname_field,surname)

    def set_address(self,address):
        self.text_input(OrderPageLocators.address_field,address)

    def set_station(self,station):
        self.text_input(OrderPageLocators.station_field,station)
        self.find_element(OrderPageLocators.station_field).send_keys(Keys.DOWN,Keys.ENTER)

    def set_phone(self,phone):
        self.text_input(OrderPageLocators.phone_field,phone)

    def click_forward_button(self):
        self.click_element(OrderPageLocators.forward_button)

    def set_order_date(self,date):
        self.text_input(OrderPageLocators.order_date_field,date)
        self.find_element(OrderPageLocators.order_date_field).send_keys(Keys.ENTER)
        
    def set_duration_field(self):
        self.click_element(OrderPageLocators.second_order_header)
        self.click_element(OrderPageLocators.order_duration_field)
        self.click_element(OrderPageLocators.one_day_duration)
        
    def set_colour(self):
        self.click_element(OrderPageLocators.scooter_colour_field)
        self.click_element(OrderPageLocators.black_colour)

    def set_comment(self, comment):
        self.text_input(OrderPageLocators.comment_field,comment)
        
    def click_order_button(self):
        self.click_element(OrderPageLocators.order_button)

    def click_yes_button(self):
        self.find_element_after_waiting(OrderPageLocators.yes_button).click()
 
    def get_text_of_header_success_order (self):
        return self.find_element(OrderPageLocators.success_order_window_header).text

    def click_header_logo_yandex(self):
        self.click_element(BasePageLocators.header_logo_yandex)

    def click_header_logo_samokat(self):
        self.click_element(BasePageLocators.header_logo_samokat)
    
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