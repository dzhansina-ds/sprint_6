from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from data.urls import URL
from pages.main_page import MainPage
import allure 

class TestMainPage():
    driver = None
    
    @allure.title('Проверка появления текста ответа на первый вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с первым вопросом, открывается текст ответа')
    def test_important_questions_list_1 (self,driver,main_page):
        main_page.click_first_question_button()
        actual_text=main_page.get_first_question_answer().text
        assert actual_text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title('Проверка появления текста ответа на второй вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом со вторым вопросом, открывается текст ответа')
    def test_important_questions_list_2 (self,driver,main_page):
        main_page.click_second_question_button()
        actual_text=main_page.get_second_question_answer().text
        assert actual_text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.title('Проверка появления текста ответа на третий вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с третьим вопросом, открывается текст ответа')
    def test_important_questions_list_3 (self,driver,main_page):
        main_page.click_third_question_button()
        actual_text=main_page.get_third_question_answer().text
        assert actual_text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.title('Проверка появления текста ответа на четвертый вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с четвертым вопросом, открывается текст ответа')
    def test_important_questions_list_4 (self,driver,main_page):
        main_page.click_fourth_question_button()
        actual_text=main_page.get_fourth_question_answer().text
        assert actual_text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        
    @allure.title('Проверка появления текста ответа на пятый вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с пятым вопросом, открывается текст ответа')
    def test_important_questions_list_5 (self,driver,main_page):
        main_page.click_fifth_question_button()
        actual_text=main_page.get_fifth_question_answer().text
        assert actual_text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    
    @allure.title('Проверка появления текста ответа на шестой вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с шестым вопросом, открывается текст ответа')
    def test_important_questions_list_6 (self,driver,main_page):
        main_page.click_sixth_question_button()
        actual_text=main_page.get_sixth_question_answer().text
        assert actual_text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.title('Проверка появления текста ответа на седьмой вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с седьмым вопросом, открывается текст ответа')
    def test_important_questions_list_7 (self,driver,main_page):
        main_page.click_seventh_question_button()
        actual_text=main_page.get_seventh_question_answer().text
        assert actual_text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.title('Проверка появления текста ответа на восьмой вопрос в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с восьмым вопросом, открывается текст ответа')
    def test_important_questions_list_8 (self,driver,main_page):
        main_page.click_eighth_question_button()
        actual_text=main_page.get_eighth_question_answer().text
        assert actual_text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

