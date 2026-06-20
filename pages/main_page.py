from selenium import webdriver  
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from .base_page import BasePage

class MainPage(BasePage):

    def click_first_question_button (self):
        self.scrolling(MainPageLocators.first_question_button)
        self.click_element(MainPageLocators.first_question_button)

    def click_second_question_button (self):
        self.click_element(MainPageLocators.second_question_button)
        
    def click_third_question_button (self):
        self.click_element(MainPageLocators.third_question_button)

    def click_fourth_question_button (self):
        self.click_element(MainPageLocators.fourth_question_button)

    def click_fifth_question_button (self):
        self.click_element(MainPageLocators.fifth_question_button)

    def click_sixth_question_button (self):
        self.click_element(MainPageLocators.sixth_question_button)

    def click_seventh_question_button (self):
        self.click_element(MainPageLocators.seventh_question_button)

    def click_eighth_question_button (self):
        self.click_element(MainPageLocators.eighth_question_button)

    def get_first_question_answer(self):
        return self.find_element_after_waiting(MainPageLocators.first_question_answer)

    def get_second_question_answer(self):
        return self.find_element_after_waiting(MainPageLocators.second_question_answer)

    def get_third_question_answer(self):
        return self.find_element_after_waiting(MainPageLocators.third_question_answer)

    def get_fourth_question_answer(self):
        return self.find_element_after_waiting(MainPageLocators.fourth_question_answer)

    def get_fifth_question_answer(self):
        return self.find_element_after_waiting(MainPageLocators.fifth_question_answer)

    def get_sixth_question_answer(self):
        return self.find_element_after_waiting(MainPageLocators.sixth_question_answer)

    def get_seventh_question_answer(self):
        return self.find_element_after_waiting(MainPageLocators.seventh_question_answer)

    def get_eighth_question_answer(self):
        return self.find_element_after_waiting(MainPageLocators.eighth_question_answer)