from selenium import webdriver  
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from .base_page import BasePage

class MainPage(BasePage):

    questions = [
        MainPageLocators.first_question_button,
        MainPageLocators.second_question_button,
        MainPageLocators.third_question_button,
        MainPageLocators.fourth_question_button,
        MainPageLocators.fifth_question_button,
        MainPageLocators.sixth_question_button,
        MainPageLocators.seventh_question_button,
        MainPageLocators.eighth_question_button
    ]

    answers = [
         MainPageLocators.first_question_answer,
        MainPageLocators.second_question_answer,
        MainPageLocators.third_question_answer,
        MainPageLocators.fourth_question_answer,
        MainPageLocators.fifth_question_answer,
        MainPageLocators.sixth_question_answer,
        MainPageLocators.seventh_question_answer,
        MainPageLocators.eighth_question_answer
    ]

    def click_question_button (self,index):
        self.accept_cookie()
        locator = self.questions[index]
        self.scrolling(locator)
        self.click_element(locator)

    def get_question_answer(self,index):
        locator = self.answers[index]
        return self.find_element_after_waiting(locator)