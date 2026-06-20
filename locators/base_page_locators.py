from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePageLocators():
    cookie_button = [By.ID, 'rcc-confirm-button']
    header_logo_yandex = [By.XPATH, "//img[@alt='Yandex']"]
    header_logo_samokat = [By.XPATH, "//img[@alt='Scooter']"]
    top_order_button = [By.XPATH, "//div[contains(@class, 'Header_')]//button[text()='Заказать']"]
    bottom_order_button = [By.XPATH, "//div[contains(@class, 'Home_')]//button[text()='Заказать']"]