from selenium import webdriver  
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainPage():
   
    def __init__(self, driver):
        self.driver = driver

    def click_first_question_button (self):
        element = self.driver.find_element(*MainPageLocators.first_question_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_second_question_button (self):
        self.driver.find_element(*MainPageLocators.second_question_button).click()
        
    def click_third_question_button (self):
        self.driver.find_element(*MainPageLocators.third_question_button).click()

    def click_fourth_question_button (self):
        self.driver.find_element(*MainPageLocators.fourth_question_button).click()

    def click_fifth_question_button (self):
        self.driver.find_element(*MainPageLocators.fifth_question_button).click()

    def click_sixth_question_button (self):
        self.driver.find_element(*MainPageLocators.sixth_question_button).click()

    def click_seventh_question_button (self):
        self.driver.find_element(*MainPageLocators.seventh_question_button).click()

    def click_eighth_question_button (self):
        self.driver.find_element(*MainPageLocators.eighth_question_button).click()

    def get_first_question_answer(self):
        return WebDriverWait(self.driver,7).until(expected_conditions.visibility_of_element_located((MainPageLocators.first_question_answer)))

    def get_second_question_answer(self):
        return WebDriverWait(self.driver,7).until(expected_conditions.visibility_of_element_located((MainPageLocators.second_question_answer)))

    def get_third_question_answer(self):
        return WebDriverWait(self.driver,7).until(expected_conditions.visibility_of_element_located((MainPageLocators.third_question_answer)))

    def get_fourth_question_answer(self):
        return WebDriverWait(self.driver,7).until(expected_conditions.visibility_of_element_located((MainPageLocators.fourth_question_answer)))

    def get_fifth_question_answer(self):
        return WebDriverWait(self.driver,7).until(expected_conditions.visibility_of_element_located((MainPageLocators.fifth_question_answer)))

    def get_sixth_question_answer(self):
        return WebDriverWait(self.driver,7).until(expected_conditions.visibility_of_element_located((MainPageLocators.sixth_question_answer)))

    def get_seventh_question_answer(self):
        return WebDriverWait(self.driver,7).until(expected_conditions.visibility_of_element_located((MainPageLocators.seventh_question_answer)))

    def get_eighth_question_answer(self):
        return WebDriverWait(self.driver,7).until(expected_conditions.visibility_of_element_located((MainPageLocators.eighth_question_answer)))