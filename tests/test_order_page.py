from selenium import webdriver  
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import URL
from pages.order_page import OrderPage
from data.order_page_data import OrderPageData
import pytest
import allure 


class TestOrderPage():

    @allure.title('Заказ самоката. Использование двух наборов данных')
    @allure.description('Нажимаем на кнопку заказа самоката. Заполняем поля: Имя, Фамилия, Адрес, Станция метро, Телефон, Дата, Срок аренды, Цвет самоката, Комментарий')
    @pytest.mark.parametrize('order_button_place, name, surname, address, station, phone, date, comment', OrderPageData.Order_test_data)
    def test_make_order (self,driver,order_page,order_button_place,name, surname, address, station, phone, date,comment):
        order_page.make_order(order_button_place,name, surname, address, station, phone, date,comment)
        assert order_page.is_watch_status_button_visible() is True

    @allure.title('Проверка логотипа "Самоката"')
    @allure.description('Нажимаем на логотип "Самоката". Попадаем на главную страницу "Самоката"') 
    def test_header_logo_samokat(self,driver,order_page):
        order_page.click_top_order_button()
        order_page.click_header_logo_samokat()
        assert driver.current_url == URL.start_page

    @allure.title('Проверка логотипа Яндекса')
    @allure.description('Нажимаем на логотип Яндекса. Через редирект открывается главная страница Дзена') 
    def test_header_logo_yandex(self,driver,order_page):
        original_window = driver.current_window_handle
        order_page.click_header_logo_yandex()
        WebDriverWait(driver, 7).until(expected_conditions.number_of_windows_to_be(2))

        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        WebDriverWait(driver, 10).until(expected_conditions.url_contains('dzen.ru'))
        
        assert 'dzen.ru' in driver.current_url