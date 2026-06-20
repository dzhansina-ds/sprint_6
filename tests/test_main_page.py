from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from data.urls import URL
from data.main_page_data import MainPageData
from pages.main_page import MainPage
import allure 

class TestMainPage():
    driver = None
    
    @allure.title('Проверка появления текста ответа на первый вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с первым вопросом, открывается текст ответа')
    def test_important_questions_list_1 (self,driver,main_page):
        main_page.click_first_question_button()
        actual_text=main_page.get_first_question_answer().text
        assert actual_text == MainPageData.answer_1

    @allure.title('Проверка появления текста ответа на второй вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом со вторым вопросом, открывается текст ответа')
    def test_important_questions_list_2 (self,driver,main_page):
        main_page.click_second_question_button()
        actual_text=main_page.get_second_question_answer().text
        assert actual_text == MainPageData.answer_2

    @allure.title('Проверка появления текста ответа на третий вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с третьим вопросом, открывается текст ответа')
    def test_important_questions_list_3 (self,driver,main_page):
        main_page.click_third_question_button()
        actual_text=main_page.get_third_question_answer().text
        assert actual_text == MainPageData.answer_3

    @allure.title('Проверка появления текста ответа на четвертый вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с четвертым вопросом, открывается текст ответа')
    def test_important_questions_list_4 (self,driver,main_page):
        main_page.click_fourth_question_button()
        actual_text=main_page.get_fourth_question_answer().text
        assert actual_text == MainPageData.answer_4
        
    @allure.title('Проверка появления текста ответа на пятый вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с пятым вопросом, открывается текст ответа')
    def test_important_questions_list_5 (self,driver,main_page):
        main_page.click_fifth_question_button()
        actual_text=main_page.get_fifth_question_answer().text
        assert actual_text == MainPageData.answer_5
    
    @allure.title('Проверка появления текста ответа на шестой вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с шестым вопросом, открывается текст ответа')
    def test_important_questions_list_6 (self,driver,main_page):
        main_page.click_sixth_question_button()
        actual_text=main_page.get_sixth_question_answer().text
        assert actual_text == MainPageData.answer_6

    @allure.title('Проверка появления текста ответа на седьмой вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с седьмым вопросом, открывается текст ответа')
    def test_important_questions_list_7 (self,driver,main_page):
        main_page.click_seventh_question_button()
        actual_text=main_page.get_seventh_question_answer().text
        assert actual_text == MainPageData.answer_7

    @allure.title('Проверка появления текста ответа на восьмой вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с восьмым вопросом, открывается текст ответа')
    def test_important_questions_list_8 (self,driver,main_page):
        main_page.click_eighth_question_button()
        actual_text=main_page.get_eighth_question_answer().text
        assert actual_text == MainPageData.answer_8

