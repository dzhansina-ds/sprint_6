import pytest
from selenium import webdriver
from data.urls import URL
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(URL.start_page)
    yield browser
    browser.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)