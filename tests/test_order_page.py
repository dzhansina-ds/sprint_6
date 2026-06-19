from selenium import webdriver  
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.urls import URL
from pages.order_page import OrderPage
import pytest
import allure 


class TestOrderPage():
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(URL.start_page)
        cls.order_page = OrderPage(cls.driver)

    @allure.title('Заказ самоката. Использование двух ноборов данных')
    @allure.description('Нажимаем на кнопку заказа самоката. Заполняем поля: Имя, Фамилия, Адрес, Станция метро, Телефон, Дата, Срок аренды, Цвет самоката, Комментарий')
    @pytest.mark.parametrize('order_button_place, name, surname, address, station, phone, date, comment',
        [
        ('top', 'Джан', 'Сина','г.Москва, ул. Шарикоподшипниковская д.28, кв.110', 'Дубровка', '89995551122','01.07.2026', 'Домофон не работает'),
        ('bottom','Роман','Рейнс','г.Москва, ул.Новоостаповская д.16, кв.304','Волгоградский проспект','89012736509','30.06.2026', 'Буду дома после 16:00')
        ]
    )
    def test_make_order (self,order_button_place,name, surname, address, station, phone, date,comment):
        self.driver.get(URL.start_page)

        self.order_page.make_order(order_button_place,name, surname, address, station, phone, date,comment)
        actual_header = self.order_page.get_text_of_header_success_order()
        assert 'Заказ оформлен' in actual_header

    @allure.title('Проверка логотипа "Самоката"')
    @allure.description('Нажимаем на логотип "Самоката". Попадаем на главную страницу "Самоката"') 
    def test_header_logo_samokat(self):
        self.driver.get(URL.start_page)
        self.order_page.click_top_order_button()
        self.order_page.click_header_logo_samokat()
        assert self.driver.current_url == URL.start_page

    @allure.title('Проверка логотипа Яндекса')
    @allure.description('Нажимаем на логотип Яндекса. Через редирект открывается главная страница Дзена') 
    def test_header_logo_yandex(self):
        original_window = self.driver.current_window_handle
        self.order_page.click_header_logo_yandex()
        WebDriverWait(self.driver, 7).until(expected_conditions.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('dzen.ru'))
        
        assert 'dzen.ru' in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()