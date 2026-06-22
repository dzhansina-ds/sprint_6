from selenium import webdriver  
from locators.order_page_locators import OrderPageLocators
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
        assert order_page.get_current_url() == URL.start_page

    @allure.title('Проверка логотипа Яндекса')
    @allure.description('Нажимаем на логотип Яндекса. Через редирект открывается главная страница Дзена') 
    def test_header_logo_yandex(self,driver,order_page):
        original_window = order_page.get_current_window_handle()
        order_page.click_header_logo_yandex()
        order_page.switch_window(original_window)
        order_page.waiting_text_in_url('dzen.ru')

        assert 'dzen.ru' in order_page.get_current_url()